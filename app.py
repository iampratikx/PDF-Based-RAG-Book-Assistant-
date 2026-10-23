import streamlit as st
from dotenv import load_dotenv
import tempfile
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate


st.set_page_config(page_title="RAG Book Assistant")

st.title("📚 RAG Book Assistant")
st.write("Upload a PDF and ask questions from the document.")

# Local embedding model
@st.cache_resource
def get_embedding_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


embedding_model = get_embedding_model()

# Local Ollama LLM
llm = ChatMistralAI(model="mistral-small-2506")

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context,
say: "I could not find the answer in the document."
"""
    ),
    (
        "human",
        """Context:
{context}

Question:
{question}
"""
    )
])

# Upload PDF
uploaded_file = st.file_uploader(
    "Upload a PDF book",
    type="pdf"
)

if uploaded_file:
    if st.button("Create Vector Database"):
        with st.spinner("Processing PDF and creating database..."):

            # Save uploaded PDF temporarily
            with tempfile.NamedTemporaryFile(
                delete=False, suffix=".pdf"
            ) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                file_path = tmp_file.name

            try:
                # Load PDF
                loader = PyPDFLoader(file_path)
                docs = loader.load()

                # Split into chunks
                splitter = RecursiveCharacterTextSplitter(
                    chunk_size=1000,
                    chunk_overlap=200
                )
                chunks = splitter.split_documents(docs)

                if not chunks:
                    st.error("No text found in this PDF.")
                    st.stop()

                # Create ChromaDB
                vectorstore = Chroma.from_documents(
                    documents=chunks,
                    embedding=embedding_model,
                    persist_directory="chroma-db"
                )

                # Save database location in session
                st.session_state["db_created"] = True
                st.session_state["db_path"] = os.path.abspath("chroma-db")

                st.success(
                    f"Vector database created! "
                    f"Pages: {len(docs)}, Chunks: {len(chunks)}"
                )

            finally:
                if os.path.exists(file_path):
                    os.remove(file_path)

# Ask questions only after creating the database
if st.session_state.get("db_created", False):

    vectorstore = Chroma(
        persist_directory=st.session_state["db_path"],
        embedding_function=embedding_model
    )

    st.divider()
    st.subheader("Ask Questions From the Book")

    st.write(
        f"Chunks stored: {vectorstore._collection.count()}"
    )

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4,
            "fetch_k": 10,
            "lambda_mult": 0.5
        }
    )

    query = st.text_input("Enter your question")

    if query:
        with st.spinner("Searching document and generating answer..."):

            docs = retriever.invoke(query)

            if not docs:
                st.warning(
                    "I could not find the answer in the document."
                )
            else:
                context = "\n\n".join(
                    doc.page_content for doc in docs
                )

                final_prompt = prompt.invoke({
                    "context": context,
                    "question": query
                })

                response = llm.invoke(final_prompt)

                st.subheader("AI Answer")
                st.write(response.content)

                with st.expander("View retrieved chunks"):
                    for i, doc in enumerate(docs, start=1):
                        st.markdown(f"**Chunk {i}**")
                        st.write(doc.page_content)
                        st.caption(
                            f"Page: {doc.metadata.get('page', 'Unknown')}"
                        )

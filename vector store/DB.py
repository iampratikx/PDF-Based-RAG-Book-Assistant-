from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

docs = [
    Document(page_content="Python is widely used in artificial intelligence", metadata={"source": "AI_book"}),
    Document(page_content="Pandas is used for data analysis in python", metadata={"source": "DataScience_book"}),
    Document(page_content="Neural Networks are used in deep learning", metadata={"source": "DL_book"}),
]

embedding_model = HuggingFaceEmbeddings(
    model = "all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory="chroma-db"
)

result = vectorstore.similarity_search("what is used for data analysis?", k=2)

for r in result:
    print(r.page_content)
    print(r.metadata)

retriver = vectorstore.as_retriever()

docs = retriver.invoke("what is deep learning")

for d in docs:
    print(d)



# load pdf
# split chunks
# create embeddings
# store iinto chroma db

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


loader = PyPDFLoader(r"D:\RAG\Document loaders\DeepLearning.pdf")
docs = loader.load()


splitters = RecursiveCharacterTextSplitter(
    chunks_size = 1000,
    chunks_overlap = 200
)

chunks = splitters.split_documents(docs)

embedding_model = HuggingFaceEmbeddings(
    model = "all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma-db"
)










"""
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter

data = PyPDFLoader(r"D:\RAG\Document loaders\PratikChavanSoftwareDeveloperIntern .pdf")

docs = data.load()

splitter = TokenTextSplitter(
    chunk_size = 100,
    chunk_overlap=1
)

chunks = splitter.split_documents(docs)

print((chunks[0].page_content))

"""
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

data = PyPDFLoader(r"D:\RAG\Document loaders\PratikChavanSoftwareDeveloperIntern .pdf")

docs = data.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap=1
)

chunks = splitter.split_documents(docs)

print((chunks[0].page_content))
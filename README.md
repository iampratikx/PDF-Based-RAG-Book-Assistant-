# PDF-Based RAG Book Assistant

A PDF-based question-answering application built using Retrieval-Augmented Generation (RAG). The application processes uploaded PDF documents, retrieves relevant text chunks using semantic search, and generates context-aware answers using a Large Language Model (LLM).

## Features

- **PDF Loading:** Extract text from uploaded PDF documents.
- **Text Chunking:** Split documents into smaller chunks with configurable chunk size and overlap.
- **Text Embeddings:** Convert document chunks into vector representations using Hugging Face embeddings.
- **Vector Database:** Store and retrieve document embeddings using ChromaDB.
- **Semantic Retrieval:** Find relevant document chunks based on the user's question.
- **Context-Aware Answers:** Use a Mistral LLM to generate answers grounded in retrieved document content.
- **Interactive Interface:** Use Streamlit to interact with the application.

## Tech Stack

- **Programming Language:** Python
- **UI Framework:** Streamlit
- **LLM Framework:** LangChain
- **Language Model:** Mistral AI
- **Embeddings:** Hugging Face Embeddings
- **Vector Database:** ChromaDB
- **Core Concepts:** RAG, Semantic Search, Text Chunking, Vector Embeddings, MMR Retrieval

## How It Works

1. Upload a PDF document through the application.
2. Extract the document's text.
3. Split the extracted text into smaller chunks.
4. Generate embeddings for the text chunks.
5. Store the embeddings in ChromaDB.
6. Submit a question about the document.
7. Retrieve relevant chunks using similarity-based retrieval.
8. Pass the retrieved context and question to the Mistral LLM.
9. Display the generated answer in the Streamlit interface.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/iampratikx/PDF-Based-RAG-Book-Assistant-.git
cd PDF-Based-RAG-Book-Assistant-
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install Dependencies

If the project contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, install the dependencies listed in your project code and create a `requirements.txt` file.

### 4. Configure Environment Variables

If your selected model provider or embedding service requires an API key, configure it using environment variables or a local `.env` file, according to the libraries used in your implementation.

**Important:** Never upload API keys, passwords, or `.env` files containing secrets to GitHub.

### 5. Run the Application

If your Streamlit entry-point file is named `app.py`, run:

```bash
streamlit run app.py
```

If your main file has a different name, replace `app.py` with the correct filename.

## Project Structure

```text
PDF-Based-RAG-Book-Assistant-/
├── app.py
├── create_database.py
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: Update this structure to match the actual files and folders in your repository.*

## Learning Outcomes

- Understanding the Retrieval-Augmented Generation (RAG) pipeline.
- Working with document loading, text chunking, and embeddings.
- Using ChromaDB for vector storage and retrieval.
- Implementing semantic search and MMR-based retrieval.
- Integrating an LLM with retrieved document context.
- Building an interactive application using Streamlit and LangChain.

## Future Improvements

- Support multiple document formats.
- Add conversation history for follow-up questions.
- Improve document retrieval and answer evaluation.
- Add source references to help users verify generated answers.

## Author

**Pratik Chavan**

- GitHub: [@iampratikx](https://github.com/iampratikx)

---

If you find this project useful, feel free to explore the repository and suggest improvements.


# RAG (Retrieval-Augmented Generation) App  

## Overview  
This app demonstrates a local Retrieval-Augmented Generation (RAG) pipeline using:  
- **Backend**: A Flask-based API for embedding files and querying a local language model.  
- **Frontend**: A simple HTML/JavaScript interface to interact with the backend.  
- **Models**: Powered by Ollama, which runs models like `mistral` locally.  

## Features  
### 1. File Embedding  
- Upload PDF files to embed them into a vector database (ChromaDB).  
- The embeddings are stored locally to enable efficient document retrieval.  

### 2. Query Processing  
- Ask questions that retrieve relevant documents and generate responses using the language model.  

### 3. Local Deployment  
- No internet dependency as everything runs locally, ensuring privacy and control.  

---

## How to Run the App  

### Prerequisites  
1. **Python 3**: Ensure Python 3.8+ is installed on your system.  
2. **Ollama**: Install Ollama to serve the language models locally.  
3. **Dependencies**: Install required Python libraries using `pip`.  

### Backend Setup  
```bash
# Clone or copy this project to your local machine.
git clone <repository_url>
cd <repository_name>

# Create and activate a Python virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```
The backend server will start at `http://127.0.0.1:8080`.  

### Frontend Setup  
```bash
cd frontend
python -m http.server 8000
```
Open your browser and navigate to `http://127.0.0.1:8000`.  

### Running the Models  
```bash
# Start the Ollama service
ollama serve

# Pull the required models
ollama pull mistral
ollama pull nomic-embed-text
```

---

## Workflow  

### 1. Embed Files  
- Use the `/embed` endpoint via the frontend or a tool like Postman to upload PDF files.  
- The files are embedded into the ChromaDB vector store.  

### 2. Ask Questions  
- Use the `/query` endpoint via the frontend or a tool like Postman to ask questions.  
- The backend retrieves relevant documents from ChromaDB and generates a response using the language model.  

---

## Current State  
- **Backend**: Fully functional. It handles file embedding and query processing seamlessly when accessed via tools like Postman or Python scripts.  
- **Frontend**:  
  - Partially functional.  
  - The integration between the frontend and backend is incomplete due to issues with `OPTIONS` requests and CORS handling.  
  - Queries submitted via the frontend may not yet trigger a proper response.  

---

## Future Plans  
1. Resolve `OPTIONS` request handling in the backend to fully enable frontend queries.  
2. Enhance the frontend interface for a more user-friendly experience.  
3. Optimize the embedding process and model integration for improved performance.  
```

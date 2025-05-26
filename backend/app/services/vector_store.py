import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

# Initialize ChromaDB client and collection
chroma_client = chromadb.Client(Settings(persist_directory="./vector_db"))
collection = chroma_client.get_or_create_collection("documents")

# Load sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def add_document(doc_id, text, metadata=None):
    embedding = model.encode(text).tolist()
    collection.add(
        ids=[doc_id],
        embeddings=[embedding],
        documents=[text],
        metadatas=[metadata or {}]
    )

def query_documents(query, n_results=3):
    query_embedding = model.encode(query).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    return results 
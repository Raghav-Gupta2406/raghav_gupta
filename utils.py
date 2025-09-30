# utils.py
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document

def get_vector_db_retriever():
    """
    Creates a simple vector database retriever for demonstration purposes.
    """
    docs = [
        Document(page_content="The @traceable decorator is a simple way to log traces. You can add it to any function to automatically track its inputs, outputs, and errors in LangSmith."),
        Document(page_content="LangSmith supports adding metadata to traces. This is done by passing a 'metadata' dictionary to the @traceable decorator. You can also add metadata at runtime using the 'langsmith_extra' parameter."),
        Document(page_content="A run tree is a nested structure of runs. The @traceable decorator handles the creation and management of this tree for you automatically.")
    ]
    
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_db = FAISS.from_documents(docs, embedding_model)
    
    return vector_db.as_retriever(search_kwargs={"k": 2})
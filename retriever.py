import json

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_community.embeddings import FakeEmbeddings
from langchain_core.documents import Document 

embeddings = FakeEmbeddings(size=768)



# TODO: Load data/tweets.json
# page content is the tweet text
# the metadata is the author information

def prep_document(file_path): 
    """Preparing tweets as document for Faiss DB"""
    documents= []
    with open(file_path, 'r') as f:
        data = json.load(f)  
        for item in data: 
            doc = Document(page_content=item["tweet"], metadata= {"author":item["author"]})
            documents.append(doc)
    return documents    
file_path = "./data/tweets.json"
tweets = prep_document(file_path)

retriever = FAISS.from_documents(tweets, embeddings)

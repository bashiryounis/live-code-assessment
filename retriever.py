import json

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_community.embeddings import FakeEmbeddings



embeddings = FakeEmbeddings(size=768)



# TODO: Load data/tweets.json
# page content is the tweet text
# the metadata is the author information
tweets = []




retriever = FAISS.from_documents(tweets, embeddings)

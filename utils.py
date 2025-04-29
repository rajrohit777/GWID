from langchain.document_loaders import PyPDFLoader
import os

def load_pdf(path):
    loader = PyPDFLoader(path)
    return loader.load()

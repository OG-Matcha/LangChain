import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain.chains.question_answering import load_qa_chain
from dotenv import load_dotenv


def read_doc(directory):
    file_loader = PyPDFDirectoryLoader(directory)
    documents = file_loader.load()
    return documents


def chunk_data(docs, chunk_size=800, chunk_overlap=50):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    doc = text_splitter.split_documents(docs)
    return doc


def build_faiss(embeddings):
    doc = read_doc("LangChain/Chat With PDF/documents")
    documents = chunk_data(docs=doc)

    db = FAISS.from_documents(documents, embeddings)
    db.save_local("faiss_index")


def search(db, query, k=5):
    results = db.similarity_search(query, k=k)
    return results


def load_faiss(embeddings):
    return FAISS.load_local("faiss_index", embeddings)


def retrieve_answers(db, query, chain):
    doc_search = search(db, query)
    response = chain.invoke({"input_documents": doc_search, "question": query})
    return response['output_text']


if __name__ == "__main__":
    load_dotenv()

    embeddings = OpenAIEmbeddings(api_key=os.getenv('OPEN_API_KEY'))
    llm = OpenAI(api_key=os.getenv("OPEN_API_KEY"),
                 temperature=0.5, max_tokens=600)
    chain = load_qa_chain(llm, chain_type="stuff")

    # build_faiss(embeddings)

    db = load_faiss(embeddings)

    query = "中大附近有甚麼好吃的嗎?"

    answer = retrieve_answers(db, query, chain)
    print(answer)

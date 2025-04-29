import streamlit as st
from utils import load_and_embed_documents
from report_generator import generate_report
from noc_guidance import get_noc_guidance
from training_resources import get_training_opportunities
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import os

st.set_page_config(page_title="Groundwater AI Chatbot", layout="wide")
st.title("💧 Groundwater AI Chatbot")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["💬 Chat", "📄 Reports", "📜 NOC Guidance", "🎓 Training", "📤 Upload Docs"])

# Load Vectorstore
if "vectorstore" not in st.session_state:
    with st.spinner("Loading knowledge base..."):
        st.session_state.vectorstore = load_and_embed_documents()

### --- CHAT TAB ---
with tab1:
    st.subheader("Ask about groundwater data")
    query = st.text_input("Your question:")
    if query:
        retriever = st.session_state.vectorstore.as_retriever(search_kwargs={"k": 3})
        qa_chain = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(temperature=0.5),
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
        )
        result = qa_chain({"query": query})
        st.write("### Answer:")
        st.write(result["result"])

### --- REPORT TAB ---
with tab2:
    st.subheader("Generate Groundwater Report")
    area = st.text_input("Enter area/district name:")
    if st.button("Generate Report"):
        report = generate_report(area)
        st.markdown(report)

### --- NOC GUIDANCE TAB ---
with tab3:
    st.subheader("Get NOC Guidance")
    entity = st.selectbox("Entity Type", ["Industry", "Agriculture"])
    if st.button("Get NOC Info"):
        info = get_noc_guidance(entity)
        st.markdown(info)

### --- TRAINING TAB ---
with tab4:
    st.subheader("Training Opportunities")
    st.markdown(get_training_opportunities())

### --- UPLOAD DOCS TAB ---
with tab5:
    st.subheader("Upload PDF to extend knowledge base")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file:
        path = f"uploads/{uploaded_file.name}"
        with open(path, "wb") as f:
            f.write(uploaded_file.read())
        st.success(f"Uploaded: {uploaded_file.name}")

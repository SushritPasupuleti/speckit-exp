import streamlit as st
import requests

st.title("QnA App for PDFs")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
if uploaded_file is not None:
    response = requests.post("http://localhost:8000/api/upload", files={"file": uploaded_file})
    if response.status_code == 200:
        file_id = response.json().get("file_id")
        st.success(f"File uploaded successfully! File ID: {file_id}")

        question = st.text_input("Ask a question about the PDF:")
        if st.button("Get Answer"):
            qna_response = requests.post("http://localhost:8000/api/qna", json={"file_id": file_id, "question": question})
            if qna_response.status_code == 200:
                answer = qna_response.json().get("answer")
                st.write(f"Answer: {answer}")
            else:
                st.error("Failed to get an answer.")

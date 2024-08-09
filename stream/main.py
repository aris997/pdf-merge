import streamlit as st
import requests

st.title("PDF *Merge*")

# File uploader allows multiple files
uploaded_files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)

if st.button("Merge"):
    if uploaded_files and len(uploaded_files) > 1:
        try:
            # Prepare files to send in the POST request
            files = [("files", file) for file in uploaded_files]

            # Send POST request to the backend
            response = requests.post("http://pdfengine:3000/pdfmerger", files=files)

            if response.status_code == 200:
                # Provide the merged PDF as a download
                st.download_button("Download the merged PDF", response.content, file_name="merged.pdf")
            else:
                st.error(f"Error {response.status_code}: {response.text}")

        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")
    else:
        st.warning("Please upload at least two PDF files to merge.")

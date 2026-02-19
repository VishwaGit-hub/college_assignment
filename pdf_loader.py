import fitz

def extract_text(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    title = doc.metadata.get("title", "Research Paper")
    text = ""

    for page in doc:
        text += page.get_text()

    return title, text

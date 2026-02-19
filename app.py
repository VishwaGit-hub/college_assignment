import streamlit as st

from pdf_loader import extract_text
from keyword_extractor import extract_keywords
from wiki_rag import fetch_wiki_context
from section_splitter import split_sections
from context_builder import build_context
from explainer import generate_notes
from report_builder import make_report

st.title("📘 Research Paper Tutor AI")

uploaded = st.file_uploader("Upload a research paper PDF", type="pdf")

if uploaded:

    title, text = extract_text(uploaded)

    st.write("Processing paper...")

    sections = split_sections(text)

    keywords = extract_keywords(text)

    wiki_context = fetch_wiki_context(keywords)

    context = build_context(sections, wiki_context)

    notes = generate_notes(context)

    st.subheader("Generated Explanation")
    st.write(notes)

    report = make_report(title, notes)

    st.download_button(
        label="Download Notes (.txt)",
        data=report.encode("utf-8"),
        file_name="paper_notes.txt",
        mime="text/plain"
    )

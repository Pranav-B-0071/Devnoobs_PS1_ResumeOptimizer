
import spacy
import pdfplumber

def extract_text_from_pdf(pdf_file):
    """Extracts text from an uploaded PDF file using pdfplumber."""
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + "\n"
    return text.strip()

def extract_keywords(text):
    """
    Extracts keywords from the text using NLP.
    :param text: Resume text
    :return: List of extracted keywords
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    keywords = list(set([token.text for token in doc if token.is_alpha and not token.is_stop]))
    return keywords

if __name__ == "__main__":
    # Example usage
    with open("sample_resume.pdf", "rb") as pdf:
        resume_text = extract_text_from_pdf(pdf)
        print("Extracted Resume Text:\n", resume_text[:500])  # Print first 500 chars
        print("Extracted Keywords:", extract_keywords(resume_text))

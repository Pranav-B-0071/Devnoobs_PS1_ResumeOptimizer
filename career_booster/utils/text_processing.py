import spacy
import re
from sklearn.feature_extraction.text import TfidfVectorizer

# Load NLP model
nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    """Removes special characters, extra spaces, and converts text to lowercase."""
    text = re.sub(r"\s+", " ", text)  # Remove extra spaces
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove special characters
    return text.lower().strip()

def extract_keywords(text, top_n=10):
    """Extracts keywords from text using TF-IDF."""
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform([text])
    keywords = vectorizer.get_feature_names_out()
    
    return keywords[:top_n]  # Return top N keywords

def get_named_entities(text):
    """Extracts named entities (skills, organizations, etc.) from text."""
    doc = nlp(text)
    entities = {ent.text: ent.label_ for ent in doc.ents}
    return entities

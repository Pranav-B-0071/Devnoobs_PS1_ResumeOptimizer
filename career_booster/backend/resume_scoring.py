import torch
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_resume_score(resume_text, job_description):
    """Calculate resume-job similarity score using Sentence BERT."""
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embedding = model.encode(job_description, convert_to_tensor=True)

    similarity_score = util.pytorch_cos_sim(resume_embedding, job_embedding).item()
    
    return round(similarity_score * 100, 2)

def generate_feedback(resume_text, job_description):
    """Generate actionable feedback based on missing keywords."""
    resume_words = set(resume_text.lower().split())
    job_words = set(job_description.lower().split())

    missing_keywords = job_words - resume_words
    feedback = f"Consider adding these keywords to your resume: {', '.join(missing_keywords)}"
    
    return feedback

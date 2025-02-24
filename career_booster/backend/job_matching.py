from sentence_transformers import SentenceTransformer, util

# Load a pre-trained SentenceTransformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

def match_resume_with_job(resume_keywords, job_description):
    """Matches resume keywords with job description and finds missing skills."""
    
    # Ensure job_description is processed into keywords
    if isinstance(job_description, str):
        job_keywords = job_description.split()  # Tokenize if it's a string
    else:
        job_keywords = job_description  # Assume it's already tokenized

    # Compute embeddings
    resume_embeddings = model.encode(resume_keywords, convert_to_tensor=True)
    job_embeddings = model.encode(job_keywords, convert_to_tensor=True)

    # Compute cosine similarity matrix
    similarity_matrix = util.pytorch_cos_sim(resume_embeddings, job_embeddings)
    
    # Identify missing skills: If similarity is low, consider it missing
    missing_skills = [
        job_keywords[i] for i in range(len(job_keywords))
        if similarity_matrix[:, i].mean().item() < 0.5  # Threshold can be adjusted
    ]

    return missing_skills  # Returns a LIST instead of a float


if __name__ == "__main__":
    # Example usage
    resume_text = "Experience in Python, machine learning, and data analysis."
    job_description = "Looking for a data scientist with expertise in Python and ML."
    
    score = match_resume_to_job(resume_text, job_description)
    print(f"Resume and job description similarity score: {score:.2f}")


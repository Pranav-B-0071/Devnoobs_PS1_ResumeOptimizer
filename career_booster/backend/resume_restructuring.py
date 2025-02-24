import google.generativeai as genai
import os

# Manually set API key (Replace with your actual API key)
GENAI_API_KEY = "AIzaSyC4aQmveouqu9mQA9zKo9OKITycgiyvfMs"
genai.configure(api_key=GENAI_API_KEY)

def restructure_resume_with_gemini(resume_text, job_description):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"Optimize this resume to align with the job description: \n\nJob Description: {job_description}\n\nResume:\n{resume_text}"
    
    response = model.generate_content(prompt)
    return response.text if response.text else "Error generating optimized resume."

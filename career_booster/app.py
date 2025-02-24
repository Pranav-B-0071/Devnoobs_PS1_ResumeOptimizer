import streamlit as st
from backend.resume_processing import extract_text_from_pdf, extract_keywords
from backend.job_matching import match_resume_with_job
from backend.course_recommendation import get_free_courses_youtube, get_free_datasets_kaggle
from backend.web_scraping import scrape_linkedin_jobs
from backend.roadmap_generator import generate_learning_roadmap
from backend.resume_scoring import calculate_resume_score, generate_feedback
from backend.resume_restructuring import restructure_resume_with_gemini
from backend.tavily_search import search_career_insights  # Tavily Integration
from backend.pdf_formatter import save_resume_as_pdf  # Convert optimized resume to PDF
from utils.text_processing import clean_text
import sys
import os

sys.path.append(os.path.abspath("S:/career_booster"))

# ✅ Ensure set_page_config is first
st.set_page_config(page_title="Career Booster", layout="wide")

st.title("🚀 Career Booster App")

# Sidebar Inputs
st.sidebar.header("📂 Upload Resume")
uploaded_file = st.sidebar.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_title = st.sidebar.text_input("Enter Job Title")
job_description = st.sidebar.text_area("Paste Job Description (Leave blank for auto-fetch)")
prep_time_weeks = st.sidebar.number_input("Preparation Time (Weeks)", min_value=1, max_value=52, value=4)

if uploaded_file and job_title:
    with st.spinner("Processing Resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)
        resume_keywords = extract_keywords(resume_text)  # Ensure this returns a list

    # Fetch Job Description if not provided
    if not job_description:
        with st.spinner("Fetching job descriptions from LinkedIn..."):
            job_descriptions = scrape_linkedin_jobs(job_title)
            job_description = " ".join(job_descriptions[:3]) if job_descriptions else ""

    with st.spinner("Matching Resume with Job Description..."):
        missing_skills = match_resume_with_job(resume_keywords, job_description)
        if isinstance(missing_skills, float):  # Ensure it's a list
            missing_skills = []

    # ✅ Resume Scoring & Feedback
    with st.spinner("Calculating Resume Score..."):
        resume_score = calculate_resume_score(resume_text, job_description)
        feedback = generate_feedback(resume_text, job_description)

    st.subheader("📊 Resume Score & Feedback")
    st.write(f"**Score:** {resume_score}%")
    st.write(f"**Feedback:** {feedback}")

    # ✅ AI Resume Restructuring (Using Gemini)
    if st.button("Optimize Resume"):
        with st.spinner("Optimizing Resume with Gemini..."):
            optimized_resume = restructure_resume_with_gemini(resume_text, job_description)

        # Convert Optimized Resume to PDF
        pdf_path = save_resume_as_pdf(optimized_resume)


        st.subheader("📝 Optimized Resume")
        st.text_area("Updated Resume", optimized_resume, height=300)
        st.download_button("📥 Download Optimized Resume (PDF)", pdf_path, file_name="Optimized_Resume.pdf")

    # ✅ Career Insights (Using Tavily Web Search)
    st.subheader("🌐 Career Insights (Powered by Tavily)")
    with st.spinner("Fetching career insights..."):
        career_insights = search_career_insights(job_title)
    st.write(career_insights if career_insights else "No insights found.")

    # ✅ Missing Skills
    st.subheader("🔍 Missing Skills")
    if missing_skills:
        st.write("These skills are missing from your resume:")
        st.write(", ".join(missing_skills))
    else:
        st.success("✅ Your resume matches the job description well!")

    # ✅ Fetch Free Courses
    with st.spinner("Fetching free courses..."):
        courses = []
        for skill in missing_skills:
            try:
                courses.extend(get_free_courses_youtube(skill))
                courses.extend(get_free_datasets_kaggle(skill))
            except Exception as e:
                st.error(f"Error fetching courses for {skill}: {str(e)}")

    # ✅ Recommended Courses
    st.subheader("📚 Recommended Free Courses")
    if courses:
        for title, url in courses:
            st.markdown(f"- [{title}]({url})")
    else:
        st.warning("⚠️ No free courses found. Try refining the job title or skills.")

    # ✅ Generate Learning Roadmap
    with st.spinner("Generating Roadmap..."):
        roadmap = generate_learning_roadmap(missing_skills, prep_time_weeks)

    st.subheader("🗺️ Learning Roadmap")
    if roadmap:
        for week, tasks in roadmap.items():
            st.write(f"**{week}**")
            for task in tasks:
                st.write(f"- {task}")
    else:
        st.warning("⚠️ No roadmap generated. Ensure you have missing skills and course recommendations.")

else:
    st.info("📢 Upload a resume and enter a job title to get started!")

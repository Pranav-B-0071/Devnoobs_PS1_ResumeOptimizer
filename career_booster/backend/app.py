import streamlit as st
from backend.resume_processing import extract_text_from_pdf, extract_keywords
from backend.job_matching import match_resume_with_job
from backend.course_recommendation import get_free_courses_youtube, get_free_datasets_kaggle
from backend.web_scraping import scrape_linkedin_jobs
from backend.roadmap_generator import generate_learning_roadmap
from utils.text_processing import clean_text

st.title("🚀 Career Booster App")

# User Inputs
st.sidebar.header("📂 Upload Resume")
uploaded_file = st.sidebar.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_title = st.sidebar.text_input("Enter Job Title")
job_description = st.sidebar.text_area("Paste Job Description (or leave blank for auto-fetch)")
prep_time_weeks = st.sidebar.number_input("Preparation Time (Weeks)", min_value=1, max_value=52, value=4)

if uploaded_file and job_title:
    with st.spinner("Processing Resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)
        resume_keywords = extract_keywords(resume_text)

    # Get Job Description
    if not job_description:
        with st.spinner("Fetching job descriptions from LinkedIn..."):
            job_descriptions = scrape_linkedin_jobs(job_title)
            job_description = " ".join(job_descriptions[:3])

    with st.spinner("Matching Resume with Job Description..."):
        missing_skills = match_resume_with_job(resume_keywords, job_description)

    st.subheader("🔍 Missing Skills")
    st.write(missing_skills)

    with st.spinner("Fetching free courses..."):
        courses = []
        for skill in missing_skills:
            courses.extend(get_free_courses_youtube(skill))
            courses.extend(get_free_datasets_kaggle(skill))

    st.subheader("📚 Recommended Free Courses")
    for title, url in courses:
        st.markdown(f"- [{title}]({url})")

    with st.spinner("Generating Roadmap..."):
        roadmap = generate_learning_roadmap(missing_skills, courses, prep_time_weeks)

    st.subheader("🗺️ Learning Roadmap")
    for week, tasks in roadmap.items():
        st.write(f"**{week}**")
        for task in tasks:
            st.write(f"- {task}")

else:
    st.info("Upload a resume and enter job title to proceed.")

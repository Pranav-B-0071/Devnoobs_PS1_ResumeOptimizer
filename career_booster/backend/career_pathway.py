import requests
from bs4 import BeautifulSoup

def scrape_salary_data(job_title, location="United States"):
    """Scrape LinkedIn salary data for the given job title."""
    job_title = job_title.replace(" ", "-").lower()
    url = f"https://www.linkedin.com/salary/search?keywords={job_title}&location={location}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    salary_info = soup.find("span", class_="text-heading-xlarge")
    
    return salary_info.text if salary_info else "Salary data unavailable"

def recommend_career_path(job_title):
    """Suggest next career steps based on job title."""
    career_paths = {
        "Software Engineer": ["Senior Software Engineer", "Tech Lead", "Engineering Manager"],
        "Data Scientist": ["Senior Data Scientist", "ML Engineer", "AI Researcher"],
        "Product Manager": ["Senior Product Manager", "Director of Product", "VP of Product"]
    }

    return career_paths.get(job_title, ["Career path data unavailable"])

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_linkedin_jobs(job_title):
    """Scrape job descriptions from LinkedIn using Selenium."""
    
    linkedin_url = f"https://www.linkedin.com/jobs/search/?keywords={job_title.replace(' ', '%20')}"
    print("🔗 Trying to access:", linkedin_url)  # Debugging
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(linkedin_url)

        time.sleep(5)  # Allow time for page to load

        job_elements = driver.find_elements(By.CLASS_NAME, "base-search-card__title")
        job_descriptions = [job.text for job in job_elements]

        driver.quit()
        return job_descriptions if job_descriptions else ["No jobs found."]
    
    except Exception as e:
        print("❌ Error accessing LinkedIn:", str(e))
        return ["LinkedIn scraping failed."]



if __name__ == "__main__":
    # Example usage
    linkedin_url = "https://www.linkedin.com/jobs/search/?keywords=data%20scientist"
    descriptions = scrape_linkedin_job_descriptions(linkedin_url)
    print("Scraped Job Descriptions:", descriptions)

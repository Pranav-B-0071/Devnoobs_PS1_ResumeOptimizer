import requests

# Manually set Tavily API Key (Replace with your actual API key)
TAVILY_API_KEY = "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"

def search_career_insights(job_title):
    query = f"Latest trends and career growth for {job_title}"
    url = f"https://api.tavily.com/search?q={query}&api_key={TAVILY_API_KEY}"

    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get("results", [])
        return "\n".join([f"- [{r['title']}]({r['url']})" for r in results[:5]])
    return "No insights available."

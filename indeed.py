
import urllib
import requests
from bs4 import BeautifulSoup

LIMIT = 0
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&l=%EC%84%9C%EC%9A%B8&start={LIMIT}&vjk=4ae5eb5bb613a826"


def extract_indeed_pages():

    result = requests.get(URL)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_indeed_jobs(last_pages):
    jobs = []
    for page in range(last_pages):
        print(f"SCRAPPING PAGE:{page+1}")
        result = requests.get(
            f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&l=%EC%84%9C%EC%9A%B8&start={page*LIMIT}&vjk=4ae5eb5bb613a826")  # page*
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all(
            "div", {"class": "result"})

        for result in results:
            title = result.find(
                "a", {"class", "jcs-JobTitle"}).find("span").string
            company = result.find("span", {"class": "companyName"}).string
            location = result.find("div", {"class": "companyLocation"}).string
            job_dict = {"title": title,
                        "company": company, "location": location}
            jobs.append(job_dict)
    return jobs


def get_jobs():
    last_indeed_pages = extract_indeed_pages()
    jobs = extract_indeed_jobs(last_indeed_pages)
    return jobs

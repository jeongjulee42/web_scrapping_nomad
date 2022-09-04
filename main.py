# 1. 파이썬을 써서 url로 접근
# 2. 페이지가 몇개인지 알아낸다.
# 3. 페이지 하나씩 들어가준다.
import urllib
import requests
from bs4 import BeautifulSoup
from indeed import extract_indeed_pages, extract_indeed_jobs, get_jobs
from save import save_to_file

jobs = get_jobs()
save_to_file(jobs)

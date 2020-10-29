from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import datetime

webdriver_options = webdriver.ChromeOptions()
webdriver_options.add_argument('headless')
driver =  webdriver.Chrome("chromedriver.exe")
wait = WebDriverWait(driver, 10)

from Linkedin_Crawler import Login_linkedin, scroll, get_all_links, crawl_skills

Login_linkedin()
print ("Logging in...: ")


company = input("Put Company Name")
region = "대한민국"

header = "https://www.linkedin.com/company/"

def refine(c):
    c_ref = "-".join(c.split(" ")).lower()
    return c_ref

link = header + refine(company) + "/" + "people/?keywords={}".format(region)
driver.get(link)

print ("Scrolling...")
scroll()
links = get_all_links()

wait = WebDriverWait(driver, 10)

results = []

from tqdm import tqdm_gui
for i in tqdm_gui(0,len(links)):
    link = links[i]
    try :
        results.append(crawl_skills(link))
    except TimeoutException:
        pass

data = {}

for i in results:
    key = list(i.keys())[0]
    val = list(i.values())[0]
    if key not in data.keys():
        data[key]=val
    else:
        for j in val:
            data[key].append(j)
import json
now = datetime.datetime.now()
with open('linkedin_JD_{}_{}.json'.format(company,now.strftime('%Y-%m-%d %H:%M:%S')), 'w', encoding='UTF-8') as f:
    json.dump(data, f, ensure_ascii=False)


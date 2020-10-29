import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import urllib
from urllib import request
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

webdriver_options = webdriver.ChromeOptions()
webdriver_options.add_argument('headless')
driver =  webdriver.Chrome("chromedriver.exe")
wait = WebDriverWait(driver, 10)


def Login_linkedin():
    url = "https://www.linkedin.com/feed/"
    udr = {'User-Agent': 'Mozilla/5.0'}

    driver.get(url)
    driver.find_element_by_xpath('/html/body/div/main/p/a').click()

    ID = input("ID (Email)")
    PASS = input("PASSWORD")

    elem = driver.find_element_by_xpath('//*[@id="username"]')
    elem.send_keys(ID)
    elem = driver.find_element_by_xpath('//*[@id="password"]')
    elem.send_keys(PASS)

    try:
        driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[4]/button').click()
    except:
        driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button').click()


def scroll():
    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height            [5]
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height


def get_all_links():
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    people = soup.find_all("li", {"class": "org-people-profiles-module__profile-item"})

    links = []
    for i in people:
        try:
            link = "https://www.linkedin.com/" + \
                   i.find("a", {"class": "ember-view link-without-visited-state"}, href=True)["href"]
            links.append(link)
        except TypeError:
            pass
    return links


def crawl_skills(profile):
    driver.get(profile)
    scroll()

    button_path = '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[6]/div/section/div[2]/button'

    element = wait.until(EC.presence_of_element_located((By.XPATH, button_path)))

    driver.find_element_by_xpath(button_path).send_keys(Keys.ENTER)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    skills = soup.find_all("span", {"class": "pv-skill-category-entity__name-text t-16 t-black t-bold"})
    skills = [i.text.strip() for i in skills]

    position = soup.find("h2", {"class": "mt1 t-18 t-black t-normal break-words"}).text.strip()
    return {position: skills}
# Selenium_Linkedin_Crawler
Using Selenium to automate process of collect (anonymously) skillsets of people working for selected company

# Description

## Introduction
Linkedin is open platform in career market. It enables many people to get access to career and reqruitment related information of various companies. Many jobseekers and reqruiters use them. 

However, it is kind of time consuming process to manually seek for what you want in linkedin. This program, automates the process of:
* Choose a company
* And manually take a look what kind of skillsets people working for that company has

Of course it collects the information of people who agreed to display their data on Linkedin platform, and since there could be privacy issues the coide definitely collect data anonymously. As I know, there exists some 3rd party APIs, and ugins Request is more efficient way for crawling programs in general, but for two reasons I use selenium:

* Since Linkedin is reactive webpage, and requires log-in, it is more easier and intuitive to use Seleinium, and
* Using urllib request to scrape from services like Linkedin could be problematic, if they prohibit such activity. However, manually searching for information through the platform is allowed, so I used Selenium which merely automates process we manually do. 


## How to Use:
* If you don't have chromedriver, you need to install the right version of Chromedriver, which matches your browser. 
* You could run 'main.py'file, which loads crawling functions from 'Linkedin_Crawling.py' file
* When you run 'main.py', you could enter the name of company you wuold like to search. You could change minor parts of codes 
* This use selenium, and chooses objects to click with xpath selector, so if the Linkedin page architecture changes, you may have to change codes



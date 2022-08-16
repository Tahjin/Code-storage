#could be what im looking for but pays in amozon gift cards
#https://free-lottery.net/ 
#
#https://lovefreelotto.com/
#
#https://www.lotterypost.com/game/186/results
#

# from bs4 import BeautifulSoup
# import requests

# # HTML From Website
# url = 'https://www.lotterypost.com/game/186/results'

# website = requests.get(url)
# print(website.status_code)

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



Path = Service("C:/Users/Talyn/Documents/Exclusion/msedgedriver.exe")
# Path = r"C:/Users/Talyn/Documents/Exclusion/msedgedriver.exe"
# for this example im useing microsoft edge
driver = webdriver.Edge(service=Path)
url = "https://www.lotterypost.com/game/186/results"
driver.get(url)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "resultsDrawDate"))
    )
    for i in main:
        print(i.text)
    # #style-scope ytd-video-primary-info-renderer

    #best way so far is useing xpath
    # main = WebDriverWait(driver, 10).until(
    #     EC.presence_of_all_elements_located((By.XPATH, '//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[1]'))
    # )
    # for i in main:
    #     print(i.text)
finally:
    print("All is well")
    driver.quit()

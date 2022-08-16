# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

Path = Service("C:/Users/Talyn/Documents/Exclusion/msedgedriver.exe")
driver = webdriver.Edge(service=Path)
url = "https://www.lotterypost.com/game/186/results"
driver.get(url)

#driver.get() comes after page click
#+", "
#don't put writeing in try statement i think

j=5
currentUrl = url
while j!=0:
    page = driver.find_element(By.LINK_TEXT, "{0}".format(j))
    page.click()
    currentUrl = driver.current_url
    driver.get(currentUrl)    
    try:
        Date = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "resultsDrawDate"))
        )
        Bonus = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "red"))
        )
        for date in range(len(Date)):
            print(Date[date].text+", "+Bonus[date].text)
    finally:
       print("All is well")    

    j-=1
driver.quit()
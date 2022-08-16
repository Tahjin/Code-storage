import openpyxl
# import re
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

Excel_Path = 'C:/Users/Talyn/Documents/Exel sheets1/Lotto_Data.xlsx'
wbook = openpyxl.load_workbook(Excel_Path)
ws = wbook.active

Path = Service("C:/Users/Talyn/Documents/Exclusion/msedgedriver.exe")
# Path = r"C:/Users/Talyn/Documents/Exclusion/msedgedriver.exe"
# for this example im useing microsoft edge
driver = webdriver.Edge(service=Path)
#
url = "https://www.lotterypost.com/game/186/results"
driver.get(url)
#Thursday, April 1, 2021  oldest date so far
#Thursday, April 1, 2020

j=4
currentUrl = url
while j!=0:
    currentUrl = driver.current_url
    driver.get(currentUrl)
    page = driver.find_element(By.LINK_TEXT, "{0}".format(j))
    page.click()        

    try:

        Date = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "resultsDrawDate"))
        )
        Numbers = []
    
        Bonus = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "red"))
        )

        #### This bellow fills Numbers[]
        #num1 = driver.find_elements_by_xpath('//*[@id="resultsTable"]/table/tbody/tr')
        num1 = driver.find_elements(by=By.XPATH, value='//*[@id="resultsTable"]/table/tbody/tr')
    
        for i in range(len(num1)):
            #num2 = driver.find_elements_by_xpath('//*[@id="resultsTable"]/table/tbody/tr[{0}]/td/div/div[2]/div[1]/ul/li'.format(i+1))
            num2 = driver.find_elements(by=By.XPATH, value='//*[@id="resultsTable"]/table/tbody/tr[{0}]/td/div/div[2]/div[1]/ul/li'.format(i+1))
            Numbers.append("")

            for li in num2:
                Numbers[i]+=str(li.text)+" "


        def isNewDate(index):

            # ws.append([Date[index].text,Numbers[index],Bonus[index].text])
            #
            #"yes"+str(index)
            print(Date[index].text+", "+Numbers[index]+", "+Bonus[index].text)

    
        i=len(Date)-1
        while i>=0:
            isNewDate(i)
            i-=1

    finally:
        print("All is well")
        # wbook.save('C:/Users/Talyn/Documents/Exel sheets1/Lotto_Data.xlsx')

    j-=1
    sleep(1)      
    
driver.quit()
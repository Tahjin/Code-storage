import openpyxl
from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

Excel_Path = 'C:/Users/Talyn/Documents/Exel sheets1/Lotto_Data.xlsx'
wbook = openpyxl.load_workbook(Excel_Path)
ws = wbook.active

Path = Service("C:/Users/Talyn/Documents/Exclusion/msedgedriver.exe")
driver = webdriver.Edge(service=Path)
url = "https://www.lotterypost.com/game/186/results"
driver.get(url)

#driver.get() comes after page click
#+", "
#don't put writeing in try statement i think

  
try:
    Date = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "resultsDrawDate"))
    )
    Bonus = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "red"))
    )
    Numbers = []

    num1 = driver.find_elements(By.XPATH, '//*[@id="resultsTable"]/table/tbody/tr')
    
    for n in range(len(num1)):
            
        num2 = driver.find_elements(By.XPATH, '//*[@id="resultsTable"]/table/tbody/tr[{0}]/td/div/div[2]/div[1]/ul/li'.format(n+1))
        Numbers.append("")

        for li in num2:
            Numbers[n]+=str(li.text)+" "

    def isNewDate(index):


        ws.append([Date[index].text,Numbers[index],Bonus[index].text])

    
    i=len(Date)-1
    while i>=0:
        isNewDate(i)
        i-=1
finally:
    print("All is well")
    wbook.save('C:/Users/Talyn/Documents/Exel sheets1/Lotto_Data.xlsx')
    

driver.quit()
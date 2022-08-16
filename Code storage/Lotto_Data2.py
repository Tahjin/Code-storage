import openpyxl
import re
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Excel_Path = 'C:/Users/Talyn/Documents/Exel sheets1/Lotto_Data.xlsx'
wbook = openpyxl.load_workbook(Excel_Path)
ws = wbook.active

Path = Service("C:/Users/Talyn/Documents/Exclusion/msedgedriver.exe")
# Path = r"C:/Users/Talyn/Documents/Exclusion/msedgedriver.exe"
# for this example im useing microsoft edge
driver = webdriver.Edge(service=Path)
url = "https://www.lotterypost.com/game/186/results"
driver.get(url)

#Thursday, April 1, 2020
#Thursday, December 30, 2021
try:
    Date = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "resultsDrawDate"))
    )
    Numbers = []
    
    Bonus = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "red"))
    )

    #### This bellow fills Numbers[]
    num1 = driver.find_elements_by_xpath('//*[@id="resultsTable"]/table/tbody/tr')
    
    for i in range(len(num1)):
        num2 = driver.find_elements_by_xpath('//*[@id="resultsTable"]/table/tbody/tr[{0}]/td/div/div[2]/div[1]/ul/li'.format(i+1))
        Numbers.append("")

        for li in num2:
            Numbers[i]+=str(li.text)+" "

    ####reverse the list


    #### This bellow only allows new information to be added
    Months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6
        , "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
    #to see if it's new it conpares from txt file
    
    with open("c:/Users/Talyn/Documents/VS python/Main/PythonProjects/LottoMemory.txt", 'r') as Memory:
        line = Memory.read()
        monthRegex = re.compile(r", \D+\s")
        yearRegex = re.compile(r"\d{4}")
        dateRegex = re.compile(r"\s\d+,")
        findMonth = monthRegex.findall(line)[0][2:-1]
        findYear = yearRegex.findall(line)[0]
        findDate = dateRegex.findall(line)[0][1:-1]

        i = len(Date)-1
        while i!=-1:
            newMonth = monthRegex.findall(Date[i].text)[0][2:-1]
            newYear = yearRegex.findall(Date[i].text)[0]
            newDate = dateRegex.findall(Date[i].text)[0][1:-1]

            #
            if int(newYear)>=int(findYear) and Months[newMonth]>=Months[findMonth] and int(newDate)>int(findDate):
                ws.append([Date[i].text,Numbers[i],Bonus[i].text])
                i-=1
            else:
                i-=1
                continue
        Memory.close()
    ####

    # Updates Memory
    with open("c:/Users/Talyn/Documents/VS python/Main/PythonProjects/LottoMemory.txt", 'w') as Memory:
        Memory.write(Date[0].text)
        Memory.close()
    
finally:
    print("All is well")
    wbook.save('C:/Users/Talyn/Documents/Exel sheets1/Lotto_Data.xlsx')
    driver.quit()

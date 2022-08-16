from selenium import webdriver
from selenium.webdriver.common.by import By

#
driver = webdriver.Edge("C:/Users/Talyn/Documents/Exclusion/msedgedriver.exe")



#'//span[@class="item-price"]' this repesents span class="item-price"
#http://econpy.pythonanywhere.com/ex/001.html

i=1
while i<=5:
    print("-"*25)
    url = "http://econpy.pythonanywhere.com/ex/00{0}.html".format(str(i))
    driver.get(url)
    buyers = driver.find_elements(By.XPATH, '//div[@title="buyer-name"]')
    prices = driver.find_elements(By.XPATH, '//span[@class="item-price"]')

    for j in range(len(buyers)):
        print(buyers[j].text+" : "+prices[j].text)    
    i+=1
#Based on this I can see two potential problems on my other program
#loops are overlaping
#I didn't use driver.get and edit the url

driver.close()
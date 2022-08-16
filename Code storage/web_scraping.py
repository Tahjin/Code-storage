from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



Path = Service("C:/Users/Talyn/Documents/Exclusion/msedgedriver.exe")
# Path = r"C:/Users/Talyn/Documents/Exclusion/msedgedriver.exe"
# for this example im useing microsoft edge
driver = webdriver.Edge(service=Path)
url = "https://www.youtube.com/watch?v=0gEkNVq1ct0&t=1066s"
driver.get(url)

try:
    # main = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "info-contents"))
    # )
    # print(main.text)
    #style-scope ytd-video-primary-info-renderer

    #best way so far is useing xpath
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="container"]/h1/yt-formatted-string'))
    )
    for i in main:
        print(i.text)
finally:
    print("All is well")
    driver.quit()

# test = driver.find_elements(By.ID, "info-contents")
# print(test[0].text)
# print("-"*25)



# search = driver.find_elements_by_class_name("style-scope ytd-video-primary-info-renderer")
# print(search)





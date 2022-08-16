from bs4 import BeautifulSoup
import requests

url = "https://www.youtube.com/watch?v=0gEkNVq1ct0&t=1958s"

website = requests.get(url)
soup = BeautifulSoup(website.content, 'html.parser')#, value="Google Search"
title = soup.find_all('h1')

print(title)
print("All is well")

from bs4 import BeautifulSoup
import requests

url = "https://www.google.com/"

website = requests.get(url).text
soup = BeautifulSoup(website, 'lxml')#, value="Google Search"
words = soup.find_all('input', class_='lsb')#
#intresting on the site the class is gNO89b when i used value the class is lsb
print(words)
print("All is well")
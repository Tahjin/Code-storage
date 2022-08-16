from bs4 import BeautifulSoup
import requests

urls = [""]
#https://www.youtube.com/watch?v=0gEkNVq1ct0&t=1789s
#https://www.youtube.com/watch?v=0gEkNVq1ct0&t=1960s


for url in urls:
    def Scrape_views(url):
        r = BeautifulSoup(requests.get(url).text, "html.parser")
        # veiws works but why?
        veiws = r.select_one('meta[itemprop="interactionCount"][content]')['content']

        data = {"veiws": veiws}
        return data
    print(Scrape_views(url))

# # A way to find meta class
# import metadata_parser

# url = "https://www.youtube.com/watch?v=0gEkNVq1ct0&t=1958s"
# page = metadata_parser.MetadataParser(url)
# # print(page.metadata)
# print(page.get_metadatas("title"))

#

print("All is well")


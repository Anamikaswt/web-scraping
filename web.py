from bs4 import BeautifulSoup
import requests
import json

web_api="https://en.wikipedia.org/wiki/Python_(programming_language)"
web_url = requests.get(web_api)
data = web_url.json
soup=BeautifulSoup(web_url.text,"html.parser")
div=soup.find("div",class_="vector-body")
div1=soup.find("table",class_="infobox vevent").get_text()

new_div=soup.find_all("td",class_="infobox-data")
text1=soup.find_all("th",class_="infobox-label")
for i in text1:
    print(i.get_text())

for i  in new_div:
    all_data=i.get_text()
    print("       ",all_data)



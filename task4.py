from task1 import scrape_top_list
from bs4 import BeautifulSoup
import requests
import json
detail_of_movie=scrape_top_list()
director=[]
language=[]
country=[]
def scrape_movie_details(movie_url):
    userinput=int(input("enter the position :"))
    movies=movie_url[userinput-1]["main_url"]
    imbd_url = requests.get(movies)
    soup = BeautifulSoup(imbd_url.text ,"html.parser")
    main_div_details=soup.find("section",class_="ipc-page-section ipc-page-section--base")
    # main_div = soup.find("div",data_testid="title-details-section",class_="styles_MetaDataContainer-sc-12uhu9s-0 cgqHBf")
    return main_div_details
print(scrape_movie_details(detail_of_movie))

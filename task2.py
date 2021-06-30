from task1 import scrape_top_list
from bs4 import BeautifulSoup
import requests
import json

movies_name= scrape_top_list()
def group_by_year(movies):
    year1=[]
    for i in movies:
        top_year=i["year"]
        if top_year not in year1:
            year1.append(top_year)
    year1.sort()
    movie_name_dict={i:[] for i in year1}
    for i in movies:
        top_year=i["year"]
        for j in movie_name_dict:
            if str(j)==str(top_year):
                movie_name_dict[j].append(i)
                with open("yearvise_movies.json","w") as imbd_data:
                    json.dump(movie_name_dict,imbd_data,indent=4)
    return movie_name_dict
group_by_year(movies_name)

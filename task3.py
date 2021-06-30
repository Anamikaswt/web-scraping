from bs4 import BeautifulSoup
import requests
from task1 import scrape_top_list
import json
movies_year=scrape_top_list()
year_of_movies={}
def group_by_decade(movies):
    year_list=[]
    for i in movies_year:
        year_list.append(i["year"])
        year_list.sort()
        list=[]
        for i in year_list:
            new=str(i)
            d_year=(new[0:2])+str(i%100-i%10)
            if i%100-i%10==0:
                d_year+="0"
            if d_year not in list:
                list.append(d_year)
        for i in list:
            d_cade_year=[]
            for j in movies:
                if j["year"]>int(i) and j["year"]<int(i)+10:
                    d_cade_year.append(j)
                    year_of_movies[i]=d_cade_year
    with open("task3.json","w") as task3:
        json.dump(year_of_movies,task3,indent=4)
    return year_of_movies
group_by_decade(movies_year)
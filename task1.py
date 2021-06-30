from bs4 import BeautifulSoup
import requests
import json

def scrape_top_list():
    imbd_api = "https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
    imbd_url = requests.get(imbd_api)
    data = imbd_url.json
    
    
    soup = BeautifulSoup(imbd_url.text ,"html.parser")
    div = soup.find("div",class_ ="lister")
    body = div.find("tbody",class_ = "lister-list")
    movie_detail = body.find_all("tr")
    movie_details=[]
    movie={"position":"","name":"","year":"","rating":"","main_url":""}
    j=1
    for i in movie_detail:
        name = i.find("td",class_ = "titleColumn").a.get_text() 
        year = i.find("td",class_="titleColumn").span.get_text()
        movies_year=year[1:5]
        movie_year=int(movies_year)
        rating = i.find("td",class_="ratingColumn imdbRating").strong.get_text()
        url=i.find("td",class_="titleColumn").a["href"]
        main_url="https://www.imdb.com"+url
        movie={"position":"","name":"","year":"","rating":"","main_url":""}
        movie["position"]=j
        movie["name"]=name
        movie["year"]=movie_year
        movie["rating"]=float(rating)
        movie["main_url"]=main_url
        movie_details.append(movie)
        j+=1
    with open("imbd_movie.json","w") as imbd_data:
        data1 = json.dump(movie_details,imbd_data,indent=4)
    return (movie_details)
print(scrape_top_list())


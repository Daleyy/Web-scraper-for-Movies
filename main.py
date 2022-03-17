import requests
from bs4 import BeautifulSoup


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, "html.parser")
movies_list = soup.find_all("h3", class_="title")

movies = [movie.getText() for movie in movies_list]
print(movies)

with open("movies.txt", "w") as movie_file:
    for movie in reversed(movies):
        movie_file.write(f"{movie}\n")

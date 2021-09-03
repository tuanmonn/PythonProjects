## note: since I couldn't scrape the website the course provided (due to dynamically rendered website) I used another website instead

from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.timeout.com/newyork/movies/best-movies-of-all-time")

empire_web = response.text

soup = BeautifulSoup(empire_web, "html.parser")

all_movies = soup.find_all(name= "h3", class_="_h3_cuogz_1")
movies_list = []

for movies in all_movies:
    title = movies.getText(strip=True)
    movies_list.append(title)

movies_list.pop(-1)             # remove the last line
print(movies_list)

with open("best 100 movies all time.txt", "w") as file:
    for n in movies_list:
        file.write(f"{n}\n")



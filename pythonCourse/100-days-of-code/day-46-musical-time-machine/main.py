from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date_input = input("Which year do you want to travel to? Type date in this format YYYY-MM-DD:")
year = date_input.split("-")[0]

# Spotify credientials

CLIENT_ID = ""                                      # fill in your client_id here
CLIENT_SECRET = ""                                  # fill in your client secret here
REDIRECT_URI = "https://example.com"
SCOPE = "playlist-modify-private"
# user_info = sp.current_user() --> get USER_ID
USER_ID = ""                                        # fill in your user id here

# authenticate
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI))

# create new playlist
playlist = sp.user_playlist_create(user=USER_ID,name=f"{date_input} Billboard 100", public=False, description="Python exercise")


# scrape billboard 100
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date_input}")

billboard_page = response.text

soup = BeautifulSoup(billboard_page, "html.parser")
songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

song_titles = []
song_uris = []

for n in songs:
    title = n.getText()
    song_titles.append(title)

# note: some songs still exist in Spotify but the Billboard's name is just too long or include (parenthesis)

for song in song_titles:
    result = sp.search(q=f"track:{song}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


# old solution: return wrong song names because I put "name" in the search query. Correct should be "track".
# also `finally` is not necessary

# for title in song_titles:
#     try:
#         result = sp.search(q=f"name:{title}",type="track")
#         song_uri = result["tracks"]["items"][0]["uri"]
#     except IndexError:
#         print("something is wrong")
#     finally:
#         song_uris.append(song_uri)


# add songs to playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


#---Lesson---

# hard: find the song uri using search api
# unexpected: couldn't find the song


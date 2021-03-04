import requests
from bs4 import BeautifulSoup
from env import SPOTIFY
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/"


def main():
    # Get date from User
    print("****** Songs Time Machine ******")
    date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD\n")

    # Get 100 top songs of given Date
    response = requests.get(url=f"{URL}{date}")
    response.raise_for_status()
    web_content = response.text

    # Scrape for song titles
    soup = BeautifulSoup(web_content, "html.parser")
    song_title_list = [text.text for text in soup.find_all(name="span",
                                    class_="chart-element__information__song text--truncate color--primary")]

    # connect to spotify
    scope = "playlist-modify-private"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY["client_id"],
                                                   client_secret=SPOTIFY["client_secret"],
                                                   redirect_uri=SPOTIFY["redirect_uri"],
                                                   scope=scope,
                                                   cache_path=".cache",
                                                   show_dialog=True))
    user_id = sp.current_user()["id"]

    # Search spotify for scraped songs' uri
    song_uri_list = []
    for title in song_title_list:
        try:
            song_uri = sp.search(title, limit=1, type="track")["tracks"]["items"][0]["uri"]
        except IndexError:
            song_uri = None

        song_uri_list.append(song_uri)

    # create a playlist
    playlist_id = sp.user_playlist_create(user=user_id,
                                          name=f"{date} Billboard 100",
                                          public=False)["id"]

    # Add songs to playlist
    sp.playlist_add_items(playlist_id=playlist_id, items=song_uri_list)


if __name__ == '__main__':
    main()

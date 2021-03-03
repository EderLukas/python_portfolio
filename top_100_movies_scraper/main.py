from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"


def main():
    # fetch webpage
    response = requests.get(URL)
    response.raise_for_status()
    content = response.text

    # soupify
    soup = BeautifulSoup(content, "html.parser")
    div_list = soup.find_all(name="div", class_="jsx-3821216435 listicle-item")

    # get movie title from alt tag of image
    movie_titles = [div.img.get("alt") for div in div_list]

    # Add rank to movie title
    for i in range(100, 0, -1):
        movie_titles[100-i] = f"{i}) " + movie_titles[100-i]

    # Write to file
    with open("movie_list.txt", mode="w") as file:
        for movie in movie_titles:
            file.write(f"{movie}\n")


if __name__ == '__main__':
    main()

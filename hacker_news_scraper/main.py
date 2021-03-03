from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

for article_tag in articles:
    text = soup.find(name="a", class_="storylink").text
    article_texts.append(text)
    link = soup.find(name="a", class_="storylink").get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

highest_number_index = article_upvotes.index(max(article_upvotes))
print(article_texts[highest_number_index])
print(article_links[highest_number_index])
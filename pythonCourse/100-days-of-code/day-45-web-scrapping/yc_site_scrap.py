from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
article_points = []

for article_tag in articles:
    story_text = article_tag.getText()
    article_texts.append(story_text)

    story_link = article_tag.get("href")
    article_links.append(story_link)


points = soup.find_all(class_="score")
for points in points:
    story_upvotes = int(points.getText().split()[0])        # get the points only
    article_points.append(story_upvotes)

index_max = article_points.index(max(article_points))

print(article_texts[index_max])
print(article_links[index_max])
print(article_points[index_max])




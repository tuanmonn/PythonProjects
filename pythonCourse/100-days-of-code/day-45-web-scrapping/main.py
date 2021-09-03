from bs4 import BeautifulSoup
import lxml


with open("website.html","r") as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser') ## sometimes we need "lxml"

## get hold of a single tag

print(soup.title)                           ## full title tag
print(soup.title.name)                      ## name of the tag
print(soup.title.string)                    ## actual string inside the title tag

## get hold of all the tags

all_anchor_tags = soup.find_all(name= "p")

for tag in all_anchor_tags:
    print(tag.getText())

heading = soup.find(name="h1", id="name")
print(heading)

headings = soup.select(".heading")
name = soup.select_one("#name")

print(headings)
print(name)
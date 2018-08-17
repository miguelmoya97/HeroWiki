from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

uClient = uReq('http://www.dota2.com/heroes/')
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

heroes = page_soup.select(".heroPickerIconLink")

hero_list = {}

# changes key values to current dota names
# i.e. rattletrap = clockwerk, etc...
for hero in heroes:
    hero_url = hero["href"]
    hero_list[hero["href"].split("/")[4]] = hero_url



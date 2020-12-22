import requests
import bs4
# install package - requests, lxml, bs4
res = requests.get("https://transcripts.fandom.com/wiki/Avengers:_Endgame")
soup = bs4.BeautifulSoup(res.text, "lxml")
soup.select("p" and "i")

for i in soup.select("p" and "i"):
    print(i.text)

#pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests

status_off = [505,504,404,403]

on_off_site = False
while not on_off_site:
    url = str(input("\nweb scrapping | SITE: "))
    try:
        status_site = requests.get(url)
    except:
        print("\nERRO TO CONECT")
    if status_site in status_off:
        print("\nERRO TO CONECT")
    else:
        # ARMAZENAR CODIGO DA PAGINA WEB>
        html_site = status_site.text
        soup = BeautifulSoup(status_site.content, "html.parser")
        tags_href = soup.find_all("a", href=True)
        for tag in tags_href:
            valor_href = tag["href"]
            print("\n",valor_href)
        on_off_site = True

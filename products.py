import requests
from bs4 import BeautifulSoup


def products(url):
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")

# Busco los primeros dos divs con esa clase
    divs = soup.find_all("div", class_="nav_dropdown-block")[:2]

# Itero para extraer de cada div, el texto que hace de título
    for div in divs:
        title = div.find("div", class_="text-weight-bold").text
        print(title)
        print("-")

    # Dentro extraigo todos los anchor del segundo div
        subtitles = div.find_all("a")

    # Itero extrayendo el texto y el link, en el caso de los links que empiezan con "/" les agrego la web
        for subtitle in subtitles:
            sub = subtitle.text
            link = subtitle["href"]
            if not link.startswith("https"):
                link = "https://reviewpro.shijigroup.com" + link

            print(sub)
            print(link)

        print('.')

products("https://reviewpro.shijigroup.com/")

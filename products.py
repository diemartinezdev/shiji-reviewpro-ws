import requests
from bs4 import BeautifulSoup
import json


def products(url):
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")

# Busco los primeros dos divs con esa clase
    divs = soup.find_all("div", class_="nav_dropdown-block")[:2]

# Creo una lista para almacenar los datos
    data = []

# Itero para extraer de cada div, el texto que hace de título
    for div in divs:
        title = div.find("div", class_="text-weight-bold").text

    # Dentro extraigo todos los anchor del segundo div
        subtitles = div.find_all("a")

    # Creo otra lista que estará contenida dentro de data
        subtitles_data = []

    # Itero extrayendo el texto y el link, en el caso de los links que empiezan con "/" les agrego la web
        for subtitle in subtitles:
            sub = subtitle.text
            link = subtitle["href"]
            if not link.startswith("https"):
                link = "https://reviewpro.shijigroup.com" + link
        # Indico qué elementos iran dentro de la sublista
            subtitle_data = {
                'Subtitle': sub,
                'Link': link
                }
            subtitles_data.append(subtitle_data)

    # Indico como irá estructurada la lista inicial
        title_data = {
            'Title': title,
            'Content': subtitles_data
        }

        data.append(title_data)

# 
    with open('products.json', 'w') as file:
        json.dump(data, file, indent=6)

print('Datos guardados en datos.json')


products("https://reviewpro.shijigroup.com/")

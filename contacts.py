import requests
from bs4 import BeautifulSoup


def contacts(url):
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")

# Busco los primeros dos divs con esa clase
    divs = soup.find_all("div", class_="contact_item")

# Itero extrayendo el h3 de cada div
    for div in divs:
        title = div.h3.text
        print(title)

    # Extraigo los anchor que comienzan con 'mailto:'
        links = div.find_all("a", href=lambda href: href and href.startswith("mailto:"))
        
    # Itero tomando los links, eliminando el 'mailto:' del principio y lo posterior a '.com'    
        for link in links:
            mail = link["href"].replace("mailto:", "")
            mail = mail.split(".com")[0] + ".com"
        
            print(mail)
            
        print('.')

contacts("https://reviewpro.shijigroup.com/team#contact")

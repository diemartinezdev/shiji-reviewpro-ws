import requests
from bs4 import BeautifulSoup
import json


def contacts(url):
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")

# Busco los primeros dos divs con esa clase
    divs = soup.find_all("div", class_="contact_item")

# Creo una lista para almacenar los datos
    data = []

# Itero extrayendo el h3 de cada div
    for div in divs:
        title = div.h3.text

    # Extraigo los anchor que comienzan con 'mailto:'
        links = div.find_all("a", href=lambda href: href and href.startswith("mailto:"))
        
        mails_data = []

    # Itero tomando los links, eliminando el 'mailto:' del principio y lo posterior a '.com'    
        for link in links:
            mail = link["href"].replace("mailto:", "")
            mail = mail.split(".com")[0] + ".com"
        
            mails_data = {
                'Mail': mail
            }
            mails_data.append(mails_data)
            
        title_data = {
            'Title': title,
            'MailsData': mails_data
        }

        data.append(title_data)    

# 
    with open('contacts.json', 'w') as file:
        json.dump(data, file, indent=6)

print('Datos guardados en datos.json')

contacts("https://reviewpro.shijigroup.com/team#contact")

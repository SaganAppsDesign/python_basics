import requests
from bs4 import BeautifulSoup

# Obtiene el contenido de la página web
url = 'https://www.as.com'
response = requests.get(url)
html = response.content
# Analiza el contenido con Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
# Encuentra el primer elemento con la clase "title"
print(soup.title)
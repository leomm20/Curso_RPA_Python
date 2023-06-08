import requests
from bs4 import BeautifulSoup as b
import warnings
from sys import exit

"""
hay que instalar pip install lxml
"""

url = 'https://www.clarin.com/politica/-nuevo-frente-cristina-kirchner-sergio-massa-presionan-presidente-acepte-' \
      'lista-unica_0_FHdRim8wxR.html'
# por ej. al ingresar a esta url, en pocos segundos nos llevará a otra que pedirá que nos suscribamos a clarín,
# por lo tanto, no podremos leer la misma. Pero con BeautifulSoup, podremos descargar su contenido

warnings.filterwarnings("ignore")
if requests.get(url, verify=False).status_code == 200:
    with open('extraccion_de_datos/clarin.html', 'w') as f:
        f.write(str(requests.get(url, verify=False).content))
    soup = b(requests.get(url, verify=False).content, 'lxml')
else:
    print('No se pudo acceder a la página')
    exit(-1)
# utilizar verify=False en caso de que haya políticas que controlen por ej. certificados autofirmados

print()
print(soup.find('span', attrs={'class': 'paywall-ico'}).text)
print()
print(soup.find('title').text)
print('*' * len(soup.find('title').text) + '\n')
print(soup.find('article').text.strip())

# for p in soup.findAll('p'):
#     print(p.text)

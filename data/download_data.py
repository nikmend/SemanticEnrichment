import urllib.request
import os

# URL del archivo
#url_cardelino = 
urls = ["https://raw.githubusercontent.com/mfaruqui/retrofitting/master/lexicons/wordnet-synonyms.txt", # WordNet synonims
        "https://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/SBW-vectors-300-min5.bin.gz", # Cardelino

]
# Carpeta de destino
folder = "data/external"

# Comprueba si la carpeta existe, si no, la crea
if not os.path.exists(folder):
    os.makedirs(folder)

for url in urls:
    name=url.split('/')[-1]
    filename = os.path.join(folder, name)
    urllib.request.urlretrieve(url, filename)
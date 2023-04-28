import pandas as pd
import requests

def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

URL = 'https://raw.githubusercontent.com/armandossrecife/teste/main/listaderepositorios.csv'
df_repositorios = pd.read_csv(filepath_or_buffer=URL, sep=';')
df_repositorios.info()

lista_url_repositorios = df_repositorios['Git Repository'].tolist()

lista_urls_validas = []
lista_urls_invalidas = []

for each in lista_url_repositorios:
    url_valida = check_url(each)
    print(f'Checa se a URL {each} é valida: {url_valida}')
    if url_valida:
        lista_urls_validas.append(each)
    else:
        lista_urls_invalidas.append(each)

print('Lista de URL inválidas: ')
for each in lista_urls_invalidas:
    print(each)
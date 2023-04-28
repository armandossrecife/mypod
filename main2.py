import pandas as pd
import requests

# Dada uma URL, checa se e valida
# retorna True se for valida
def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

# Ler arquivo .csv e carrega em um DataFrame
URL = 'https://raw.githubusercontent.com/armandossrecife/teste/main/listaderepositorios.csv'
df_repositorios = pd.read_csv(filepath_or_buffer=URL, sep=';')

print(f'Colunas do dataframe: {df_repositorios.columns}')

# Ler as url do dataframe e carrega em uma lista
lista_url_repositorios = df_repositorios['Git Repository'].tolist()
lista_urls_validas = []
lista_urls_invalidas = []

# Verifica se a URL e valida
for each in lista_url_repositorios:
    url_valida = check_url(each)
    print(f'Checa se a URL {each} é valida: {url_valida}')
    if url_valida:
        lista_urls_validas.append(each)
    else:
        lista_urls_invalidas.append(each)

if len(lista_urls_invalidas) > 0:
    print('Lista de URL inválidas: ')
    for each in lista_urls_invalidas:
        print(each)
else:
    print('Não há URL inválidas. ')
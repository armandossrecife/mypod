# Verifica se um sub-diretorio pertence a um diretorio
import os
import pandas as pd

def checa_sub_pasta(subdir, directory):
    if subdir in os.listdir(directory):
        print(f"{subdir} exists in {directory}")
    else:
        print(f"{subdir} doesn't exist in {directory}")

def is_path_in_dir(directory_path, file_path):
    rel_path = os.path.relpath(file_path, directory_path)
    return not rel_path.startswith('..')

def checa_file_path(directory_path, file_path):
    if is_path_in_dir(directory_path, file_path):
        print('File path is in directory')
    else:
        print('File path is not in directory')

def checa_sub_path(sub_path, repositorio):
    current_path = os.getcwd()
    abs_sub_path = current_path + '/' + repositorio + '/'+ sub_path
    print(f"Analisa {lista_src[i]} em {repositorio} - {os.path.exists(abs_sub_path)}")

# URL da lista de 31 repositorios do Darius Sas 
URL = 'https://raw.githubusercontent.com/armandossrecife/teste/main/l31repositoriossrc.csv'

# Carrega os dados dos repositorios em um DataFrame
df_repositorios = pd.read_csv(URL)

lista_repositorios = df_repositorios['repositorio'].tolist()
lista_src = df_repositorios['source_java'].tolist()

# Checa se os subdiretorios source existem nos repositorios
for i, repositorio in enumerate(lista_repositorios):
    checa_sub_path(sub_path=lista_src[i], repositorio=repositorio)
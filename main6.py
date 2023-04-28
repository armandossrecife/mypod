import os
import pandas as pd
import subprocess

# dado um diretorio, calcula a quantidade total de arquivos do diretorio
def get_total_arquivos(directory):
    result = subprocess.run(['sh', '-c', f"find {directory} -type f | wc -l"], stdout=subprocess.PIPE)
    total_arquivos = int(result.stdout.decode('utf-8').strip())
    return total_arquivos

# pega a lista de tags de um diretorio sob gerencia de configuracao do git
def get_lista_tags(directory):
    os.chdir(directory)
    lista_tags = subprocess.check_output(['git', 'tag'])
    lista_tags = lista_tags.decode().split()
    return lista_tags

# dado um diretorio sob gerencia de configuracao e uma tag, retorna 
# a quantidade de arquivos do diretorio setado para o branch da tag passada
def get_total_arquivos_branch(directory, my_tag):
    cmd = f"cd {directory} && git checkout {my_tag} && echo 'Total de arquivos: ' && find . -type f | wc -l"
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, text=True)
    total_arquivos = int(result.stdout.strip().split()[-1])
    return total_arquivos

# dado um diretorio sob gerencia de configuracao e uma tag, retorna uma lista contendo 
# os tipos de arquivos do diretorio
def get_types_of_files_branch(directory, my_tag):
    os.chdir(directory)  # change to the directory
    subprocess.run(['git', 'checkout', my_tag])  # run git checkout
    result = subprocess.run(['cloc', '.'], capture_output=True, text=True)  # run cloc and capture output
    return result.stdout


# URL da lista de 31 repositorios do Darius Sas 
URL = 'https://raw.githubusercontent.com/armandossrecife/teste/main/l31repositoriossrc.csv'

# Carrega os dados dos repositorios em um DataFrame
df_repositorios = pd.read_csv(URL)

lista_repositorios = df_repositorios['repositorio'].tolist()

# Calcula a quantidade de arquivos de cada repositorio
current_path = os.getcwd()
for repo in lista_repositorios:
    repo_path = current_path + '/' + repo
    print(f'Qtd de arquivos do {repo}: {get_total_arquivos(directory=repo_path)}')

# Lista as tags de cada repositorio
for repo in lista_repositorios:
    repo_path = current_path + '/' + repo
    print(f'Tags do {repo}: {get_lista_tags(directory=repo_path)}')

teste_cassandra = current_path + '/' + 'repositorio3'
print(get_types_of_files_branch(directory=teste_cassandra, my_tag='cassandra-3.11.11'))


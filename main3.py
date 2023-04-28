# Clona varios repositorios simultaneamente usando threads
import os
import threading
import datetime
import pandas as pd
from git import Repo

# Dado um comando de so, faz a execucao via python
def executa_comando_so(comando):
  try:
    os.system(comando)
    print(f'Comando: {comando} executado com sucesso!')
  except:
    print(f'Erro ao executar o comando {comando}')

# Dada uma url do git, salva no diretorio. Tambem adiciona o tempo de clonagem em uma lista de informacoes
def my_clone(git_url, repo_dir, lista):
  try:
    Repo.clone_from(git_url, repo_dir)
    tempo = datetime.datetime.now()
    print(f'Clonagem do repo {git_url} concluída com sucesso! -> instante: {tempo}')
    elemento = (repo_dir, tempo)
    lista.append(elemento)
  except Exception as ex:
    print(f"Erro ao clonar o repo: {git_url} - {str(ex)}")


def clona_repositorios(qtd_repositorios, lista_urls, lista_threads, lista_tempo_inicio, lista_tempo_conclusao):
  for i in range(qtd_repositorios):
    nome = 'repositorio'+str(i+1)
    tdi = threading.Thread(target=my_clone, args=(lista_urls[i], nome, lista_tempo_conclusao)) # Thread que inicia cada clonagem
    tdi.name = 'Thread-'+str(i+1) # nome do objeto thread recem criado
    inicio_thread = datetime.datetime.now() # instante que o clone inicia
    print(f"Thread {i+1} iniciada em {inicio_thread} - clonando {nome}:{lista_urls[i]}...")
    lista_threads.append(tdi) # insere a thread recem criada na lista de threads
    elemento = (nome, inicio_thread)
    lista_tempo_inicio.append(elemento)
    tdi.start() # inicia a thread
  for each in lista_threads:
    each.join()

def mostra_tempo_clonagens(lista_tempo_inicio, lista_tempo_conclusao):
  for t1 in lista_tempo_inicio:
    for t2 in lista_tempo_conclusao:
      if (t1[0]==t2[0]):
        print(f"Tempo de download do {t1[0]} é: {t2[1]-t1[1]} s")

# Ler arquivo .csv e carrega em um DataFrame
URL = 'https://raw.githubusercontent.com/armandossrecife/teste/main/listaderepositorios.csv'
df_repositorios = pd.read_csv(filepath_or_buffer=URL, sep=';')

# Ler as url do dataframe e carrega em uma lista
lista_url_repositorios = df_repositorios['Git Repository'].tolist()

lista_urls = lista_url_repositorios
lista_tempo_conclusao = []
lista_threads = [] # lista que armazena dos threads que vao fazer os clones
lista_tempo_inicio = [] # lista que vai guardar o instante de inicio de cada thread de clonagem

print("bloco de clonagem...")
tempo1 = datetime.datetime.now()
clona_repositorios(len(lista_urls), lista_urls, lista_threads, lista_tempo_inicio, lista_tempo_conclusao)  
tempo2 = datetime.datetime.now()

print("")
print(f"Tempo total de {len(lista_urls)} clonagens: {tempo2-tempo1}s")
print("")
print(f'Lista de tempos de inicio: {lista_tempo_inicio}')
print(f'Lista de tempos de conclusao: {lista_tempo_conclusao}')
print("")
mostra_tempo_clonagens(lista_tempo_inicio, lista_tempo_conclusao)
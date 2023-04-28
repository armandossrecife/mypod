import pandas as pd

URL = 'https://raw.githubusercontent.com/armandossrecife/teste/main/l31repositorios.csv'
URL2 = 'https://raw.githubusercontent.com/armandossrecife/teste/main/l31repositoriosurl.csv'

df_repositorios_src = pd.read_csv(URL)
#df_repositorios_src.info()
df_complemento = pd.read_csv(URL2)
#df_complemento.info()
#print(df_repositorios_src[['projeto', 'source']])
#print(df_complemento[['repositorio', 'url']])

df_complemento['nome'] = df_repositorios_src['projeto']
df_complemento['source_java'] = df_repositorios_src['source']

df_repositorios = df_complemento.copy()
df_repositorios = df_repositorios[['repositorio', 'url', 'nome', 'source_java']]
df_repositorios['source_java'] = df_repositorios['source_java'].str.replace('.','/')

print(df_repositorios)

df_repositorios.to_csv('l31repositoriossrc.csv', index=False)

#lista_src = df_repositorios_src['source'].tolist()

#for i, each in enumerate(lista_src):
#    print(f'{i}, {each}')
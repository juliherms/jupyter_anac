# %% [markdown]
# Realiza a leitura de um arquivo JSON dos dados públicos do governo

# %%
import pandas as pd

# pd.set_option('display.max_columns', None) # Exibe todas as colunas

caminho_do_arquivo = r"data\V_OCORRENCIA_AMPLA.json"
df = pd.read_json(caminho_do_arquivo, encoding='utf-8-sig')

# fltra as colunas que devme ser exibidas
colunas = ['Numero_da_Ocorrencia','Classificacao_da_Ocorrência','Data_da_Ocorrencia','Municipio','UF','Regiao','Nome_do_Fabricante']
df = df[colunas]

# reonmeia das colunas
df.rename(columns={'Classificacao_da_Ocorrência':'Classificacao_da_Ocorrencia'}, inplace=True)

# Converte a ocorrencia para datetime
df['Data_da_Ocorrencia'] = pd.to_datetime(df['Data_da_Ocorrencia'])
# df.head(3)
df.dtypes

from datetime import datetime
ano_atual = datetime.now().year
# Filtra o dataframe de acordo com o ano atual
df = df[df['Data_da_Ocorrencia'].dt.year == ano_atual]



# %% [markdown]
# Realiza a configuração e conexão com o banco de dados e faz a carga dos dados extraídos do JSON

# %%
from sqlalchemy import create_engine, Integer, String, Date, VARCHAR, text

# Parâmetros de conexão
dbname    = 'postgres'
user      = 'postgres'
password  = '12345'
host      = 'localhost'
port      = '5432'

# Connection string
connection_string = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'

# Create connection wiht sqlalchemy
engine = create_engine(connection_string)

table_name = "anac_sql"

# Atualiza os dados do ano atual
cursor = engine.connect()
delete = text(f'DELETE FROM public.{table_name} WHERE EXTRACT(YEAR FROM "Data_da_Ocorrencia") = {ano_atual}')
cursor.execute(delete)
cursor.commit()

df.to_sql(table_name, engine, index=False, if_exists='append', dtype={
    'Numero_da_Ocorrencia': Integer,
    'Classificacao_da_Ocorrencia': VARCHAR(50),
    'Data_da_Ocorrencia': Date
})
# replace = sobrescreve toda a tabela
# append = adiciona os dados ao final da tabela

engine.dispose()
cursor.close()




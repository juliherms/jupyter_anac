# %% [markdown]
# Realiza a leitura de um arquivo JSON dos dados públicos do governo

# %%
import pandas as pd
import psycopg2

# pd.set_option('display.max_columns', None) # Exibe todas as colunas

caminho_do_arquivo = r"data\V_OCORRENCIA_AMPLA.json"
df = pd.read_json(caminho_do_arquivo, encoding='utf-8-sig')

# fltra as colunas que devme ser exibidas
colunas = ['Numero_da_Ocorrencia','Classificacao_da_Ocorrência','Data_da_Ocorrencia','Municipio','UF','Regiao','Nome_do_Fabricante']
df = df[colunas]

# reonmeia das colunas
df.rename(columns={'Classificacao_da_Ocorrência':'Classificacao_da_Ocorrencia'}, inplace=True)

# df.head(3)


# %% [markdown]
# Realiza a configuração e conexão com o banco de dados e faz a carga dos dados extraídos do JSON

# %%
# Parâmetros de conexão
dbname    = 'dados'
user      = 'postgres'
password  = '12345'
host      = 'localhost'
port      = '5432'

conn = psycopg2.connect(dbname=dbname,
                        user=user,
                        password=password,
                        host=host,
                        port=port)
cur = conn.cursor()
cur.execute('delete from anac')

for indice,coluna in df.iterrows():
    cur.execute("""
                insert into anac (
                    numero_da_ocorrencia,
                    classificacao_da_ocorrencia,
                    data_da_ocorrencia,
                    municipio,
                    uf,
                    regiao,
                    nome_do_fabricante
                ) VALUES (%s,%s,%s,%s,%s,%s,%s) 
                """,(
                    coluna["Numero_da_Ocorrencia"],
                    coluna["Classificacao_da_Ocorrencia"],
                    coluna["Data_da_Ocorrencia"],
                    coluna["Municipio"],
                    coluna["UF"],
                    coluna["Regiao"],
                    coluna["Nome_do_Fabricante"],
                    )
                )

conn.commit()

# %%
# fecha o cursor e a conexão
cur.close()
conn.close()



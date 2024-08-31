# %%
import pandas as pd
import matplotlib.pyplot as plt

caminho_do_arquivo = r"data\pix_202408261208.csv"
dados = pd.read_csv(caminho_do_arquivo)

dados['data'] = pd.to_datetime(dados['data'])
dados['ano'] = dados['data'].dt.year

dados_filtrados = dados[dados['id_pix_status'] == 2]

df_valor_pix = dados_filtrados.groupby('ano')[['valor']].sum().sort_values('ano')



# %% [markdown]
# Gera gráfico do volume total de pix por ano

# %%
df_valor_pix.plot(kind='barh', figsize=(14,10), color='gray');
plt.legend()

plt.savefig('grafico_evolucao_pix.png', format='png')

# Exibir o gráfico
plt.show()


# %% [markdown]
# Gera gráfico do valor médio de pix por ano

# %%
df_valor_pix_medio = dados_filtrados.groupby('ano')[['valor']].mean().sort_values('ano')

df_valor_pix_medio.plot(kind='line', figsize=(14,10), color='gray');
plt.legend()

plt.savefig('grafico_valor_medio_pix.png', format='png')

# Exibir o gráfico
plt.show()

# %%




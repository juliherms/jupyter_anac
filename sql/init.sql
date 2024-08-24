CREATE TABLE IF NOT EXISTS Anac (
    numero_da_ocorrencia int,
    classificacao_da_ocorrencia varchar(50),
    data_da_ocorrencia date,
    municipio varchar(50),
    uf varchar(30),
    regiao varchar(30),
    nome_do_fabricante varchar(100)
)

insert into anac (
    numero_da_ocorrencia,
    classificacao_da_ocorrencia,
    data_da_ocorrencia,
    municipio,
    uf,
    regiao,
    nome_do_fabricante
) VALUES (
    1,
    'Acidente',
    '2022-01-01',
    'São Paulo',
    'SP',
    'Sudeste',
    'Jatinho 444')
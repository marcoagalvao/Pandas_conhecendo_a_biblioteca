import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('aluguel.csv', sep=';')

#Conhecendo o dataset
print(dados.head(10))

print(dados.shape)

print(dados.columns)

print(dados.info())

print(dados.describe())

print(dados['Tipo'].unique())

#-----------------------------------------------------------------------------#
#Analise exploratória

#Valor médio dos imóveis por tipo
print(dados['Valor'].mean())

print(dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor'))

df_preco_tipo = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

df_preco_tipo.plot(kind='barh', figsize=(14, 10), color='purple')
#plt.show()

#Removendo os imóveis comerciais
imoveis_comerciais = ['Conjunto Comercial/Sala', 
                      'Prédio Inteiro', 'Loja/Salão', 
                      'Galpão/Depósito/Armazém', 
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']

#Plotando novamente o valor médio dos imóveis por tipo, agora sem os imóveis comerciais
df = dados.query('@imoveis_comerciais not in Tipo')
df_preco_tipo = df.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
df_preco_tipo.plot(kind='barh', figsize=(14, 10), color='purple')
#plt.show()

#Distribuição percentual dos tipos de imóveis
print(df.Tipo.value_counts(normalize=True))

df_percentual_tipo = df.Tipo.value_counts(normalize=True).sort_values().to_frame()
df_percentual_tipo.plot(kind='bar', figsize=(14, 10), color='green', xlabel='Tipos', ylabel='Percentual')
#plt.show()

#Filtrando apenas os apartamentos
df = df.query('Tipo == "Apartamento"')

#-------------------------------------------------------------------------------#
#Desafio - Qual a média de quartos dos apartamentos? E a quantidade de bairros únicos? E quais os 5 bairros com os maiores valores médios de aluguel?
print('Média de quartos:', df.Quartos.mean())

print('Quantidade de bairros únicos:', df['Bairro'].nunique())

df_preco_bairro = df.groupby('Bairro')[['Valor']].mean().sort_values('Valor', ascending=False)

print('Os 5 bairros com os maiores valores médios de aluguel:')
print(df_preco_bairro.head())

df_preco_bairro.head(5).sort_values('Valor', ascending=True).plot(kind='barh', figsize=(14, 10), color='orange', xlabel='Valor', ylabel='Bairros')
#plt.show()
#--------------------------------------------------------------------------------#
#Tratando e filtrando os dados

#Tratando os dados faltantes
print(df.isnull().sum())
df = df.fillna(0)
print(df.isnull().sum())

#Removendo os registros com valores zero nas colunas 'Valor' e 'Condominio'
registros_a_remover = df.query('Valor == 0 | Condominio == 0').index
df.drop(registros_a_remover, axis=0, inplace=True)
#Removendo a coluna 'Tipo'
df.drop('Tipo', axis=1, inplace=True)

#Filtrando os apartamentos com 1 quarto e valor menor que R$ 1.200,00
selecao_final = (df['Valor'] < 1200) & (df['Quartos'] == 1)
df_1 = df[selecao_final]
#Filtrando os apartamentos com 2 ou mais quartos, valor menor que R$ 3.000,00 e área maior que 70m²
selecao = (df['Quartos'] >= 2) & (df['Valor'] < 3000) & (df['Area'] > 70)
df_2 = df[selecao]

#-------------------------------------------------------------------------------#
#Salvando os dataframes em arquivos csv
df.to_csv('dados_apartamentos.csv', sep=';', index=False)
apartamento = pd.read_csv('dados_apartamentos.csv', sep=';')
print(apartamento.head())

df_1.to_csv('dados_apartamentos_1_quarto.csv', sep=';', index=False)
df_2.to_csv('dados_apartamentos_2_quartos.csv', sep=';', index=False)
#-------------------------------------------------------------------------------#
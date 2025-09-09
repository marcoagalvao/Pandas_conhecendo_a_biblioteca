import pandas as pd

dados = pd.read_csv('aluguel.csv', sep=';')

#Criando novas colunas numericas
dados['Valor_por_mes'] = dados['Valor'] + dados['Condominio']

dados['Valor_por_ano'] = dados['Valor_por_mes'] * 12 + dados['IPTU']

print(dados.head())

#Criando novas colunas categóricas
dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro'] + ' com ' + dados['Quartos'].astype(str) + ' quarto(s)' + ' e ' + dados['Vagas'].astype(str) + ' vaga(s)'

print(dados.head())

#Criando novas colunas boleanas
dados['Possui_suite'] = dados['Suites'].apply(lambda x: 'Sim' if x >= 1 else 'Não')

print(dados.head())

#Salvando o novo dataframe em um arquivo csv
dados.to_csv('aluguel_completo.csv', sep=';', index=False)
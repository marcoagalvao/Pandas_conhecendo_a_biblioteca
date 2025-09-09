#Desafio prático - Alunos de curso superior
import pandas as pd

alunos = pd.read_csv('alunos.csv')

print(alunos.head(10))

print(alunos.isnull().sum())

alunos['Notas'].fillna(0)

registros_a_remover = alunos.query('Nome == "Alice" | Nome == "Carlos"').index

alunos.drop(registros_a_remover, axis=0, inplace=True)

alunos = alunos.replace(7.0, 8.0)

alunos['Pontos Extras'] = alunos['Notas'] * 0.4

alunos['Notas Finais'] = alunos['Notas'] + alunos['Pontos Extras']

alunos['Aprovados_final'] = alunos['Notas Finais'].apply(lambda x: True if x >= 6 else False)

alunos_aprovados = alunos.query('Aprovados_final == True')

aprovados_com_ponto_extra = alunos.query('Aprovado == False & Aprovados_final == True')

print('Alunos aprovados com pontos extras:')
print(aprovados_com_ponto_extra)

print(alunos_aprovados)

alunos_aprovados.to_csv('alunos_aprovados.csv', index=False)

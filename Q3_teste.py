import pandas as pd
def exportar_csv(pessoas: list, nome_arquivo: str): 
  dados = {'id': [1, 2, 3, 4, 5], 'Nomes': ["Marcos", "Ana", "Carlos", "Julia", "Pedro"], "idade": [28, 24, 30, 22, 27], "gostos": [['Musica', 'Futebol'], ['Leitura', 'Cinema'], ['Viagem'], ['Dança', 'Esporte'], ['Tecnologia', 'Culinária']]}
  df = pd.DataFrame(dados)
  df.to_csv('pessoas.csv', index=False)

import pandas as pd
df = pd.read_csv('ClassicDisco.csv')

#print(df.to_string()) imprimi planilha toda

#print(df.head()) imprimi cabeçalho 5 linhas, entanto colocando o número dentro o parenteses vazio

#print(df.tail(15)) imprimi rodapé 5 linhas, entanto colocando o número dentro o parenteses vazio

#print(df[10:25])

print(df.shape)
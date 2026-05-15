import pandas as pd

# Lê o CSV tratando a coluna 'data' como data real
df = pd.read_csv("extrato_exemplo.csv", parse_dates=["data"])

'''# Visão geral
print("--- INFORMAÇÕES GERAIS ---")
df.info()

print()
print("--- ESTATÍSTICAS ---")
print(df.describe().round(2))

print()
print("--- PRIMEIRAS TRANSAÇÕES ---")
print(df.head())

print()
print("--- ÚLTIMAS TRANSAÇÕES ---")
print(df.tail())'''

# Filtrar apenas despesas (valores negativos)
print()
despesas = df[df["valor"] < 0]

print("--- DESPESAS DO MÊS ---")
print(despesas)
print()

print("--- TOTAL DE DESPESAS ---")
total_despesas = despesas["valor"].sum()
print(total_despesas)

print()
receitas = df[df["valor"] > 0]

# Filtrar entrada de receita
print("--- TOTAL DE RECEITAS ---")
print(receitas)
total_receitas = receitas["valor"].sum()
print(total_receitas)

# Saldo 
print()
print("--- SALDO DO MÊS ---")
saldo = total_receitas + total_despesas
print(saldo)
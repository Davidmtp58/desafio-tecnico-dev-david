import pandas as pd

# Lê o CSV tratando a coluna 'data' como data real
df = pd.read_csv("extrato_exemplo.csv", parse_dates=["data"])

# Palavras chaves para categorização

categorias_map = {
    "IFOOD": "Alimentação",
    "SUPERMERCADO": "Alimentação",
    "LANCHONETE": "Alimentação",
    "UBER": "Transporte",
    "POSTO COMBUSTIVEL": "Transporte",
    "NETFLIX": "Streaming",
    "SPOTIFY": "Streaming",
    "AMAZON PRIME": "Streaming",
    "FARMACIA": "Saúde",
    "SALARIO": "Salário",
    "PIX RECEBIDA": "Entrada Diversa",
}

print(categorias_map)

def descobrir_categoria(descricao):
    for palavra_chave, categoria in categorias_map.items():
        if palavra_chave in descricao:
            return categoria
    return "Outros"


df["categoria"] = df["descricao"].apply(descobrir_categoria)

print(df)


"""
# Visão geral
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
print(df.tail())

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
print(saldo)"""

print()
print("--- TOTAL POR CATEGORIA ---")
total_por_categoria = df.groupby("categoria")["valor"].sum()
print(total_por_categoria)

print()
print("--- TOP 3 CATEGORIAS DE GASTO ---")
top3 = total_por_categoria[total_por_categoria < 0].sort_values().head(3)
print(top3)
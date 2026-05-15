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

def descobrir_categoria(descricao):
    for palavra_chave, categoria in categorias_map.items():
        if palavra_chave in descricao:
            return categoria
    return "Outros"


df["categoria"] = df["descricao"].apply(descobrir_categoria)

print(df)

print()
print("--- TOTAL POR CATEGORIA ---")
total_por_categoria = df.groupby("categoria")["valor"].sum().round(2)
print(total_por_categoria)

print()
print("--- TOP 3 CATEGORIAS DE GASTO ---")
top3 = total_por_categoria[total_por_categoria < 0].sort_values().head(3)
print(top3)
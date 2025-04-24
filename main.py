import pandas as pd

# Carrega a planilha
df = pd.read_excel("clientes.xlsx")

# Percorre cada linha da tabela
for index, row in df.iterrows():
    nome = row["Nome"]
    email = row["Email"]

    # Mensagem personalizada
    mensagem = f"""
    Olá, {nome}!

    Esta é uma mensagem automática gerada pelo script em Python.
    Estamos testando a automação com base numa planilha Excel 😄

    Até breve!

    -- Manuela
    """

    print(f"Mensagem para {email}")
    print(mensagem)
    print("-" * 60)

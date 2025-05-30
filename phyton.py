import pandas as pd

# URL do Google Sheets (formato CSV)
google_sheets_url = "https://docs.google.com/spreadsheets/d/e/THIAGOVRS_projeto/pub?output=csv"

# Carregar os dados
try:
    df = pd.read_csv(google_sheets_url)
    print("Dados carregados com sucesso!")
except Exception as e:
    print(f"Erro ao carregar dados: {e}")
    exit()

# Exibir informações iniciais
df.info()

# Remover espaços extras dos nomes das colunas
df.columns = df.columns.str.strip()

# Preencher valores nulos com valores padrão ou remover linhas nulas
df.fillna({
    "Nome": "Desconhecido",
    "Idade": df["Idade"].median(),  # Preencher com a mediana
    "Salário": 0.0
}, inplace=True)

# Corrigir tipos de dados
df["Idade"] = pd.to_numeric(df["Idade"], errors='coerce').fillna(0).astype(int)
df["Salário"] = pd.to_numeric(df["Salário"], errors='coerce').fillna(0.0)

# Remover duplicatas
df.drop_duplicates(inplace=True)

# Padronizar formatação de texto
df["Nome"] = df["Nome"].str.title()

# Salvar no formato Excel
output_file = "dados_tratados.xlsx"
df.to_excel(output_file, index=False)
print(f"Dados tratados e salvos em {output_file}

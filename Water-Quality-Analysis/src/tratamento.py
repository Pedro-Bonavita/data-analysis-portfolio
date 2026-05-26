import pandas as pd
import os

# Determina os caminhos dinamicamente baseados na localização deste script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_PATH = os.path.join(BASE_DIR, 'data', 'raw', 'Copy of WaterQuality.csv')
OUTPUT_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'WaterQuality_Clean.csv')

# Carregar dataset
try:
    df = pd.read_csv(INPUT_PATH)
except FileNotFoundError:
    # Fallback caso o script seja executado de uma estrutura diferente
    df = pd.read_csv('Copy of WaterQuality.csv')

# Verificar a quantidade de nulos por coluna
print("Valores ausentes por coluna:")
print(df.isnull().sum())

# Tratar nulos
df['pH'] = df['pH'].fillna(df['pH'].median())
df['Land_Use'] = df['Land_Use'].fillna('Unknown')

# Separar Latitude e Longitude usando str.split
df[['Latitude','Longitude']] = df['Station_Location'].str.split(',', expand=True)

# Deletando a coluna antiga
df = df.drop(columns=['Station_Location'])

# Convertendo tipos
df['Latitude'] = df['Latitude'].astype(float)
df['Longitude'] = df['Longitude'].astype(float)
df['Date'] = pd.to_datetime(df['Date'])
df['Land_Use'] = df['Land_Use'].astype("string")
df['Pollution_Event'] = df['Pollution_Event'].astype(bool)

# Arrumando a Ordem das Colunas (Esta etapa faltava no script original!)
nova_ordem = [
    'Station_ID',
    'Latitude',
    'Longitude',
    'Date',
    'pH',
    'Dissolved_Oxygen',
    'Turbidity',
    'Nitrogen',
    'Phosphorus',
    'Rainfall',
    'Pollution_Event',
    'Fish_Population',
    'Land_Use'
]

# Aplicando a mesma ordenação do Jupyter Notebook
df = df[nova_ordem]

# Visualizar informações finais no terminal
print("\nTipos finais de dados:")
print(df.dtypes)
print("\nEstrutura final dos dados (head):")
print(df.head())

# Exportando resultado para a pasta correspondente
try:
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"\nArquivo exportado com sucesso para: {OUTPUT_PATH}")
except FileNotFoundError:
    df.to_csv('WaterQuality_Clean.csv', index=False)
    print("\nArquivo exportado com sucesso para o diretório local.")
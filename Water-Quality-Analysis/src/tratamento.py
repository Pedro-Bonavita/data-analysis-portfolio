import pandas as pd

# Carregar dataset

df = pd.read_csv('Copy of WaterQuality.csv')

# Verificar a quantidade de nulos por coluna
print ("Valores ausentes por coluna:")
print(df.isnull().sum())

df['pH'] = df['pH'].fillna(df['pH'].median())

df['Land_Use'] = df['Land_Use'].fillna('Unknown')

# Separar Latitude e Longitude usando str.split
df[['Latitude','Longitude']] = df['Station_Location'].str.split(',',expand=True)

# Deletando a coluna antiga
df = df.drop(columns=['Station_Location'])

# Visualizar
df.head()

print(df.dtypes)

# Convertendo Lati e Long para Float
df['Latitude'] = df['Latitude'].astype(float)
df['Longitude'] = df['Longitude'].astype(float)

# Convertendo Date para Datetime
df['Date'] = pd.to_datetime(df['Date'])

# Convertendo Land_Use para String
df['Land_Use'] = df['Land_Use'].astype("string")

# Convertendo Polution_Event para boolean
df['Pollution_Event'] = df['Pollution_Event'].astype(bool)

# Convertendo Lati e Long para Float
df['Latitude'] = df['Latitude'].astype(float)
df['Longitude'] = df['Longitude'].astype(float)

# Convertendo Date para Datetime
df['Date'] = pd.to_datetime(df['Date'])

# Convertendo Land_Use para String
df['Land_Use'] = df['Land_Use'].astype("string")

# Convertendo Polution_Event para boolean
df['Pollution_Event'] = df['Pollution_Event'].astype(bool)

# Exportando resultado

df.to_csv('WaterQuality_Clean.csv',index=False)
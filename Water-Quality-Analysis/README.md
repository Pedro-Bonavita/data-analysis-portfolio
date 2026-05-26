# 🌊 Pipeline de Engenharia & Análise de Qualidade da Água

Este projeto faz parte do meu portfólio profissional de dados e apresenta um pipeline completo de **Engenharia e Limpeza de Dados (Data Wrangling)** com foco em monitoramento ambiental e preparação para Business Intelligence.

O objetivo é processar dados brutos sobre a qualidade da água coletados em várias estações de monitoramento, tratar valores nulos e inconsistências geográficas usando **Python (Pandas)** e **SQL**, preparando os dados para a ingestão e desenvolvimento de um dashboard interativo no **Power BI**.

---

## 📊 Visão Geral do Problema de Negócio

No setor de gestão ambiental e saneamento, monitorar a qualidade da água é crucial para a preservação de ecossistemas aquáticos e para a saúde pública. Este dataset contém medições críticas como:
*   **pH:** Acidez da água (fator crucial para a vida aquática).
*   **Dissolved Oxygen (Oxigênio Dissolvido):** Quantidade de oxigênio disponível para a fauna marinha.
*   **Turbidity (Turbidez):** Medida de clareza da água.
*   **Nutrientes (Nitrogênio e Fósforo):** Indicadores de poluição agrícola ou industrial.
*   **Rainfall (Precipitação) & Land Use (Uso do Solo):** Fatores ambientais e geográficos.
*   **Pollution Event (Evento de Poluição):** Registro se houve algum incidente de contaminação.
*   **Fish Population (População de Peixes):** Indicador biológico da saúde da água.

---

## 🛠️ Arquitetura e Estrutura do Projeto

O projeto é estruturado de forma limpa e modular:

```text
Water-Quality-Analysis/
├── data/                  # Conjuntos de dados brutos e tratados (ex: CSVs)
├── notebooks/             # Playgrounds e exploração visual (Jupyter Notebooks)
│   └── limpeza_dados.ipynb
├── sql/                   # Scripts e consultas de banco de dados
│   └── consulta.sql
├── src/                   # Código-fonte do pipeline de tratamento em Python
│   └── tratamento.py
├── requirements.txt       # Dependências de bibliotecas Python
└── README.md              # Documentação detalhada do projeto
```

---

## ⚙️ Detalhamento do Pipeline de Dados

### 1. Limpeza e Engenharia de Atributos com Python (`src/tratamento.py`)
Utilizando a biblioteca **Pandas**, o script de produção realiza as seguintes etapas automatizadas para garantir a qualidade dos dados:
*   **Tratamento de Valores Ausentes:**
    *   Imputação de valores nulos na coluna `pH` através da **mediana** (`median()`) para mitigar o impacto de distorções causadas por outliers.
    *   Preenchimento de valores ausentes na coluna qualitativa `Land_Use` com o termo genérico `'Unknown'`.
*   **Engenharia de Recursos Geográficos (Geospatial Parsing):**
    *   Divisão da string de localização combinada `Station_Location` em duas colunas numéricas independentes: `Latitude` e `Longitude` usando `str.split(',')`.
    *   Remoção da coluna original desnecessária para otimização de memória.
*   **Tipagem Estrita de Dados (Data Type Casting):**
    *   Conversão das coordenadas geográficas para `float`.
    *   Conversão da coluna temporal `Date` para tipo `datetime` padronizado.
    *   Ajuste da coluna qualitativa `Land_Use` para tipo `string` explícito.
    *   Conversão de `Pollution_Event` para valores lógicos Booleanos (`bool`).
*   **Exportação:** Salvamento do conjunto higienizado final como `WaterQuality_Clean.csv`.

```python
# Trecho de exemplo do tratamento de geolocalização e tipos
df[['Latitude','Longitude']] = df['Station_Location'].str.split(',', expand=True)
df = df.drop(columns=['Station_Location'])
df['Latitude'] = df['Latitude'].astype(float)
df['Longitude'] = df['Longitude'].astype(float)
df['Date'] = pd.to_datetime(df['Date'])
```

### 2. Otimização de Consultas para Ingestão (`sql/consulta.sql`)
O arquivo SQL simula um cenário empresarial realista de **restrição de privilégios** (onde o analista de dados não possui permissão de escrita/criação de *Views* ou tabelas no banco de dados). 

Para contornar isso e alimentar diretamente o Power BI com dados otimizados, desenvolvi uma consulta personalizada (`SELECT`) que:
*   Realiza o split de latitude e longitude via manipulação de string em SQL (`substring_index`).
*   Extrai ano, mês e dia da coluna de data nativa.
*   Traduz dinamicamente o nome dos meses para o português (`Jan`, `Fev`, `Mar`...) usando a função `elt(month(date), ...)` e `CASE WHEN`, enriquecendo a navegação temporal local no painel.

```sql
SELECT 
    station_id AS "id da estação",
    SUBSTRING_INDEX(station_location, ',', 1) AS latitude,
    SUBSTRING_INDEX(station_location, ',', -1) AS longitude,
    date,
    ELT(MONTH(date), 'jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez') AS "mês",
    pH, Dissolved_Oxygen, Turbidity, Nitrogen, Phosphorus, rainfall, land_use, pollution_event, fish_population
FROM waterquality;
```

---

## 📈 Próxima Etapa: Visualização de Dados (Power BI)

A etapa final do ciclo consiste na conexão das fontes tratadas ao **Power BI** para elaboração de um dashboard executivo e tático. O relatório interativo focará em:
1.  **Monitoramento de Métricas Críticas (KPIs):** Painéis com médias de oxigênio dissolvido e pH aceitável por estação.
2.  **Análise Espacial (Mapas):** Plotagem das coordenadas tratadas (`Latitude` e `Longitude`) mapeando a distribuição da turbidez e surtos de poluição no território.
3.  **Correlação de Impacto (Estudos):** Gráficos de dispersão e análise de tendências conectando a presença de poluentes (Nitrogênio/Fósforo) com a saúde biológica local (População de Peixes) e o Uso do Solo correspondente.

---

## 🚀 Tecnologias Utilizadas

*   **Linguagem Principal:** Python 3
*   **Manipulação de Dados:** Pandas
*   **Ambiente de Desenvolvimento:** Jupyter Notebook / VS Code
*   **Banco de Dados:** MySQL (Consultas Analíticas Avançadas)
*   **Business Intelligence:** Power BI (Em desenvolvimento)

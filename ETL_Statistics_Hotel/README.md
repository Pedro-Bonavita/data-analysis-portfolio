<!-- ============================================================ -->
<!--                  🇧🇷  VERSÃO EM PORTUGUÊS                   -->
<!-- ============================================================ -->

<div align="center">

# 🏨 ETL & Análise Estatística — Dataset Hoteleiro

**Pipeline de tratamento de dados e análise estatística aplicados ao setor hoteleiro.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-orange?logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

</div>

---

## ✨ Funcionalidades

- **Ingestão de dados brutos** — Leitura de arquivo CSV com dados hoteleiros desestruturados (`hotel_dataset_messy.csv`)
- **Tratamento de Outliers** — Detecção e substituição de idades impossíveis (> 100 anos) pela mediana; valores negativos em `Total_Charges` convertidos para `NaN`
- **Transformação e Enriquecimento de Dados:**
  - Tradução de colunas do inglês para o português via dicionário de mapeamento
  - Normalização de nomes de hóspedes (Title Case)
  - Conversão de colunas de data para o tipo `datetime`
  - Criação da coluna derivada `Tempo_Estadia` (Check-out − Check-in em dias)
  - Criação da coluna `Classe_Satisfacao` via `pd.cut` (Baixa / Média / Alta)
  - Tipagem ordinal de `Tipo_Quarto` com `CategoricalDtype` (Standard < Deluxe < Suite)
  - Arredondamento de `Total_Gastos` para 2 casas decimais
  - Remoção de duplicatas ocultas
- **Carga (Load)** — Exportação do DataFrame tratado para um novo arquivo CSV (`hotel_dataset_clean`)
- **Análise Estatística Descritiva** — Geração de estatísticas gerais (numéricas e categóricas) com `describe()`
- **Visualização de Dados** — Gráfico de dispersão (Scatter Plot) correlacionando Idade vs. Total de Gastos, segmentado por Tipo de Quarto

---

## 🛠️ Tecnologias Utilizadas

| Ferramenta / Biblioteca | Finalidade |
|---|---|
| **Python 3.x** | Linguagem base do projeto |
| **Jupyter Notebook** | Ambiente de desenvolvimento interativo |
| **Pandas** | Manipulação, limpeza e transformação do DataFrame |
| **NumPy** | Operações numéricas e tratamento de valores nulos |
| **Matplotlib** | Engine de renderização dos gráficos |
| **Seaborn** | Visualizações estatísticas estilizadas |
| **Google Colab** | Plataforma de execução utilizada durante o desenvolvimento |

---

## 📦 Pré-requisitos e Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/Pedro-Bonavita/data-analysis-portfolio.git
cd data-analysis-portfolio/ETL_Statistics_Hotel
```

### 2. Criar e ativar um ambiente virtual (recomendado)

```bash
# Criar ambiente
python -m venv venv

# Ativar — Windows
venv\Scripts\activate

# Ativar — Linux/macOS
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### 4. Dataset

O notebook espera um arquivo chamado `hotel_dataset_messy.csv` no mesmo diretório (ou, ao rodar no Google Colab, no caminho `/content/hotel_dataset_messy.csv`).  
Certifique-se de disponibilizar o dataset antes de executar o notebook.

> **Colunas esperadas no CSV de entrada:**
>
> | Coluna | Tipo | Descrição |
> |---|---|---|
> | `Guest_Name` | string | Nome do hóspede |
> | `Age` | int | Idade |
> | `Room_Type` | string | Tipo de quarto (Standard / Deluxe / Suite) |
> | `CheckIn_Date` | string (YYYY-MM-DD) | Data de check-in |
> | `CheckOut_Date` | string (YYYY-MM-DD) | Data de check-out |
> | `Booking_Channel` | string | Canal de reserva |
> | `Total_Charges` | float | Valor total cobrado |
> | `Satisfaction_Score` | float | Pontuação de satisfação (1–5) |

---

## 🏃 Como Executar

### Opção A — Jupyter Notebook (local)

```bash
jupyter notebook ETL_Estatystics_Hotel.ipynb
```

Execute as células **em ordem sequencial** (de cima para baixo).

### Opção B — Google Colab

1. Faça o upload do notebook e do arquivo `hotel_dataset_messy.csv` para o Colab.
2. Execute todas as células com `Runtime > Run all`.

---

## 🛣️ Estrutura do Pipeline

O notebook está organizado em **cinco estágios**:

```
[1] EXTRACT  ──► Leitura do CSV bruto
        │
[2] TRANSFORM ─► Tratamento de outliers (Age, Total_Charges)
        │         Tradução de colunas
        │         Classificação de variáveis categóricas
        │         Normalização de nomes e datas
        │         Engenharia de features (Tempo_Estadia, Classe_Satisfacao)
        │         Limpeza de duplicatas
        │
[3] LOAD     ──► Exportação para hotel_dataset_clean.csv
        │
[4] ANALYZE  ──► Estatísticas descritivas (numéricas e categóricas)
        │
[5] VISUALIZE ─► Scatter Plot: Idade vs. Total de Gastos por Tipo de Quarto
```

---

## 👤 Autor

**Pedro Bonavita**  
[![GitHub](https://img.shields.io/badge/GitHub-@Pedro-Bonavita-181717?logo=github)](https://github.com/Pedro-Bonavita)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Conectar-0A66C2?logo=linkedin)](https://linkedin.com/in/pedro-bonavita)

---

---

<!-- ============================================================ -->
<!--                  🇺🇸  ENGLISH VERSION                        -->
<!-- ============================================================ -->

<div align="center">

# 🏨 ETL & Statistical Analysis — Hotel Dataset

**Data cleaning pipeline and statistical analysis applied to the hospitality sector.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-orange?logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

</div>

---

## ✨ Features

- **Raw data ingestion** — Reads a messy CSV file with unstructured hotel data (`hotel_dataset_messy.csv`)
- **Outlier Treatment** — Detects and replaces impossible ages (> 100) with the median; negative `Total_Charges` values are converted to `NaN`
- **Data Transformation & Enrichment:**
  - Column renaming from English to Portuguese via a mapping dictionary
  - Guest name normalization (Title Case)
  - Date columns converted to `datetime` type
  - Derived column `Tempo_Estadia` (Stay Duration = Check-out − Check-in in days)
  - Satisfaction classification column `Classe_Satisfacao` via `pd.cut` (Low / Medium / High)
  - Ordinal typing of `Tipo_Quarto` using `CategoricalDtype` (Standard < Deluxe < Suite)
  - Rounding of `Total_Gastos` to 2 decimal places
  - Duplicate record removal
- **Load** — Exports the cleaned DataFrame to a new CSV file (`hotel_dataset_clean`)
- **Descriptive Statistical Analysis** — Generates numeric and categorical statistics using `describe()`
- **Data Visualization** — Scatter plot correlating Age vs. Total Charges, segmented by Room Type

---

## 🛠️ Tech Stack

| Tool / Library | Purpose |
|---|---|
| **Python 3.x** | Core programming language |
| **Jupyter Notebook** | Interactive development environment |
| **Pandas** | DataFrame manipulation, cleaning and transformation |
| **NumPy** | Numerical operations and null value handling |
| **Matplotlib** | Chart rendering engine |
| **Seaborn** | Styled statistical visualizations |
| **Google Colab** | Execution platform used during development |

---

## 📦 Prerequisites & Installation

### 1. Clone the repository

```bash
git clone https://github.com/Pedro-Bonavita/data-analysis-portfolio.git
cd data-analysis-portfolio/ETL_Statistics_Hotel
```

### 2. Create and activate a virtual environment (recommended)

```bash
# Create
python -m venv venv

# Activate — Windows
venv\Scripts\activate

# Activate — Linux/macOS
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### 4. Dataset

The notebook expects a file named `hotel_dataset_messy.csv` in the same directory (or at `/content/hotel_dataset_messy.csv` when running on Google Colab).  
Make sure the dataset is available before executing the notebook.

> **Expected input CSV columns:**
>
> | Column | Type | Description |
> |---|---|---|
> | `Guest_Name` | string | Guest name |
> | `Age` | int | Age |
> | `Room_Type` | string | Room type (Standard / Deluxe / Suite) |
> | `CheckIn_Date` | string (YYYY-MM-DD) | Check-in date |
> | `CheckOut_Date` | string (YYYY-MM-DD) | Check-out date |
> | `Booking_Channel` | string | Booking channel |
> | `Total_Charges` | float | Total amount charged |
> | `Satisfaction_Score` | float | Satisfaction score (1–5) |

---

## 🏃 How to Run

### Option A — Jupyter Notebook (local)

```bash
jupyter notebook ETL_Estatystics_Hotel.ipynb
```

Run all cells **in sequential order** (top to bottom).

### Option B — Google Colab

1. Upload the notebook and the `hotel_dataset_messy.csv` file to Colab.
2. Run all cells via `Runtime > Run all`.

---

## 🛣️ Pipeline Structure

The notebook is organized into **five stages**:

```
[1] EXTRACT   ──► Read raw CSV
        │
[2] TRANSFORM ──► Outlier treatment (Age, Total_Charges)
        │          Column renaming
        │          Categorical variable classification
        │          Name & date normalization
        │          Feature engineering (Stay Duration, Satisfaction Class)
        │          Duplicate removal
        │
[3] LOAD      ──► Export to hotel_dataset_clean.csv
        │
[4] ANALYZE   ──► Descriptive statistics (numeric & categorical)
        │
[5] VISUALIZE ──► Scatter Plot: Age vs. Total Charges by Room Type
```

---

## 👤 Author

**Pedro Bonavita**  
[![GitHub](https://img.shields.io/badge/GitHub-@Pedro-Bonavita-181717?logo=github)](https://github.com/Pedro-Bonavita)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin)](https://linkedin.com/in/pedro-bonavita)

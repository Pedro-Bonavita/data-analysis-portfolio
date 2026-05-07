# GenTech HR Data Analysis & Interactive Dashboard

## 📊 Project Overview
This project was developed as the final assessment for the Data Analytics module at the GenTech bootcamp. The objective was to act as an HR Data Analyst to clean, process, and analyze employee data, providing actionable insights through an interactive dashboard.

The project covers the entire data lifecycle: from raw data cleaning and transformation to advanced data visualization.

## 🛠️ Key Features & Methodology

### 1. Advanced Data Cleaning (Data Governance Mindset)
Unlike standard cleaning, this project implements a **traceable data pipeline**:
* **Audit Columns:** Created `clean_` prefix columns to store transformed data while preserving the original raw inputs, ensuring 100% data lineage.
* **Quality Flags:** Implemented a `flag_Performance_Rating` column to identify records where missing values were imputed using department averages.
* **Text Standardization:** Used `TRIM` and `PROPER` functions to eliminate inconsistencies in naming and department strings.

### 2. Data Enrichment
* **Relational Mapping:** Integrated the `Employee Data` sheet with `Training Programme Data` using `XLOOKUP` (PROCX) to calculate total investment per employee.
* **Feature Engineering:** Developed a `Performance_Category` classifier based on nested logic to segment staff into *High Performers*, *Satisfactory*, and *Needs Improvement*.

### 3. Business Intelligence & Visualization (The "Tool-Fit" Challenge)
While modern BI tools like **Power BI** or **Tableau** are the industry standard for high-level data storytelling and complex modeling, this project was intentionally developed within **Google Sheets** to meet specific assessment requirements and demonstrate versatility.

Recognizing the UI/UX limitations of spreadsheet-based dashboards, I implemented several advanced workarounds to deliver a professional-grade interface:
* **Dynamic Slicers (Control Filters):** Bridged the gap between static tables and interactive reports, allowing real-time data exploration by Department.
* **Layout Optimization:** Conducted a complete UI cleanup by removing gridlines, headers, and unnecessary chart elements (buttons/legends) to mimic a standalone application environment.
* **Semantic Formatting:** Applied conditional formatting to performance metrics to enable "at-a-glance" executive decision-making, compensating for the lack of native advanced KPIs.
* **Bonus Analytics:** Expanded the scope to include *Average Salary by Job Role* and *Company Tenure Analysis*, proving that a structured data foundation can overcome tool-specific constraints.

## 📁 Repository Structure
* `/data/raw`: Original inconsistent dataset.
* `/data/processed`: Final cleaned and enriched Excel/Google Sheets file.
* `/images`: Screenshots of the interactive dashboard.
* `README.md`: Project documentation.

## 🚀 Tools Used
* **Google Sheets / MS Excel**
* **Pivot Tables & Pivot Charts**
* **Logic Functions:** IF, IFS, XLOOKUP, AVERAGEIFS, ROUND.
* **Data Visualization:** Slicers, Conditional Formatting, Bar/Column Charts.

---
*Developed by Pedro Bonavita as part of a Data Science specialization.*
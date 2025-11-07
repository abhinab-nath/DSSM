<div align="center">

  <h1>🧠 Data Science Project — Phishing Websites Dataset</h1>

  <br />
  <div>
    <img src="https://img.shields.io/badge/-Python-black?style=for-the-badge&logo=python&logoColor=white&color=3776AB" alt="Python" />
    <img src="https://img.shields.io/badge/-Pandas-black?style=for-the-badge&logo=pandas&logoColor=white&color=150458" alt="Pandas" />
    <img src="https://img.shields.io/badge/-Matplotlib-black?style=for-the-badge&logo=plotly&logoColor=white&color=11557C" alt="Matplotlib" />
    <img src="https://img.shields.io/badge/-Seaborn-black?style=for-the-badge&logoColor=white&color=01B0F0" alt="Seaborn" />
    <img src="https://img.shields.io/badge/-YData_Profiling-black?style=for-the-badge&logo=data&logoColor=white&color=FF6B6B" alt="YData Profiling" />
    <img src="https://img.shields.io/badge/-UCI_Dataset-black?style=for-the-badge&logo=databricks&logoColor=white&color=13ADC7" alt="UCI Dataset" />
  </div>
  <br />
  <p>Performing Data Analysis and Visualization on the UCI Phishing Websites Dataset</p>
  
</div>

---

## 📍 Overview  
This project explores and analyzes the **[Phishing Websites Dataset](https://archive.ics.uci.edu/ml/datasets/Phishing+Websites)** from the **UCI Machine Learning Repository**.  
The workflow includes **data conversion**, **data description**, **visualization**, and an **automated profiling report** — to better understand the dataset’s features and structure.

---

## ⚙️ Steps Performed  

### 🧾 1. Data Conversion  
- The original dataset was in **ARFF format**.  
- Converted it to **CSV** using `convert_into_csv.py`.  
- **Output:** `Phishing_Dataset.csv`  

---

### 📊 2. Data Description  
- Generated a comprehensive summary report using `description.py`.  
- **Output:** `Dataset_Description.txt`  
- Report includes:  
  - Dataset shape and columns  
  - Data types  
  - Statistical summary  
  - Missing values  
  - Class distribution (`Result` column)  
  - Correlation matrix  

---

### 📈 3. Data Visualization  
- Visualized dataset using `visualization.py`.  
- Plots generated:  
  - Histograms — feature distributions  
  - Boxplots — outlier detection  
  - Countplots — categorical features  
  - Correlation heatmap  
  - Pairplots (for smaller numeric feature sets)  
- **All plots saved in:** `results/plots/`  

---

### 🧮 4. Automated Profiling Report  
- Used **YData Profiling** (formerly *pandas-profiling*) via `ydata_profiling_report.py`.  
- Created an interactive HTML report showing:  
  - Data overview  
  - Correlations  
  - Missing values  
  - Feature insights  
- **Output:** `results/Phishing_Dataset.html`  

---

## 🧰 Tools & Libraries  
- **Python 3.x**  
- **pandas** — data handling  
- **matplotlib**, **seaborn** — visualizations  
- **ydata-profiling** — automated EDA report  
- **arff** — file conversion  

---

## 💻 How to Run  

### 1️⃣ Clone this repository  
```bash
git clone https://github.com/abhinab-nath/DSSM.git
cd DSSM
```

### 2️⃣ Install dependencies
```bash
pip install pandas matplotlib seaborn ydata-profiling scipy
```

### 3️⃣ Run the scripts (in order)
```bash
python scripts/convert_into_csv.py
python scripts/description.py
python scripts/visualization.py
python scripts/ydata_profiling_report.py
```

### 4️⃣ Check the outputs

- 📁 `data/Phishing_Dataset.csv` — converted dataset

- 🧾 `results/Dataset_Description.txt` — text summary report

- 📊 `results/plots/` — generated plots

- 🌐 `results/Phishing_Dataset.html` — interactive profiling report

---

## 📂 Folder Structure
```
DSSM/
│
├── scripts/
│   ├── convert_into_csv.py
│   ├── description.py
│   ├── visualization.py
│   └── ydata_profiling_report.py
│
├── results/
│   ├── plots/
│   ├── Dataset_Description.txt
│   └── Phishing_Dataset.html
│
└── data/
    ├── Training Dataset.arff
    └── Phishing_Dataset.csv
```

---

## ✅ Summary

Through this project, we successfully:

✔ Converted and cleaned the dataset

✔ Generated descriptive and statistical summaries

✔ Visualized relationships and patterns

✔ Produced an automated profiling report

---

#### 👨‍💻 Author: [Abhinab Nath](https://github.com/abhinab-nath/)

<img src="https://img.shields.io/badge/-MIT_License-black?style=for-the-badge&logo=bookstack&logoColor=white&color=019B8F" alt="MIT License" />

# 🧠 Data Science Project — Phishing Websites Dataset  

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

## 👨‍💻 Author

Abhinab Nath

📎 **[GitHub Profile](https://github.com/abhinab-nath)**

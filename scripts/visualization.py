# ==============================
# Data Visualization (boxplot, histogram, heatmap)
# ==============================

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# nicer style
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# <1> Load Dataset
df = pd.read_csv('/phishing+websites/data/Phishing_Dataset.csv')

# Identify column types
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = df.select_dtypes(exclude=['int64', 'float64']).columns

print("==> Loaded dataset:", df.shape)
print("Numeric columns:", list(numeric_cols))
print("Categorical columns:", list(categorical_cols))


# <2> Create output folders
output_dir = "outputs/plots"
os.makedirs(output_dir, exist_ok=True)


# <3> Distribution of Numeric Features
for col in numeric_cols:
    plt.figure()
    sns.histplot(df[col], kde=True, bins=30)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/{col}_hist.png')
    plt.close()


# <4> Boxplots for Outlier Detection
for col in numeric_cols:
    plt.figure()
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.xlabel(col)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/{col}_boxplot.png')
    plt.close()


# <5> Countplots for Categorical Features
for col in categorical_cols:
    plt.figure()
    sns.countplot(x=df[col])
    plt.title(f'Count Plot of {col}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/{col}_countplot.png')
    plt.close()


# <6> Correlation Heatmap (Numeric)
if len(numeric_cols) > 1:
    plt.figure(figsize=(12, 8))
    corr = df[numeric_cols].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/correlation_heatmap.png')
    plt.close()


# <7> Pairplot (Scatter Matrix)
# Keep it only for small number of numeric columns
if 2 <= len(numeric_cols) <= 6:
    pairplot_fig = sns.pairplot(df[numeric_cols])
    pairplot_fig.fig.suptitle('Pairplot of Numeric Features', y=1.02)
    pairplot_fig.savefig(f'{output_dir}/pairplot.png')
    plt.close()


# <8> Feature vs Target Plots
# Replace 'target_column' with your target column name (if any)
target_col = 'URL_Length'  # CHANGE THIS

if target_col in df.columns:
    # Numeric vs Target
    for col in numeric_cols:
        if col != target_col:
            plt.figure()
            sns.boxplot(x=df[target_col], y=df[col])
            plt.title(f'{col} vs {target_col}')
            plt.tight_layout()
            plt.savefig(f'{output_dir}/{col}_vs_{target_col}_box.png')
            plt.close()

    # Categorical vs Target
    for col in categorical_cols:
        if col != target_col:
            plt.figure()
            sns.countplot(x=col, hue=target_col, data=df)
            plt.title(f'{col} vs {target_col}')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(f'{output_dir}/{col}_vs_{target_col}_count.png')
            plt.close()

print(f"\n==> All plots saved to: {output_dir} <==")

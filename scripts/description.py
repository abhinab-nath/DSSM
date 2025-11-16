import pandas as pd

# Load the cleaned dataset
df = pd.read_csv('/phishing+websites/data/Phishing_Dataset.csv')

# Prepare a text report
with open('Dataset_Description.txt', 'w', encoding='utf-8') as f:
    f.write("=== DATASET SUMMARY REPORT ===\n\n")

    # Basic info
    f.write(" Shape of Dataset:\n")
    f.write(str(df.shape) + "\n\n")

    f.write(" Column Names:\n")
    f.write(", ".join(df.columns) + "\n\n")

    # Data types
    f.write(" Data Types:\n")
    f.write(str(df.dtypes) + "\n\n")

    # Basic statistics
    f.write(" Statistical Summary:\n")
    f.write(str(df.describe(include='all')) + "\n\n")

    # Missing values
    f.write(" Missing Values per Column:\n")
    f.write(str(df.isnull().sum()) + "\n\n")

    # Class distribution
    f.write(" Class Distribution (Result column):\n")
    f.write(str(df['Result'].value_counts()) + "\n\n")

    # Display first five rows
    f.write(" First Five Rows (head function):\n")
    f.write(str(df.head()) + "\n\n")

    # Correlation matrix
    f.write(" Correlation Matrix (top 10 shown):\n")
    f.write(str(df.corr().head(10)) + "\n\n")

print(" 'Dataset_Description.txt' file created successfully!")

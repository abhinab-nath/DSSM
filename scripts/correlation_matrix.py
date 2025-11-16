import pandas as pd

# Load dataset
df = pd.read_csv('/phishing+websites/data/Phishing_Dataset.csv')

# Select only numeric columns
numeric_cols = df.select_dtypes(include=['int64', 'float64'])

# Compute correlation matrix
corr_matrix = numeric_cols.corr()

# Print correlation matrix in console
print("=== Correlation Matrix ===")
print(corr_matrix)

# Save to CSV
corr_matrix.to_csv('/phishing+websites/results/correlation_matrix.csv', index=True)

print("\nCorrelation matrix saved as 'correlation_matrix.csv'")

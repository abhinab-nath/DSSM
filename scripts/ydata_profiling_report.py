import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('/phishing+websites/data/Phishing_Dataset.csv')
print(df)

profile = ProfileReport(df)
profile.to_file(output_file='/phishing+websites/results/Phishing_Dataset.html')
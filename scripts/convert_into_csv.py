# convert_arff_to_csv.py

import arff
import pandas as pd

# Load ARFF file
data = arff.load(open('/phishing+websites/data/Training Dataset.arff', 'r'))

# Convert to DataFrame
df = pd.DataFrame(data['data'], columns=[attr[0] for attr in data['attributes']])

# Save to CSV
df.to_csv('/phishing+websites/data/Phishing_Dataset.csv', index=False)

print("Conversion complete: Phishing_Dataset.csv created!")
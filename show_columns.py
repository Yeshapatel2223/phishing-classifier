import pandas as pd

# CSV file ka sahi path
csv_path = r"upload_data_to_db\phising_08012020_120000.csv"

# CSV read karo
df = pd.read_csv(csv_path)

# Columns list print karo
print("\nColumns in CSV:")
print(df.columns.tolist())

import pandas as pd

# Read an Excel file
df = pd.read_excel("rit.xlsx")

print(df)

print(df['Student Name'])

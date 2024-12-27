import pandas as pd

# Read Excel file
df = pd.read_excel("rit.xlsx")

# Filter data
filtered_data = df[df['Sl No'] > 50]

# Save to a new Excel file
filtered_data.to_excel("filtered_students.xlsx", index=False)

print("Filtered data saved successfully!")

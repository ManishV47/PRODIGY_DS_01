import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
data = pd.read_csv('data.csv')  # Assuming 'data.csv' is in the same directory as your Python script

# Display the first few rows of the dataset to ensure it's read correctly
print(data.head())

# Assuming 'ages' is a column in your dataset containing continuous data
DistributioOf60th = data['1960']  # Replace 'ages' with the actual column name containing your continuous data
print(DistributioOf60th)

# Creating the histogram
plt.figure(figsize=(8, 6))
plt.hist(DistributioOf60th, bins=30, color='purple', edgecolor='black')
plt.xlabel('World Development Indicators for 1960')
plt.ylabel('Frequency/Count')
plt.title('Distribution of 1960')
plt.grid(axis='y')

# Display the plot
plt.tight_layout()
plt.show()

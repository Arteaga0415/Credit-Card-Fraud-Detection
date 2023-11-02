import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv("creditcard_2023.csv")

# Calculate the correlation matrix for numerical columns
correlation_matrix = df.corr()

# Get the correlation of each feature with the "Class" column
correlation_with_class = correlation_matrix["Class"].sort_values(ascending=False)

# Plot a heatmap of the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, cmap="coolwarm", annot=False)
plt.title("Correlation Matrix Heatmap")

# Plot a bar graph of the correlation with the "Class" column
plt.figure(figsize=(12, 8))
sns.barplot(x=correlation_with_class.index, y=correlation_with_class.values, palette="coolwarm")
plt.title("Correlation with Class")
plt.xticks(rotation=45)
plt.ylabel("Correlation Value")
plt.show()

# Print the correlations with the "Class" column
print("Correlation with Class:\n", correlation_with_class)

# Read the CSV file into a Pandas Dataframe
df = pd.read_csv("creditcard_2023.csv")

# Identify the duplicate rows
duplicate_rows = df[df.duplicated("V1")]
# Create a new DataFrame with only the duplicate rows
duplicate_df = df.loc[duplicate_rows.index]
# Write the duplicate DataFrame to an Excel file
duplicate_df.to_excel("duplicate_rows.xlsx", index=False)

# Drop any rows that are completely duplicated
df = df.drop_duplicates("V1")

# Print the total number of transactions
print("Total number of transactions:", df.shape[0])

# Print the number of fraudulent transactions
print("Number of fraudulent transactions:", df[df['Class'] == 1].shape[0])

# Print the number of good transactions
print("Number of good transactions:", df[df['Class'] == 0].shape[0])

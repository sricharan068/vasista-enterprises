import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('diabetes.csv')
print(df.head())

# Inspect Data Structure and Check Missing Values
df.info()
print(df.isnull().sum())

#Statistical Summary and Visualizing Outliers
print(df.describe())

fig, axs = plt.subplots(len(df.columns), 1, figsize=(7, 18), dpi=95)
for i, col in enumerate(df.columns):
    axs[i].boxplot(df[col], vert=False)
    axs[i].set_ylabel(col)
plt.tight_layout()
plt.show()


# Remove Outliers Using the Interquartile Range (IQR) Method
q1, q3 = np.percentile(df['Insulin'], [25, 75])
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
clean_df = df[(df['Insulin'] >= lower) & (df['Insulin'] <= upper)]
print(clean_df)

#Correlation Analysis
corr = df.corr()
plt.figure(dpi=130)
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm')
plt.show()

print(corr['Outcome'].sort_values(ascending=False))

#Visualize Target Variable Distribution
plt.pie(df['Outcome'].value_counts(), labels=[
        'Diabetes', 'Not Diabetes'], autopct='%.f%%', shadow=True)
plt.title('Outcome Proportionality')
plt.show()

#Separate Features and Target Variable
X = df.drop(columns=['Outcome'])
y = df['Outcome']

#Feature Scaling: Normalization and Standardizatio
#Min-Max Scaling
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)
print("Min-Max Scaling:\n",X_normalized[:5])

#Standardization:
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)
print("StandardScaler: \n",X_standardized[:5])

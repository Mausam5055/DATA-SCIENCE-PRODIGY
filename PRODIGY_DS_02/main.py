# Titanic Data Cleaning, EDA, and Save All Plots as PNG
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# ---- Load Data ----
df = pd.read_csv('train.csv')  # Ensure 'train.csv' is in your working directory

# ---- Create Output Directory for PNGs ----
output_dir = 'png_outputs'
os.makedirs(output_dir, exist_ok=True)

# ---- Data Inspection ----
print(df.head())
print(df.info())
print(df.describe(include='all'))

# ---- Data Cleaning ----
print(df.isnull().sum())  # Check missing values

df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop('Cabin', axis=1, inplace=True)

df['Sex'] = df['Sex'].astype('category')
df['Embarked'] = df['Embarked'].astype('category')
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# ---- Univariate Analysis ----
plt.figure()
sns.countplot(x='Survived', data=df)
plt.title('Survival Count')
plt.savefig(os.path.join(output_dir, 'survival_count.png'))
plt.close()

plt.figure()
sns.histplot(df['Age'], bins=20, kde=True)
plt.title('Age Distribution')
plt.savefig(os.path.join(output_dir, 'age_distribution.png'))
plt.close()

# ---- Bivariate Analysis ----
plt.figure()
sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Survival Rate by Sex')
plt.savefig(os.path.join(output_dir, 'survival_by_sex.png'))
plt.close()

plt.figure()
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Survival Rate by Passenger Class')
plt.savefig(os.path.join(output_dir, 'survival_by_pclass.png'))
plt.close()

plt.figure()
sns.violinplot(x='Survived', y='Age', data=df)
plt.title('Age vs Survival')
plt.savefig(os.path.join(output_dir, 'age_vs_survival.png'))
plt.close()

# ---- Correlation Heatmap ----
plt.figure()
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.savefig(os.path.join(output_dir, 'correlation_heatmap.png'))
plt.close()

print("\nAll plots are saved as PNG files in the 'png_outputs' folder.")

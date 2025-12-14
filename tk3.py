import pandas as pd
df = pd.read_csv(r"C:\Users\ADMIN\OneDrive\문서\internship\Task1\store_cities.csv")
df.head()
df.shape
df.describe()
df.info()
df.isnull().sum()
df['storetype_id'] = df['storetype_id'].fillna('Unknown')
df['city_id'] = df['city_id'].fillna('Unknown')
df['store_size'] = df['store_size'].fillna(df['store_size'].mean())
print("Duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()
import matplotlib.pyplot as plt
df['city_id'].value_counts().plot(kind='bar', figsize=(10,5))
plt.title("Number of Stores per City")
plt.show()

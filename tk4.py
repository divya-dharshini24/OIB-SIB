import pandas as pd
import pandas as pd

df=pd.read_csv(r"C:\Users\ADMIN\OneDrive\문서\internship\Task1\sales\sales.csv",nrows=500)
print(df.head())

df.head()
df.shape
df.describe()
df.info()
df.isnull().sum()
df['price'] = df['price'].fillna(df['price'].mean())
df['promo_bin_1'] = df['promo_bin_1'].fillna('No Promo')
df['price'] = df['price'].fillna(df['price'].mean())       
df['promo_bin_1'] = df['promo_bin_1'].fillna('No Promo')  
print("Duplicate rows:", df.duplicated().sum())
print(df.describe(include='all'))
print(df.isnull().sum())
import matplotlib.pyplot as plt
df['date'] = pd.to_datetime(df['date'])
daily_sales = df.groupby('date')['sales'].sum()
plt.figure(figsize=(12,5))
plt.plot(daily_sales.index, daily_sales.values)
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()

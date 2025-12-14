import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\ADMIN\OneDrive\문서\internship\Task1\AirPassengers.csv")
print(df.head())
print("Shape:", df.shape)
print(df.describe())
print(df.info())
print("Missing values:\n", df.isnull().sum())

if df['#Passengers'].isnull().sum() > 0:
    df['#Passengers'] = df['#Passengers'].fillna(df['#Passengers'].mean())


print("Duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()

df['Month'] = pd.to_datetime(df['Month'])
df.set_index('Month', inplace=True)


plt.figure(figsize=(12,6))
plt.plot(df.index, df['#Passengers'], marker='o', color='skyblue')
plt.title("Monthly Air Passengers")
plt.xlabel("Month")
plt.ylabel("Number of Passengers")
plt.grid(True)
plt.show()


plt.figure(figsize=(8,5))
plt.hist(df['#Passengers'], bins=20, color='lightgreen', edgecolor='black')
plt.title("Distribution of Air Passengers")
plt.xlabel("Number of Passengers")
plt.ylabel("Frequency")
plt.show()

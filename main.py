import pandas as pd

df = pd.read_csv(r"C:\Users\rajas\Desktop\Foodpanda Project\Foodpanda-Resturants-Data-Analysis\Foodpanda Analysis Dataset.csv"
)  

print(df.head())

print(df.describe())
print(df.info())
print(df.tail())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.columns)

print(df["rating"].dtype)

#Average rating of all orders
def average_rating():
  print(df["rating"].mean())

average_rating()

#Top rating in all orders
def top_rating():
  top = df.sort_values(by ="rating", ascending=False)
  print(top.head(50))

top_rating()

#Most Common City
def most_common_city():
    common_city = df["city"].value_counts()
    print(common_city)

most_common_city()

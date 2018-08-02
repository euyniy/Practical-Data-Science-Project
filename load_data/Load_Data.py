import pandas as pd

df = pd.DataFrame.from_csv("movie_data", sep = "\t")

print(len(df))
df = pd.read_pickle("movies.pkl")


print(len(df))
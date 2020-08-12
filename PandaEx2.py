import pandas as pd
reviews = pd.read_csv('ign.csv')
print(reviews.head())
print(reviews.shape)
print(reviews.iloc[0:5, :])
print(reviews.iloc[:5, :])
reviews = reviews.iloc[:, 1:]
print(reviews.head())
print(reviews.loc[0:5, :])
print(reviews.index)
some_reviews = reviews.iloc[10:20, ]
print(some_reviews.head())
print(reviews.loc[:5, "score"])
print(reviews.loc[:5,["score", "release_year"]])
reviews.to_html("reviews.html")
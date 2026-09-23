import pandas as pd
dataset=pd.read_csv("C:\\Users\\sushm\\OneDrive\\Desktop\\Pandas\\netflix_titles.csv")
print(dataset)
# show the datasets structure
dataset.info()
# to show the first 10 rows
print("The first 10 rows are\n",dataset.head(10))
# to count movie and tv shows
print(dataset["type"].value_counts())
movies=dataset[dataset["type"]=="Movie"]
print("The moivie are\n",movies)
# the movies which are released after 2021
recent_movies=dataset[dataset["release_year"] > 2021]
print("Release year after 2021 is:\n",recent_movies)
US_movies=dataset[dataset["country"]=="United States"]
print("The movies released by united states are:\n",US_movies)
dataset=dataset.drop(["description"],axis=1)
print("Drop the null values or descriptions\n",dataset)
dataset.to_csv("cleaned_netflix_data.csv",index=False)


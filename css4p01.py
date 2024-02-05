# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

file_path = "C:/Users/Muano Odelle/CSS_Project_Option1_IMDB_Data/movie_dataset.csv"  
movies_df = pd.read_csv(file_path)

movies_df.head()

df = pd.DataFrame(movies_df)

print(df)

df_clean = df.dropna()

print(df_clean.head())

df_clean.to_csv('cleaned_dataset.csv', index=False)

# Highest rated movie

highest_rated_movie = df.loc[df['Rating'].idxmax()]

print("Highest Rated Movie:")

print(highest_rated_movie)

# Average revenue of the dataset

average_revenue = df['Revenue (Millions)'].mean()

print("Average Revenue of All Movies:", average_revenue)

# Average revenue of movies between 2015 to 2017

filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

average_revenue_2015_to_2017 = filtered_df['Revenue (Millions)'].mean()

print("Average Revenue of Movies from 2015 to 2017:", average_revenue_2015_to_2017)


# The number of movies released in the year 2016

filtered_df = df[(df['Year']== 2016)]

movies_2016_count = (df['Year'] == 2016).sum()

print("Number of Movies Released in 2016:", movies_2016_count)


# Number of movies directed by christopher Nolan

nolan_movies_count = (df['Director'] == 'Christopher Nolan').sum()

print("Number of Movies Directed by Christopher Nolan:", nolan_movies_count)

                
# Number of movies with the rating of atleast 8.0

high_rated_movies_count = (df['Rating'] >= 8.0).sum()

print("Number of Movies with a Rating of at Least 8.0:", high_rated_movies_count)

# Median rating of movies directed by Christopher Nolan

nolan_movies = df[df['Director'] == 'Christopher Nolan']

median_rating_nolan_movies = nolan_movies['Rating'].median()

print("Median Rating of Movies Directed by Christopher Nolan:", median_rating_nolan_movies)


# Year with the highest average rating

average_rating_by_year = df.groupby('Year')['Rating'].mean()

year_highest_avg_rating = average_rating_by_year.idxmax()

highest_avg_rating = average_rating_by_year.max()

print("Year with the Highest Average Rating:", year_highest_avg_rating)

print("Highest Average Rating:", highest_avg_rating)


# The percentage increase in number of movies made between 2006 and 2016

movies_2006 = (df['Year'] == 2006).sum()

movies_2016 = (df['Year'] == 2016).sum()

percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100

print("Percentage Increase in Number of Movies (2006 to 2016):", percentage_increase)


# Find the most common actor 

from collections import Counter

all_actors = df['Actors'].str.split(', ').explode().str.strip()

actors_counter = Counter(all_actors)

most_common_actor, most_common_count = actors_counter.most_common(1)[0]

print("Most Common Actor in All Movies:", most_common_actor)

print("Number of Appearances:", most_common_count)



# Counting the number of unique genres in the dataset

df['Genres'] = df['Genre'].str.split(', ')

df_expanded = df.explode('Genres')

print(df_expanded[['Title', 'Genres']])


# Correlation of the numerical features

numerical_features = df[['Rating', 'Revenue (Millions)','Runtime (Minutes)', 'Votes', 'Metascore', 'Rank']]

correlation_matrix = numerical_features.corr()

print("Correlation Matrix:")

print(correlation_matrix)





        
                  














import pandas as pd

#movie_df = pd.read_csv('movies\movies.csv')

#ratings1_df = pd.read_csv('movies\ratings1.csv')

dates_df = pd.read_csv('movies\dates.csv')

dates_df['date']=pd.to_datetime(dates_df['date'])

dates_df['year']=dates_df['date'].dt.year

print(dates_df['year'].value_counts())
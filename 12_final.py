import pandas as pd
import re 

def get_year_release(arg):
    #находим все слова по шаблону "(DDDD)"
    candidates = re.findall(r'\(\d{4}\)', arg) 
    # проверяем число вхождений
    if len(candidates) > 0:
        #если число вхождений больше 0,
	#очищаем строку от знаков "(" и ")"
        year = candidates[0].replace('(', '')
        year = year.replace(')', '')
        return int(year)
    else:
        #если год не указан, возвращаем None
        return None

ratings_df = pd.read_csv('ratings/ratings_movies.csv')

ratings_df['year_release']=ratings_df['title'].apply(get_year_release)

#a=ratings_df[ratings_df['year_release']==1999].groupby('title')['rating'].mean().sort_values()

#a=ratings_df[ratings_df['year_release']==2010].groupby('genres')['rating'].mean().sort_values()

#a=ratings_df.groupby('userId')['rating'].agg(['count', 'mean']).sort_values(by=['count','mean'], ascending=[True, False])

#a=ratings_df.groupby('userId')['genres'].nunique().sort_values()

#a=ratings_df[ratings_df['year_release']==2018].groupby('genres')['rating'].agg(['count', 'mean'])

#b=a[a['count']>10].sort_values(by=['mean', 'count'], ascending=False)

##ratings_df['date'] = pd.to_datetime(ratings_df['date'])
#ratings_df['year_rating'] = ratings_df['date'].dt.year

#a=ratings_df.pivot_table(values='rating', index='genres', columns='year_rating', fill_value=0)

#print(a.loc['Comedy'])
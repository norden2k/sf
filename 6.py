import pandas as pd

citybike_df = pd.read_csv('citibike-tripdata.csv', index_col = False)

def time_of_day(in_hour):
    if 0<=in_hour<=6:
        return 'night'
    if 6<in_hour<=12:
        return 'morning'
    if 12<in_hour<=18:
        return 'day'
    if 18<in_hour<=23:
        return 'evening'

citybike_df['starttime']=pd.to_datetime(citybike_df['starttime'])

citybike_df['starttime']=citybike_df['starttime'].dt.hour

citybike_df['time_of_day']=citybike_df['starttime'].apply(time_of_day)

print(citybike_df['time_of_day'].value_counts())

print(143012/15085)

#trip_duration = pd.to_datetime(citybike_df['stoptime'])-pd.to_datetime(citybike_df['starttime'])

#trip_duration = trip_duration.dt.seconds

#print(trip_duration.mean())
import pandas as pd

def get_weekend(weekday):
    if weekday == 5 or weekday == 6:
        return 1
    else:
        return 0

melb_df = pd.read_csv('melb_data.csv', index_col = False)

melb_df['Date'] = pd.to_datetime(melb_df['Date'])

melb_df['WeekdaySale'] = melb_df['Date'].dt.dayofweek

weekend = melb_df['WeekdaySale'].apply(get_weekend)

melb_df['Weekends'] = weekend

a=melb_df[melb_df['Weekends']==1]['Price'].mean()

print(a)
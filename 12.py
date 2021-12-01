import pandas as pd

melb_df = pd.read_csv('melb_data_fe.csv')

answer = melb_df.pivot_table(values='Price', index='SellerG', columns='Type')

#answer = melb_df.pivot_table(values='BuildingArea', index='Rooms', columns='Type', fill_value=0, aggfunc='median')

print(answer[answer['unit']==answer['unit'].max()])

#melb_df['Date'] = pd.to_datetime(melb_df['Date'])

#mask1 = melb_df['Date'] >= pd.to_datetime('2017-05-01')
#mask2 = melb_df['Date'] <= pd.to_datetime('2017-09-01')

#print(melb_df[mask1 & mask2].groupby('SellerG')['Price'].sum().sort_values(ascending=True))

#print(melb_df.groupby(by='Regionname')['Lattitude'].std())

#print(melb_df.groupby(by='Rooms')['Price'].mean())

#print(melb_df['Type'].value_counts())

#mask1 = melb_df['Type']=='townhouse'
#mask2 = melb_df['Rooms'] > 2

#print(melb_df[mask1 & mask2].sort_values(by=['Rooms', 'MeanRoomsSquare'], ascending=[True, False], ignore_index=True).loc[18, 'Price'])

#print(melb_df.sort_values(by='AreaRatio', ascending=False, ignore_index=True).loc[1558, 'BuildingArea'])

#print(melb_df.at(1558, 'AreaRatio'))

##melb_df['Date'] = pd.to_datetime(melb_df['Date'])

##cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car']

##for col in melb_df.columns:
##    if melb_df[col].nunique() < 150 and col not in cols_to_exclude:
##        melb_df[col]=melb_df[col].astype('category')

##print(melb_df.describe())

#melb_df['quarter'] = melb_df['Date'].dt.quarter

#print(melb_df['quarter'].value_counts())
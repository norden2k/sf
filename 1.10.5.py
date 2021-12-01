import pandas as pd

ufo_df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv', index_col = False)

ufo_df['Time']=pd.to_datetime(ufo_df['Time'])

ufo_df['Date']=ufo_df['Time'].dt.date

mask=ufo_df['State']=='NV'

ufo_nevada=ufo_df[mask]

ufo_nevada['Dist']=ufo_nevada['Date'].diff()

ufo_nevada['Dist'] = ufo_nevada['Dist'].dt.days

print(ufo_nevada['Dist'].mean())

#ufo_df[mask]=ufo_df[mask]['Date'].diff()

#print(ufo_df[mask])

#print(ufo_df[mask])
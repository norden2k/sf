import pandas as pd

melb_df = pd.read_csv('melb_data.csv', index_col = False)

print(melb_df.info())

print(melb_df['Suburb'].nunique())

pop_urb = melb_df['Suburb'].value_counts().nlargest(119).index

melb_df['Suburb'] = melb_df['Suburb'].apply(lambda x: x if x in pop_urb else 'other')

melb_df['Suburb'] = melb_df['Suburb'].astype('category')

print(melb_df.info())

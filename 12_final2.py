import pandas as pd

orders_df = pd.read_csv('orders.csv', sep=';')
products_df = pd.read_csv('products.csv', sep=';')

orders_products = orders_df.merge(products_df, how='left', right_on='Product_ID', left_on='ID товара')

#print(orders_products[orders_products['Отменен']=='Да'])

orders_products['Прибыль']=orders_products['Количество']*orders_products['Price']

a=orders_products.groupby('ID Покупателя')['Прибыль'].max()

print(a.sort_values())
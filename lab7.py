import pandas as pd

car_sales_csv = pd.read_csv('carSale.csv')
car_sales_df = car_sales_csv.reset_index(drop=True).rename(columns={"Unnamed: 0":"Manufacturer"})
car_sales_df['Yearly Total'] = car_sales_df.drop('Manufacturer', axis=1).sum(axis=1)
car_sales_df.loc['Monthly Total',:] = car_sales_df.sum(axis=0)

print(car_sales_df)

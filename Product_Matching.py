import pandas as pd
# from pandas_profiling import ProfileReport
from IPython.display import display
import time

import keyboard
keyboard.press('f11')

# df = pd.read_csv('file_name.csv', engine='python')

dfAMZ = pd.read_csv('amz_com-ecommerce_sample.csv', encoding= 'unicode_escape')
dfFK = pd.read_csv('flipkart_com-ecommerce_sample.csv', encoding= 'unicode_escape')

# Checking if the given data contain any null/NaN value
# AMZnan = dfAMZ.isnull().sum().sum()
# print('Number of NaN values present in AMZ dataset: ' + str(AMZnan))

# FKnan = dfFK.isnull().sum().sum()
# print('Number of NaN values present in FK dataset: ' + str(FKnan))

# Drop only those rows where the specified column has a missing value
# Ignoring 'brand' column as it has no relation
subsets = ['retail_price', 'discounted_price', 'image', 'description', 'product_specifications']
dfAMZ.dropna(subset= subsets, inplace=True)
dfFK.dropna(subset= subsets, inplace=True)
dfAMZ.reset_index(drop=True, inplace=True) # resetig the index
dfFK.reset_index(drop=True, inplace=True)  # resetig the index

# print('DataFrame after using the subset function:')
# AMZnan = dfAMZ.isnull().sum().sum()
# print('Number of NaN values present in AMZ dataset: ' + str(AMZnan))
# FKnan = dfFK.isnull().sum().sum()
# print('Number of NaN values present in FK dataset: ' + str(FKnan))

# Making product list from Amazon and Flipkart dataframe and elemenating products with similar names
prodName = set(set(dfAMZ.product_name).union(set(dfFK.product_name)))
prodName = set(pN.lower() for pN in prodName)
prodName = {'Products': list(prodName)}
dfPName = pd.DataFrame(data = prodName)
display(dfPName)

from thefuzz import fuzz, process
productName = input("You can choose any product from above given products. \nEnter the product name: ")

similarProductsInAMZ = process.extract(productName, dfAMZ.product_name, limit=20, scorer=fuzz.token_set_ratio)
similarProductsInFK = process.extract(productName, dfFK.product_name, limit=20, scorer=fuzz.token_set_ratio)

AMZproduct = []
FKproduct = []

for product, similarityRate, index in similarProductsInAMZ:
    if similarityRate>95:
        AMZproduct.append(index)
        
for product, similarityRate, index in similarProductsInFK:
    if similarityRate>95:
        FKproduct.append(index)

dfSimilarProductAMZ = dfAMZ.iloc[AMZproduct]
dfSimilarProductFK = dfFK.iloc[FKproduct]

dropList = ['uniq_id','crawl_timestamp','product_url','product_category_tree','pid','image','is_FK_Advantage_product','description','product_rating','overall_rating','brand','product_specifications']

dfSimilarProductAMZ = dfSimilarProductAMZ.drop(dropList, axis = 1)
dfSimilarProductFK = dfSimilarProductFK.drop(dropList, axis = 1)

dfSimilarProductAMZ = dfSimilarProductAMZ.reset_index(drop=True)
dfSimilarProductFK = dfSimilarProductFK.reset_index(drop=True)

dfSimilarProductAMZ = dfSimilarProductAMZ.sort_values(by=['discounted_price'])
dfSimilarProductFK = dfSimilarProductFK.sort_values(by=['discounted_price'])

dfSimilarProductAMZ = dfSimilarProductAMZ.rename(columns={'product_name':'Product name in Amazon','retail_price':'Retail Price in Amazon','discounted_price':'Discounted Price in Amazon'})
dfSimilarProductFK = dfSimilarProductFK.rename(columns={'product_name':'Product name in Flipkart','retail_price':'Retail Price in Flipkart','discounted_price':'Discounted Price in Flipkart'})
display(pd.concat([dfSimilarProductFK ,dfSimilarProductAMZ], axis=1))

t = 20
while True:
  t -= 1
  print('Program terminates in',int(t),'seconds', end="", flush=True)
  print(" \r", end="", flush=True)
  time.sleep(1)
  if t == 0:
    keyboard.press('f11')
    break


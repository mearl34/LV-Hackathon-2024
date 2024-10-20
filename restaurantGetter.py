
import pandas as pd


df = pd.read_csv("campus_foods_datasets.csv", usecols=["ITEM_ID", "RESTAURANT_ID"])


column1_data = df["ITEM_ID"]
column2_data = df["RESTAURANT_ID"]
column1 = column1_data.tolist()
column2 = column2_data.tolist()
def search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
itemName="Muffin"
index = int(search(column1,itemName) )
resturant = column2[index]

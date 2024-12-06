import pandas as pd

print(pd.read_csv('text.txt')) #read data from text file

print(pd.read_excel('111.xlsx', sheet_name="Лист1"))#read data from excel file

dict_cities ={
    "City": ["Moscow", "Sankt-Petersburg", "Novosibirsk"],
    "Population": [12452, 4562, 7894]
}

df = pd.DataFrame(dict_cities) #create dataframe form dictionary
print(df) #print dataframe
print(df.describe()) #analize data and return avarage, max, min, etc.
print(df.shape) #show amount of rows and columns

print(df[df["City"] == "Moscow"])
# df.to_excel("cities.xlsx") #create excel file from dataframe
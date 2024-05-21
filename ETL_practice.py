#this code shows different ways to organize aquahives data
#remove the "#" if you want to look at the data
import pandas as pd

aquahives_data = pd.read_csv("aquahives_export.csv")

df = pd.DataFrame(aquahives_data)
df.info()

print(df.duplicated())

#see if there is duplicated data
duplicated_data = aquahives_data[aquahives_data.duplicated()]
print(duplicated_data)
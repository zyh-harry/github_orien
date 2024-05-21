#this code shows different ways to organize aquahives data
#remove the "#" if you want to look at the data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

aquahives_data = pd.read_csv('aquahives_export.csv')
#look at the data again
#print(aquahives_data)

#only show parameter values over the years at all sites
#tp_history = aquahives_data[['parameter', 'year(timestamp)', 'site']]
#print(tp_history)

#only show tp values over the years at pnwa in 2022
#data_2022 = aquahives_data.sort_values('site')
#print(data_2022)

#extract data for tp at pnwa in 2022
tp_pnwa_2022 = aquahives_data[
    (aquahives_data['parameter'] == 'tp') &
    (aquahives_data['year(timestamp)'] == 2022) &
    (aquahives_data['site'] == 'pnwa')
]
#print(tp_pnwa_2022)

#try grouping the data we want, for example: 
#grouped_data = tp_pnwa_2022.groupby(['parameter', 'value', 'site', 'year(timestamp)']).size()
#print(grouped_data)

print(aquahives_data[['parameter']].value_counts())

#identify duplicate rows, if there is any
#print(aquahives_data.duplicated())

#determine the categorical and numerical columns
cat_col = [col for col in aquahives_data.columns if aquahives_data[col].dtype == 'object']
print('Categorial columns: ', cat_col)

num_col = [col for col in aquahives_data.columns if aquahives_data[col].dtype != 'object']
print('Numerical column: ', num_col)

#total number of unique values in the categorical columns
print(aquahives_data[cat_col].nunique())

#prints the 4 unique parameters, can put a larger number to see all the unique parameters
print(aquahives_data['parameter'].unique()[:4])

aquahives_data2 = aquahives_data.drop(columns = 'year(timestamp)')
print(aquahives_data2)

aquahives_data3 = aquahives_data2.fillna(aquahives_data2.discharge.mean())
print(aquahives_data3)



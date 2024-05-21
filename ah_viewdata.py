import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


aquahives_data = pd.read_csv('aquahives_export.csv')
print(aquahives_data)

#in GitHub Codespaces, or in Visual Studio Code, must use the print() function to display the output?

#view just the parameter, value and year data
print(aquahives_data[['parameter', 'value', 'year(timestamp)']])

#the data set is so big, view just the 'tp' value data in 2023 at site pnwa
tp_2023_pnwa = aquahives_data[(aquahives_data.parameter == 'tp') & (aquahives_data['year(timestamp)'] == 2023) & (aquahives_data.site =='pnwa')]
print(tp_2023_pnwa)

#sort the 'tp' value data in 2023 at pnwa from low to high
sorted_tp2023 = tp_2023_pnwa.sort_values('value')
print(sorted_tp2023)

#a basic plot for 2023 tp data at pwna
tp_2023_pnwa.value.value_counts().plot()
plt.show()
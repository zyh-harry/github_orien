import pandas as pd
import matplotlib.pyplot as plt

aquahives_data = pd.read_csv('aquahives_export.csv')

#convert 'timestamp' to datetime 
aquahives_data['timestamp'] = pd.to_datetime(aquahives_data['timestamp'])

#extract only the tp value data in 2023 at pwna
tp_2023_pnwa = aquahives_data[(aquahives_data['parameter'] == 'tp') & (aquahives_data['year(timestamp)'] == 2023) & (aquahives_data['site'] == 'pnwa')]

#sort data by 'timestamp' 
tp_2023_pnwa = tp_2023_pnwa.sort_values('timestamp')

#set 'timestamp' as the index and this makes timestamp the x-axis
tp_2023_pnwa.set_index('timestamp', inplace=True)

#plotting the 'value' 
tp_2023_pnwa['value'].plot()

plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('2023 TP Data at PNWA')
plt.show()
plt.savefig('tp_2023_pnwa_plot.png')

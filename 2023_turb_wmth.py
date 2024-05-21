import pandas as pd
import matplotlib.pyplot as plt

aquahives_data = pd.read_csv('aquahives_export.csv')

#convert 'timestamp' to datetime 
aquahives_data['timestamp'] = pd.to_datetime(aquahives_data['timestamp'])

#extract only the tp value data in 2023 at wmth
turb_2023_wmth = aquahives_data[(aquahives_data['parameter'] == 'turbidity') & (aquahives_data['year(timestamp)'] == 2023) & (aquahives_data['site'] == 'wmth')]

#sort data by 'timestamp' 
turb_2023_wmth = turb_2023_wmth.sort_values('timestamp')

#set 'timestamp' as the index and this makes timestamp the x-axis
turb_2023_wmth.set_index('timestamp', inplace=True)

#plotting the 'value' 
turb_2023_wmth['value'].plot()

plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('2023 Turbidity at wmth')
plt.show()
plt.savefig('2023_turbidity_wmth.png')

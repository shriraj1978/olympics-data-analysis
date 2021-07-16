# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path

#Code starts here

# Data Loading 
data = pd.read_csv(path)

# Renaming the column
data.rename(columns={'Total':'Total_Medals'},inplace=True)

# Displaying first 10 records
data.head(10)

# Summer or Winter
data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')
data['Better_Event'] = np.where(data['Total_Summer']==data['Total_Winter'],'Both',data['Better_Event'])

# Finding the better event with respect to all the performing countries
better_event = data['Better_Event'].value_counts().index.values[0]
print('Better Event: ',better_event,'\n')

# Top 10
top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]

# Dropping the last row from top_countries
top_countries = top_countries[:-1]

# Creating a function top_ten
def top_ten(df,col):
    country_list = []
    country_list = list((df.nlargest(10,col)['Country_Name']))
    return country_list

# Calling the function top_ten and storing the results 
top_10_summer = top_ten(top_countries,'Total_Summer')
print('Top 10 Summer:\n',top_10_summer,'\n')

top_10_winter = top_ten(top_countries,'Total_Winter')
print('Top 10 Winter:\n',top_10_winter,'\n')

top_10 = top_ten(top_countries,'Total_Medals')
print('Top 10:\n',top_10,'\n')

# Creating the common list from all three lists
common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print('Common Countries:\n',common,'\n')

# Plotting top 10

# Plot for Top 10 countries at Summer Event
summer_df = data[data['Country_Name'].isin(top_10_summer)]

plt.figure(figsize=(20,6))
plt.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
plt.xlabel('Country_Name')
plt.ylabel('Total_Summer')
plt.title('Top 10 countries at Summer Event')
plt.show()

# Plot for Top 10 countries at Winter Event
winter_df = data[data['Country_Name'].isin(top_10_winter)]

plt.figure(figsize=(20,6))
plt.bar(winter_df['Country_Name'],summer_df['Total_Winter'])
plt.xlabel('Country_Name')
plt.ylabel('Total_Winter')
plt.title('Top 10 countries at Winter Event')
plt.show()

# Plot for Top 10 countries at Both Event
top_df = data[data['Country_Name'].isin(top_10)]

plt.figure(figsize=(20,6))
plt.bar(winter_df['Country_Name'],top_df['Total_Medals'])
plt.xlabel('Country_Name')
plt.ylabel('Total_Medals')
plt.title('Top 10 countries at Both Events')
plt.show()

# Top Performing Countries

# Top Performing Country in Summer Event
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = max(summer_df['Golden_Ratio'])
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

print('Top Country - Summer Event: ',summer_country_gold)
print('Golden Ratio : ',summer_max_ratio)

# Top Performing Country in Winter Event
winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = max(winter_df['Golden_Ratio'])
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

print('Top Country - Summer Event: ',winter_country_gold)
print('Golden Ratio : ',winter_max_ratio)

# Top Performing Country in Both Event
top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = max(top_df['Golden_Ratio'])
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']

print('Top Country - Both Event: ',top_country_gold)
print('Golden Ratio : ',top_max_ratio)

# Best in the world 

# Removing the last row from the data
data_1 = data[:-1]

# Creating a new column Total_Points
data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']

# Finding the max value of Total_Points
most_points = max(data_1['Total_Points'])

# Finding the country associated with max value of Total_Points
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']

print('Maximum Point acheived by ',best_country,' and the points are ',most_points)

# Plotting the best

# Creating a single row dataframe
best = data[data['Country_Name']==best_country]

# Subsetting the dataframe best to include columns Gold Total, Silver Total, Bronze Total
best = best[['Gold_Total','Silver_Total','Bronze_Total']]

# Plotting the stacked bar plot of best 
best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tallty')
plt.xticks(rotation=45)
plt.show()






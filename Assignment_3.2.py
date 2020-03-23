# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 20:10:27 2019

@author: Zach Hill
"""

# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create Pandas dataframe using the excel spreadsheet
df = pd.read_excel('hotdog-places.xlsm')

# Create labels and totals for categorical variables
labels = '1st', '2nd', '3rd'
totals = (sum(df.loc[0]), sum(df.loc[1]), sum(df.loc[2]))

# Bar Chart
plt.bar(labels, totals)
plt.ylabel('Hot Dogs Eaten')
plt.title('Total Hot Dogs Eaten By Top Contestants')

plt.show()

# Pie chart
plt.pie(totals, labels = labels, autopct = '%1.1f%%')
plt.title('Dogs Eaten by Top Contestants as % of Total')

plt.show()

# Line Plot
plt.plot(labels, totals)
plt.ylabel('Hot Dogs Eaten')
plt.title('Total Hot Dogs Eaten By Top Contestants')

plt.show()

# Grid for chart comparison
plt.figure(figsize = (9,3))
plt.subplot(131)
plt.bar(labels, totals)
plt.subplot(132)
plt.pie(totals, labels = labels, autopct = '%1.1f%%')
plt.subplot(133)
plt.plot(labels, totals)
plt.suptitle('Plot Comparison')

plt.show()
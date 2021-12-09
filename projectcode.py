"""
Name: David Xue
Email: David.Xue37@myhunter.cuny.edu
Title: Renovating NYC: Keeping our buildings and areas from deteriorating
Resources: https://www.geeksforgeeks.org/plotting-multiple-bar-charts-using-matplotlib-in-python/ (used to create double bar graph)
          https://www.geeksforgeeks.org/bar-plot-in-matplotlib/ (used to create side ways bar graph)
          https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html 
URl: https://asura124.github.io/DataScience/
"""

import pandas as pd
import pandasql as psql
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.style as style

style.available
style.use('fivethirtyeight')

###############################
#LANDMARK_COMPLAINT.CSV DATASET
###############################

#read the csv
landmarks_com = pd.read_csv('Landmarks_Complaints.csv')
#makes the borough lowercase
landmarks_com['Borough'] = landmarks_com['Borough'].str.lower()

#q1_land = 'SELECT Borough, COUNT(Borough) FROM landmarks_com GROUP BY Borough'
#query_one_land = psql.sqldf(q1_land)
#print(query_one_land)

#my query to group and count the boroughs and status
q2_land = 'SELECT Borough,Status, COUNT(Status) as num_status FROM landmarks_com GROUP BY Status,Borough ORDER BY Borough'
query_two_land = psql.sqldf(q2_land)
#print(query_two_land)

Boroughs = query_two_land['Borough']
#print(Boroughs.unique())
unq_boro = Boroughs.unique()
#print('\n')
status_open = []
status_closed = []
count = 0
#for loop
for i in (query_two_land['num_status']):
  #gets all the closed status count from Dataframe
  if(count%2==0):
    status_closed.append(i)
  #get all the open status count from Dataframe
  else:
    status_open.append(i)
  count += 1
#print(status_closed)
#print(status_open)

x = np.arange(5)
#print(x)
#plots the 2 bars for each boro
plt.bar(x - 0.2, status_open, 0.4,label='Open')
plt.bar(x + 0.2, status_closed, 0.4,label='Closed')
plt.xticks(x, unq_boro)
#set the labels of the graph
plt.xlabel("Boroughs")
plt.ylabel("Number of Reported Complaints")
plt.title("LandMark Complaints")
plt.legend()
#plt.show()
plt.tick_params(axis='x', which='major', labelsize=10) #used to fix overlapping issue in the x-axis
plt.tight_layout()
#saves the graph
plt.savefig("landmark")

#########################################
#HOUSING_MAINT_CODE_COMPLAINT.CSV DATASET
#########################################

#read the csv file 
house_maint_code = pd.read_csv('Housing_Maintenance_Code_Complaints.csv')
#makes the borough and status lower case since some are captialize and others lowercase
house_maint_code['Borough'] = house_maint_code['Borough'].str.lower()
house_maint_code['Status'] = house_maint_code['Status'].str.lower()

#q1_maint = 'SELECT Borough, COUNT(Borough) FROM house_maint_code GROUP BY Borough'
#query_one_maint = psql.sqldf(q1_maint)
#print(query_one_maint)
#my query to group and count the boroughs and status
q2_maint = 'SELECT Borough,Status, COUNT(Status) as num_status FROM house_maint_code GROUP BY Status, Borough ORDER BY Borough'
query_two_maint = psql.sqldf(q2_maint)
#print(query_two_maint)
#set 2 empty arr
status_open = []
status_closed = []
count = 0
#for loop
for i in (query_two_maint['num_status']):
  #gets all the closed status count from Dataframe
  if(count%2==0):
    status_closed.append(i)
  #get all the open status count from Dataframe
  else:
    status_open.append(i)
  count += 1

x = np.arange(5)
#print(x)
#plots the 2 bars for each boro
plt.bar(x - 0.2, status_open, 0.4,label='Open')
plt.bar(x + 0.2, status_closed, 0.4,label='Closed')
plt.xticks(x, unq_boro)
#set the labels of the graph
plt.xlabel("Boroughs")
plt.ylabel("Number of Reported Complaints")
plt.title("House Maintenance Code Complaint")
plt.legend()
#plt.show()
plt.tick_params(axis='x', which='major', labelsize=10) #used to fix overlapping issue in the x-axis
plt.tight_layout()
#saves the graph
plt.savefig("Housing")

##############################
#COMPLAINT_PROLBEM.CSV DATASET
##############################

#reads the csv file 
complaint_prob = pd.read_csv('Complaint_Problems.csv',engine='python', error_bad_lines=False) #needed to add the 2 arguements to skip lines where there were errors/ I couldn't read
#my query to get each unique issue/complaint and count them 
q1_comp_prob = 'SELECT MajorCategory, COUNT(MajorCategory) as num FROM complaint_prob GROUP BY MajorCategory' 
query_one_comp_prob = psql.sqldf(q1_comp_prob)
#print(query_one_comp_prob)
#sets the figuresize
plt.figure(figsize=(10,8))
#plots the information
plt.barh(query_one_comp_prob['MajorCategory'],query_one_comp_prob['num']) #https://www.geeksforgeeks.org/bar-plot-in-matplotlib/
#sets the label of the graph
plt.ylabel("Issues")
plt.xlabel("Num of Issues(In Millions)")
plt.title("Housing Complaints/Issues")
#plt.show()
plt.tight_layout()
#saves the graph
plt.savefig("Complaint")
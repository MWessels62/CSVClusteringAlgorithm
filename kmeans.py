#K-Means clustering implementation

#Some hints on how to start have been added to this file.
#You will have to add more code that just the hints provided here for the full implementation.
from random import sample
import math
import pandas as pd

#get user input):
def userInput():
  global number_clusters
  #year = input("From which year would you like to view the country data (1953 or 2008)")
  #number_clusters = input("How many clusters would you like to use? ")
  year = str(1953)
  number_clusters = str(3)
  return year

# ====
# Define a function that computes the distance between two data points
def distance(x1,y1,x2,y2):
     return math.sqrt((x1-x2)^2 + (y1-y2)^2)

# ====
# Define a function that reads data in from the csv files  HINT: http://docs.python.org/2/library/csv.html
def importCSV(year):
  #import csv 
  #with open('data1953.csv') as data_1953:
  #    reader_1953= csv.DictReader(data_1953)
  import csv 
  year_filename = "data" + year + ".csv"
  with open(year_filename) as country_data:
    data_reader = csv.DictReader(country_data)
    #for row in data_reader:
    #    print(row['BirthRate(Per1000 - '+ year + ')'], row['LifeExpectancy(' + year + ')'])
    #  print("")
    #print(row)
    global column1,column2
    column1 = "BirthRate(Per1000 - "+ year + ")"
    column2 = "LifeExpectancy(" + year + ")"
    global data_frame
    data_frame = pd.DataFrame(data_reader)
    #print(data_frame.iloc[3])
  return data_frame
    
# ====
# Write the initialisation procedure
#number_clusters = 3
def cluster_initialisation(data_frame):
  column1_samples = (data_frame.sample(n=3,random_state=1,axis=0))[column1]
  column2_samples = (data_frame.sample(n=3,random_state=1,axis=0))[column2]
  print(column1_samples.iloc[1],column2_samples.iloc[1])
  global clusters
  clusters = pd.DataFrame({'Cluster1': [column1_samples.iloc[0],column2_samples.iloc[0]],'Cluster2': [column1_samples.iloc[1],column2_samples.iloc[1]],'Cluster3': [column1_samples.iloc[2],column2_samples.iloc[2]]})
  print(clusters)
  print(type(clusters))


#Allocate each point to a cluster, for each point this will be calculating the distance to find the minimum, then do I write a new field to the text file with the clustering?

# ====
# Implement the k-means algorithm, using appropriate looping
# how do you "shift"the cluster point
#Applying each point to a cluster_initialisation
def kMeans():
  data_frame['Cluster'] = ""
  #The name of the closest cluster for each row will be stored here
  closest = ""
  cluster_distance = 0

  # iterate over rows with iterrows()
  for index, row in data_frame.head().iterrows():
    # access data using column names
    print(index, row[column1], row[column2])
    #Add cluster1 distance as default
    cluster_distance = distance(row[column1],row[column2],clusters.iloc[0,0], clusters.iloc[1,0])
    #print(row)
    #print(cluster_distance)
    #data_frame[column1] = data_frame.itemsets.transform(tuple)
    #df.loc[df.itemsets == ('26',), 'support']


# ====
# Print out the results



#Execution

importCSV(userInput())
cluster_initialisation(data_frame)
kMeans()



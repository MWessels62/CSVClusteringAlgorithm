# This program reads in life expectancy and birth rate data from either 1953 or 2008
# It will then perform a cluster analysis (the user determines the number of clusters to use)
# It also produces a graph to help choose the optimum number of clusters
# Information is printed on the number of countries per cluster, each of these countries is then printed out, and mean birth rates and life expectancy is provided

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import math


#get user input):
def userInput():
  global year
  global number_clusters
  year = str(input("From which year would you like to view the country data (1953 or 2008): "))
  number_clusters = int(input("How many clusters would you like to use?: "))
  return year

def importCSV(year):
    #Allows user to determine which year file to open   
    year_filename = "data" + year + ".csv"
    country_data = pd.read_csv(year_filename)
    country_data.head()

    descr1 = "BirthRate(Per1000 - "+ year + ")"
    descr2 = "LifeExpectancy(" + year + ")"
    
    global column1,column2, country_list
    column1 = country_data[descr1].values #BirthRate
    column2 = country_data[descr2].values #Life expectancy
    country_list = country_data['Countries'].values

    global main_model
    main_model = np.array(list(zip(column1,column2)))
    return main_model

importCSV(userInput())

#Initial calculation of random centroids for value of number_clusters
#X co-ordinates of random centroids 
C_x = np.random.randint(0,np.max(main_model)-20, size = number_clusters)
#Y co-ordinates of random centroids
C_y = np.random.randint(0, np.max(main_model)-20,size = number_clusters)


#Plotting the centroids
plt.scatter(column1,column2,c="#050505", s=20)
plt.scatter(C_x,C_y, marker = '*',s=200, c = 'g')
plt.xlabel("Birth rate per 1000 people")
plt.ylabel("Life expectancy (years)")
plt.title("Country data from " + year + "\nInitial randomised centroids")
#plt.show()



#Clustering algorithm

#Cluster plot
kmeans = KMeans(n_clusters = number_clusters)
#Fitting the input data
kmeans = kmeans.fit(main_model)

# Getting the cluster labels
#'labels' effectively stores which cluster each row belongs to
labels = kmeans.predict(main_model)

#Centroid values
centroids = kmeans.cluster_centers_


#Repeating with different number of clusters
colours = ['r','g','b','y','c','m','o','w']
fig2 = plt.figure()
new_plot = fig2.add_subplot(111)

for i in range(number_clusters):
    points = np.array([main_model[j] for j in range(len(main_model)) if labels[j] == i])
    new_plot.scatter(points[:,0], points[:,1], s=20, cmap = 'rainbow')
new_plot.scatter(centroids[:,0], centroids[:,1], marker = '*', s=200, c="#050505")
plt.xlabel("Birth rate per 1000 people")
plt.ylabel("Life expectancy (years)")
plt.title(("Country data from " + year + "\nClusters").format(number_clusters))


cluster_count = [0]*number_clusters
print("\n")
#Counts the number of countries in each cluster
for i in range(len(country_list)):
    cluster_count[labels[i]] += 1

#prints the number of countries in each cluster
for i in range(number_clusters):
    print("Cluster " + str(i) +  " has " + str(cluster_count[i]) + " countries")

#Prints the countries in each cluster and provides mean birth rate and life expectancy per cluster
for k in range(number_clusters):
    print("\nThe countries in cluster " + str(k) + " are...")
    mean_life, mean_birth = 0.0,0.0     # float
    count = 0   # integer
    for j in range(len(country_list)):

        if labels[j] == k:
            count += 1
            mean_life += column2[j]
            mean_birth += column1[j]
            print(country_list[j])
    print("The mean life expectancy of cluster "+ str(k) + " is: " + str(round(mean_life/count,2)))
    print("The mean birth rate of cluster "+ str(k) + " is: " + str(round(mean_birth/count,2)))





#ELBOW METHOD
    #The elbow method is used to determine the optimum K/number_clusters value
    #i.e. the elbow is the point where adding an additional cluster starts making a minimal difference

#cluster data into 1-10 clusters
K_range=range(1,10)
distortions = []

#Show the distance to centroid / distortion for adding up to 10 clusters
for i in K_range:
    kmeanModel = KMeans(n_clusters=i)
    kmeanModel.fit(main_model)
    distortions.append(sum(np.min(cdist(main_model, kmeanModel.cluster_centers_, 'euclidean'), axis =1)) / main_model.shape[0])
print("The distortions/distances to the centroids are: " + str(distortions))
fig1 = plt.figure()
ex = fig1.add_subplot(111)
ex.plot(K_range,distortions, 'b*-')

plt.grid(True)
plt.ylim([0,45])
plt.xlabel("Birth rate per 1000 people")
plt.ylabel("Life expectancy (years)")
plt.title("Selecting cluster numbers with the Elbow Method")
plt.show()
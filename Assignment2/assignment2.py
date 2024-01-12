# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:12:02 2021

@author: ergun
"""
import numpy as np 

def getName():
    #TODO: Add your full name instead of Lionel Messi
    return "Koorosh Shakoori"

def getStudentID():
    #TODO: Replace X's with your student ID. It should stay as a string and should have exactly 9 digits in it.
    return "X00000000"


def basic_k_means(df_data , n_clusters, n_iter = 100, random_seed = None):
     #TODO: Implement your logic here
    import pandas as pd
    import numpy as np

    #Assign the random seed as requested by the problem.
    np.random.seed(seed=random_seed)
    
    if len(df_data) < n_clusters:
        #As requested we raise an exception when K exceeds the sample count.
        raise ValueError("Number of clusters should not be greater than instance count.")
    
    else:
        #Choosing random centroids using random.choice from numpy.
        #By setting replace argument to False we avoid duplicates in initial centroids.
        #This will yield in an array of K(n_clusters) unique random indexes.
        centroid_list = np.random.choice(df_data.index ,n_clusters, replace=False)
        
        #Assigning the centroids from dataframe using the random index array.
        centroids = df_data.iloc[centroid_list, :].transpose()
        
        #Enumerating the centroid from zero upwards according to the problem.
        centroids.columns = list(range(n_clusters))
        
        #This dataframe is used to pass for the first loop when the last_centroid datadrame is not made yet.
        last_centroids = pd.DataFrame()
        iteration = 0

        while iteration < n_iter and not centroids.equals(last_centroids):
            #This is to check if the centroids has changed in each iteration, and if there is no change the loop will halt.
            #However, this loop is multi-conditional,
            #meaning even in case of a change if the iteration count surpasses the limit the loop will halt.
            last_centroids = centroids
            
            #This line calculate the euclidean norm of all data points in respect to each cluster center.
            distances = centroids.apply(lambda x: np.sqrt(((df_data - x) ** 2).sum(axis=1)))
            
            #Now we choose the index(in this case the column number since we use the transposed form),
            #with least distance to the point and assign it as the cluster for the data point.
            clusters = distances.idxmin(axis=1)
            
            #This line will yield new centroids by taking the average of all data points grouped by their new clusters.
            centroids = df_data.groupby(clusters).mean().T
            iteration += 1
    
    #Assigning the name of the cluster column as requested.
    clusters.name = 'Cluster'  
    
    #Returning the updated pandas dataframe including the last iteration of cluster values.
    return pd.concat([df_data, clusters], axis=1)



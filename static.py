from typing import *
from math import fsum,sqrt
from collections import defaultdict
from random import sample

#big Ideass with little code

#kmeans
allpoints =[(10,41,23),(22,30,29),(11,42,5),(20,32,4),(12,40,12),(21,36,23)]

def mean(a: Iterable)-> Tuple:
    return (fsum(a)/len(a))

def dist(centroid,point):
    return sqrt(fsum([(x-y)**2 for x,y in zip(centroid,point)]))

def assign_groups(centroids: Iterable,allpoints: Iterable):
    d = defaultdict(list)
    for point in allpoints:
        closest_centroid=min(centroids,key=lambda centroid: dist(centroid,point=point))
        d[closest_centroid].append(point)
    return dict(d)    

def compute_centroids(groups: Iterable) :
    new_centroids=[]
    for group in groups:
        centroid=[]
        for point in zip(*group):
            centroid.append(mean(point))
        centroid=tuple(centroid)
        new_centroids.append(centroid)    
    return new_centroids        



samp_cent = sample(allpoints,k=2)
for i in range(500):
    new_grps=assign_groups(samp_cent,allpoints)
# print(next(zip(*list(new_grps.values())[0])))
    samp_cent=compute_centroids(list(new_grps.values()))
print(samp_cent)    
print(new_grps)

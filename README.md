# VRU-Interaction Drivers

This reposirty contains the Source Code for Filtering the inD dataset by the drivers who interacts with the VRUs
# The Data

The code Contains 3 main DataFrame :

 - tracks : this data collected from "*_tracks.csv" files  this DataFrame contains the  details about   each Frame for each driver
 - pedestrians : this data is collected from "*_tracksMeta.csv" this DataFrame contains the class and the init Frame and the Final Frame for each pedestrian or bicyle
 - cars : this data is collected from "*_tracksMeta.csv" this DataFrame contains the class and the init Frame and the Final Frame for each car or truck bus 

## The Algorithm
This algorithm can only be applied for one recording at a time 
here's  an steps for finding if the car interacts with pedestrian or not

 - take one car from the cars DataFrame
 - Using the Overlaping formula get all the pedestrians who overlapped with the car frames
 - for each pedestrian who overlapped with the car get the overlapping frames
 - for each overlapping frame for the pedestrian and the car check the distance between the car and the pedestrian in this frame
 - if the distance is less than or equal to 5 then the Car considered to be interacted with the pedestrian and save it in result DataFrame
 - repeat the same steps for all cars 

## Adding the DVs for the interacted drivers

after getting the filtered drivers for each record we need to combine them into one DataFrame after that using the volitilty_df.csv file we extract in the main project we can map the DVs values for each driver and get the data ready for the next Step

## Clustering 

the same code used in the main project was used in this Project 
the only difference changing the source of data to be the new data we get 
so **we didn't include the code here in the repository**

## Result Analysis

all the results' analysis are discussed in the research paper we submit 

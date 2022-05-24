import py
import glob
import os.path
from matplotlib.pyplot import axes, axis
from numpy import square
import pandas as pd
import time
from math import sqrt
class Bouns: 
    interacted_drivers_id = []
    interacted_drivers_record = []

    def __init__(self):
        self.tracks = self.read_tracks()
        self.tracksMeta = self.read_meta()
        self.pedestrian = self.filter_pedestrian()
        self.car = self.filter_cars()
 
        self.car.apply(self.filteringFrame,axis = 1)
        finall_df = pd.DataFrame(data=self.interacted_drivers_id,columns=["trackid"])
        recordIdFrame = pd.DataFrame(data=self.interacted_drivers_record,columns=["recordingId"])
        finall_df["recordingId"]=recordIdFrame["recordingId"]
        finall_df.to_csv("29.csv")
        print("finisheed")
    def read_tracks(self):
        return  pd.read_csv("data/29_tracks.csv")

    def read_meta(self):
        return  pd.read_csv("data/29_tracksMeta.csv")

    def filter_pedestrian(self):
        condition = (self.tracksMeta["class"]=="pedestrian") | (self.tracksMeta["class"]=="bicycle")
        return self.tracksMeta[condition]

    def filter_cars(self):
        condition = (self.tracksMeta["class"]=="car") | (self.tracksMeta["class"]=="truck_bus")
        return self.tracksMeta[condition]

    def filteringFrame(self,row):
        init = row["initialFrame"]
        final = row["finalFrame"]
        pedestrian2 = self.pedestrian.copy(deep=True)
        pedestrian2 ["overlabed"] = pedestrian2.apply(self.detectOverLaping,args=[init,final],axis=1)
        pedestrian2 = pedestrian2[pedestrian2["overlabed"]==1]

        pedestrian2.apply(self.filteringIndex,args=[row],axis=1)

    def detectOverLaping(self,row,init,final):

        return int(max(row["initialFrame"],init) <= min(row["finalFrame"],final))


    def filteringIndex(self,pedestrianRow,carRow):   
   
        pedInit = pedestrianRow["initialFrame"]
        pedFinal = pedestrianRow["finalFrame"]
        carInit = carRow["initialFrame"]
        carFinal = carRow["finalFrame"]
        pedList = list(range(pedInit,pedFinal+1))
        carList = list(range(carInit,carFinal+1))
        overlabedList = list(set(pedList) & set(carList))
        for frame in overlabedList:
            if(carRow["trackId"] in self.interacted_drivers_id):
                return
            condition = ((self.tracks["recordingId"]==pedestrianRow["recordingId"]) & (self.tracks["trackId"]==pedestrianRow["trackId"])& (self.tracks["frame"]==frame))
            pedestrianX = self.tracks[condition]["xCenter"].values[0]
            pedestrianY = self.tracks[condition]["yCenter"].values[0]
            condition = ((self.tracks["recordingId"]==carRow["recordingId"]) & (self.tracks["trackId"]==carRow["trackId"])& (self.tracks["frame"]==frame))
            carX = self.tracks[condition]["xCenter"].values[0]
            carY = self.tracks[condition]["yCenter"].values[0]

            if sqrt((pow(carX-pedestrianX,2)+pow(carY-pedestrianY,2))) <= 5:
                self.interacted_drivers_id.append(carRow["trackId"])
                self.interacted_drivers_record.append(carRow["recordingId"])
                return      
    




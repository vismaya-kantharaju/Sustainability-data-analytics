import numpy as np
import pandas as pd


class preprocessing:

    def __init__(self, number_of_sensors = 6, tables_names= 'random', table_size  = 1000):
        self.no_sensors = number_of_sensors 
        self.table_names  = tables_names
        self.table_size = table_size

    def add_data(self, data=None):
        # generating a random number in the table for now.
        sensor_names  = ['Temp', 'Carbon', 'water', 'ele', 'solid_waste', 'occupancy']
        temp = np.random.random(self.table_size)
        Carbon=np.random.random(self.table_size)
        water=np.random.random(self.table_size)
        ele=np.random.random(self.table_size)
        solid_waste=np.random.random(self.table_size)
        occupancy=np.random.random(self.table_size)
        self.dataframe = pd.DataFrame([temp,Carbon,water,ele,solid_waste,occupancy], columns=sensor_names)



    def process_temp(self):
        self.dataframe['Temp']


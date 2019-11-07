"""Prerequesites"""

import pandas as pd
import matplotlib.pyplot as plt
import os
from Tire import Tire

"""Data import"""
# Import boundary values for sorting
df = pd.read_table("Grenzen.txt", header=None)
keys = df[0].tolist()
lowerBorders = df[1].tolist()
upperBorders = df[2].tolist()
key_dict = {"ia_keys": keys[0:3], "fz_keys": keys[3:7], "sa_keys": keys[7:]}
lowerBorder_dict = {
    "ia_lBorder": lowerBorders[0:3], "fz_lBorder": lowerBorders[3:7], "sa_lBorder": lowerBorders[7:]}
upperBorder_dict = {
    "ia_uBorder": upperBorders[0:3], "fz_uBorder": upperBorders[3:7], "sa_uBorder": upperBorders[7:]}

# Import Braking files
files_braking = os.listdir("Data/Braking")
files_braking = [('Data/Braking/' + i) for i in files_braking]

# Import Cornering Files


# Import pressure levels
pressure_keys_df = pd.read_table("Druck.txt", header=None)
pressure_keys = pressure_keys_df[0].tolist()
data = {pressure_keys[0]: 0}

# Import raw data
for i in range(len(files_braking)):
    data[pressure_keys[i]] = pd.read_table(
        files_braking[i], header=[1], skiprows=[2])

# Create new object of class Tire and use the object function to sort data in "situations"
hoosier13 = Tire(13, data, pressure_keys)
hoosier13.sortLonData(key_dict["ia_keys"], key_dict["fz_keys"], key_dict["sa_keys"], 
                      lowerBorder_dict["ia_lBorder"], upperBorder_dict["ia_uBorder"],
                      lowerBorder_dict["fz_lBorder"], upperBorder_dict["fz_uBorder"], 
                      lowerBorder_dict["sa_lBorder"], upperBorder_dict["sa_uBorder"])

#hoosier13.sortLatData(key_dict["ia_keys"],key_dict["fz_keys"],key_dict["sa_keys"], lowerBorder_dict["ia_lBorder"], upperBorder_dict["ia_uBorder"], lowerBorder_dict["fz_lBorder"], upperBorder_dict["fz_uBorder"], lowerBorder_dict["sa_lBorder"], upperBorder_dict["sa_uBorder"] )


# Plot sorted data
# hoosier13.plotLonData(key_dict["ia_keys"])
# hoosier13.plotLatData(key_dict["ia_keys"])

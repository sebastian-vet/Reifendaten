"""Prerequesites"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os
from Tire import Tire
from pprint import pprint

matplotlib.use('TkAgg')


key_dict: dict
lower_border_dict: dict
upper_border_dict: dict
data: dict

files_braking: list
pressure_keys: list

def import_raw_data():
    global key_dict, lower_border_dict, upper_border_dict, data
    global files_braking, pressure_keys

    """Data import"""
    # Import boundary values for sorting
    df = pd.read_table("Grenzen.txt", header=None)

    keys = df[0].tolist()
    lowerBorders = df[1].tolist()
    upperBorders = df[2].tolist()

    key_dict = {
        "ia_keys": keys[0:3],
        "fz_keys": keys[3:7],
        "sa_keys": keys[7:]
    }

    lower_border_dict = {
        "ia_lBorder": lowerBorders[0:3], 
        "fz_lBorder": lowerBorders[3:7], 
        "sa_lBorder": lowerBorders[7:]
    }

    upper_border_dict = {
        "ia_uBorder": upperBorders[0:3],
        "fz_uBorder": upperBorders[3:7],
        "sa_uBorder": upperBorders[7:]
    }

    # Import Braking files
    files_braking = [('Data/Braking/' + i) for i in os.listdir("Data/Braking")]

    # Import pressure levels
    pressure_keys_df = pd.read_table("Druck.txt", header=None)
    pressure_keys = pressure_keys_df[0].tolist()

    data = {}

    # Import raw data
    for path, pressure_key in zip(files_braking, pressure_keys):
        table = pd.read_table(path, header=[1], skiprows=[2])


import_raw_data()

# x = [for item["V"] in data.items[0]]

def plot():
    for path, pressure_key in zip(files_braking, pressure_keys):
        table = pd.read_table(path, header=[1], skiprows=[2])
        plt.plot(table["ET"], table["V"], label="locations filled")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    plot()


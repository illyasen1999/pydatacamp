import numpy as np
import pandas as pd

def basic_loop():
    # Initialize offset
    offset = 8

    # Code the while loop
    while offset != 0:
        print('correcting...')
        offset = offset - 1

def loops_with_conditionals():
    # Initialize offset
    offset = -6

    # Code the while loop
    while offset != 0 :
        print("correcting...")
        if offset > 0 :
            offset = offset - 1
        else : 
            offset = offset + 1
            print(offset)

def loop_over_a_list():
    # areas list
    areas = [11.25, 18.0, 20.0, 10.75, 9.50]

    # Code the for loop
    for a in areas:
        print(a)

def indexes_and_values_1():
    # areas list
    areas = [11.25, 18.0, 20.0, 10.75, 9.50]

    # Change for loop to use enumerate() and update print()
    for index, area in enumerate(areas) :
        print("room " + str(index) + ": " + str(area))

def indexes_and_values_2():
    # areas list
    areas = [11.25, 18.0, 20.0, 10.75, 9.50]

    # Code the for loop
    for index, area in enumerate(areas) :
        print("room " + str(index + 1) + ": " + str(area))

def loop_over_list_of_lists():
    # house list of lists
    house = [["hallway", 11.25], 
            ["kitchen", 18.0], 
            ["living room", 20.0], 
            ["bedroom", 10.75], 
            ["bathroom", 9.50]]
            
    # Build a for loop from scratch
    for x,y in enumerate(house):
        print("the " + str(house[x][0]) + " is " + str(house[x][1]) + " sqm")

def loop_over_dictionary():
    # Definition of dictionary
    europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
            'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
            
    # Iterate over europe
    for country, capital in europe.items():
        print("the capital of " + country + " is " + capital)

def loop_over_numpy_array():
    # For loop over np_height
    for height in np_height:
        print(str(height) + " inches")

    # For loop over np_baseball
    for baseball in np.nditer(np_baseball):
        print(baseball)

def loop_over_dataframe_1():
    cars = pd.read_csv('./data/cars.csv', index_col = 0)

    # Iterate over rows of cars
    for lab, con in cars.iterrows():
        print(lab)
        print(con)

def loop_over_dataframe_2():
    cars = pd.read_csv('./data/cars.csv', index_col = 0)

    # Adapt for loop
    for lab, row in cars.iterrows() :
        print(lab + ": " + str(row['cars_per_cap']))

def add_column_1():
    cars = pd.read_csv('./data/cars.csv', index_col = 0)

    # Adapt for loop
    for lab, row in cars.iterrows() :
        print(lab + ": " + str(row['cars_per_cap']))

def add_column_2():
    cars = pd.read_csv('./data/cars.csv', index_col = 0)

    # Use .apply(str.upper)
    # for lab, row in cars.iterrows() :
        # cars.loc[lab, "COUNTRY"] = row["country"].upper()

    cars['COUNTRY'] = cars['country'].apply(str.upper)

    print(cars)

import numpy as np

def comparisons():
    # Comparison of booleans
    True == False

    # Comparison of integers
    -5 * 15 != 75

    # Comparison of strings
    "pyscript" == "PyScript"

    # Compare a boolean with an integer
    True == 1

    # Comparison of integers
    x = -3 * 6
    print(x >= -10)

    # Comparison of strings
    y = "test"
    print("test" <= y)

    # Comparison of booleans
    print(True > False)

def compare_arrays():
    my_house = np.array([18.0, 20.0, 10.75, 9.50])
    your_house = np.array([14.0, 24.0, 14.25, 9.0])

    # my_house greater than or equal to 18
    print(my_house >= 18)

    # my_house less than your_house
    print(my_house < your_house)

def bools():
    # and, or, not
    # Define variables
    my_kitchen = 18.0
    your_kitchen = 14.0

    # my_kitchen bigger than 10 and smaller than 18?
    print(my_kitchen > 10 and my_kitchen < 18)

    # my_kitchen smaller than 14 or bigger than 17?
    print(my_kitchen < 14 or my_kitchen > 17)

    # Double my_kitchen smaller than triple your_kitchen?
    print(my_kitchen * 2 < your_kitchen * 3)

def bool_with_numpy():
    # normal and, or, not comparisons dont work with nunpy arrays, instead there are numpy functions for and, or, not
    my_house = np.array([18.0, 20.0, 10.75, 9.50])
    your_house = np.array([14.0, 24.0, 14.25, 9.0])

    # my_house greater than 18.5 or smaller than 10
    print(np.logical_or(my_house > 18.5, my_house < 10))

    # Both my_house and your_house smaller than 11
    print(np.logical_and(my_house < 11, your_house < 11))

def if_elif_else():
    # Define variables
    room = "kit"
    area = 14.0

    # if statement for room
    if room == "kit" :
        print("looking around in the kitchen.")

    # if statement for area
    if area > 15:
        print("big place!")

  # if-else construct for room
    if room == "kit" :
        print("looking around in the kitchen.")
    else :
        print("looking around elsewhere.")

    # if-else construct for area
    if area > 15 :
        print("big place!")
    else:
        print("pretty small.")
        
    # if-elif-else construct for room
    if room == "kit" :
        print("looking around in the kitchen.")
    elif room == "bed":
        print("looking around in the bedroom.")
    else :
        print("looking around elsewhere.")

    # if-elif-else construct for area
    if area > 15 :
        print("big place!")
    elif area > 10:
        print("medium size, nice!")
    else :
        print("pretty small.")

# TODO: Intermediate Python - Filtering pandas DataFrames
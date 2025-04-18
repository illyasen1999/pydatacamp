import pandas as pd

def get_capital():
    # Definition of countries and capital
    countries = ['spain', 'france', 'germany', 'norway']
    capitals = ['madrid', 'paris', 'berlin', 'oslo']

    # Get index of 'germany': ind_ger
    ind_ger = countries.index("germany")

    # Use ind_ger to print out capital of Germany
    print(capitals[ind_ger])

def py_dictionary():
    # CREATING DICTIONARY
    # Definition of countries and capital
    countries = ['spain', 'france', 'germany', 'norway']
    capitals = ['madrid', 'paris', 'berlin', 'oslo']

    # From string in countries and capitals, create dictionary europe
    europe = {
        'spain':'madrid', 
        'france':'paris', 
        'germany':'berlin', 
        'norway':'oslo'
    }

    # Print europe
    print(europe)

    # ACCESSING DICTIONARY
    # Definition of dictionary
    europe_2 = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

    # Print out the keys in europe_2
    print(europe_2.keys())


    # Print out value that belongs to key 'norway'
    print(europe_2['norway'])

def py_dictionary_2():
    # DICTIONARY MANIPULATION(1)
    # Definition of dictionary
    europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

    # Add italy to europe
    europe['italy'] = 'rome'

    # Print out italy in europe
    print('italy' in europe)

    # Add poland to europe
    europe['poland'] = 'warsaw'

    # Print europe
    print(europe)

    # DICTIONARY MANIPULATION(2)
    # Definition of dictionary
    europe_2 = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
            'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
            'australia':'vienna' }

    # Update capital of germany
    europe_2['germany'] = 'berlin'

    # Remove australia
    del europe_2['australia']

    # Print europe_2
    print(europe_2)

    # DICTIONARICEPTION
    # Dictionary of dictionaries
    europe_3 = { 'spain': { 'capital':'madrid', 'population':46.77 },
            'france': { 'capital':'paris', 'population':66.03 },
            'germany': { 'capital':'berlin', 'population':80.62 },
            'norway': { 'capital':'oslo', 'population':5.084 } }


    # Print out the capital of France
    print(europe_3['france']['capital'])

    # Create sub-dictionary data
    data = {
        'capital': 'rome',
        'population': 59.83
    }

    # Add data to europe_3 under key 'italy'
    europe_3['italy'] = data

    # Print europe_3
    print(europe_3)

def pandas_df_1():
    # DICTIONARY TO DATAFRAME(1)
    # Pre-defined lists
    names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
    dr =  [True, False, False, False, True, True, True]
    cpc = [809, 731, 588, 18, 200, 70, 45]

    # Create dictionary my_dict with three key:value pairs: my_dict
    my_dict = {
        'country': names,
        'drives_right': dr,
        'cars_per_cap': cpc,
    }

    # Build a DataFrame cars from my_dict: cars
    cars = pd.DataFrame(my_dict)

    # Print cars
    print(cars)


def pandas_df_2():
    # DICTIONARY TO DATAFRAME(2)
    # Build cars DataFrame
    names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
    dr =  [True, False, False, False, True, True, True]
    cpc = [809, 731, 588, 18, 200, 70, 45]
    cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
    cars = pd.DataFrame(cars_dict)
    # print(cars)

    # Definition of row_labels
    row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

    # Specify row labels of cars
    cars.index = row_labels

    # Print cars again
    print(cars)

def csv_to_dataframe_1():
    # Import the cars.csv data: cars
    cars = pd.read_csv('./data/cars.csv')

    # Print out cars
    print(cars)

def csv_to_dataframe_2():
    # Fix import by including index_col
    cars = pd.read_csv('./data/cars.csv', index_col=0)

    # Print out cars
    print(cars)

def square_brackets():
    cars = pd.read_csv('./data/cars.csv', index_col=0)

    # Print out country column as Pandas Series(w/o top label)
    print(cars['country'])

    # Print out country column as Pandas DataFrame(w/ top label)
    print(cars[['country']])

    # Print out DataFrame with country and drives_right columns
    print(cars[['country', 'drives_right']])
    
def square_brackets_2():
    cars = pd.read_csv('./data/cars.csv', index_col = 0)

    # Print out first 3 observations
    print(cars[0:3])

    # Print out fourth, fifth and sixth observation
    print(cars[3:6])

def loc_and_iloc_1():
    cars = pd.read_csv('./data/cars.csv', index_col = 0)

    # Print out observation for Japan
    print(cars.loc['JPN'])
    print(cars.iloc[2])
    print(cars)

    # Print out observations for Australia and Egypt
    print(cars.loc[['AUS', 'EG']])
    print(cars.iloc[[1, 6]])

def loc_and_iloc_2():
    cars = pd.read_csv('./data/cars.csv', index_col = 0)
    # print(cars)
    # Print out drives_right value of Morocco
    print(cars.loc['MOR', 'drives_right'])
    print(cars.iloc[-3, 2])

    # Print sub-DataFrame
    print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

def loc_and_iloc_3():

    cars = pd.read_csv('./data/cars.csv', index_col = 0)

    # Print out drives_right column as Series
    print(cars.loc[:, 'drives_right'])

    # Print out drives_right column as DataFrame
    print(cars.loc[: ,['drives_right']])

    # Print out cars_per_cap and drives_right as DataFrame
    print(cars.loc[:, ['cars_per_cap', 'drives_right']])
    print(cars.iloc[:, [0, 2]])


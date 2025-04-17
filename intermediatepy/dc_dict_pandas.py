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

def pandas_pandas():
    # TODO: Intermediate Python: Pandas
    pass
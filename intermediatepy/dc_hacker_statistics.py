import numpy as np
import matplotlib.pyplot as plt

def random_float():
    # Set the seed
    np.random.seed(123)

    # Generate and print random float
    print(np.random.rand())

def roll_the_dice():
    np.random.seed(123)

    # Use randint() to simulate a dice
    print(np.random.randint(1,7))

    # Use randint() again
    print(np.random.randint(1,7))

def determine_next_move():
    np.random.seed(123)

    # Starting step
    step = 50

    # Roll the dice
    dice = np.random.randint(1, 7)

    # Finish the control construct
    if dice <= 2 :
        step = step - 1
    elif dice <= 5 :
        step = step + 1
    else :
        step = step + np.random.randint(1,7)

    # Print out dice and step
    print(dice)
    print(step)

def the_next_step():
    np.random.seed(123)

    # Initialize random_walk
    random_walk = [0]

    # Complete the ___
    for x in range(100) :
        # Set step: last element in random_walk
        step = random_walk[-1]

        # Roll the dice
        dice = np.random.randint(1,7)

        # Determine next step
        if dice <= 2:
            step = step - 1
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # append next_step to random_walk
        random_walk.append(step)

    # Print random_walk
    print(random_walk)

def long_walk():
    np.random.seed(123)

    # Initialize random_walk
    random_walk = [0]

    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

    print(random_walk)

def visualize_the_walk():
    # Initialization
    random_walk = [0]

    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        random_walk.append(step)

    # Plot random_walk
    plt.plot(random_walk)

    # Show the plot
    plt.show()

def sim_simple_walks():
    np.random.seed(123)


    # Initialize all_walks (don't change this line)
    all_walks = []

    # Simulate random walk five times
    for i in range(5) :

        # Code from before
        random_walk = [0]
        for x in range(100) :
            step = random_walk[-1]
            dice = np.random.randint(1,7)

            if dice <= 2:
                step = max(0, step - 1)
            elif dice <= 5:
                step = step + 1
            else:
                step = step + np.random.randint(1,7)
            random_walk.append(step)

        # Append random_walk to all_walks
        all_walks.append(random_walk)

    # Print all_walks
    print(all_walks)

def vis_all_walks():
    np.random.seed(123)

    # initialize and populate all_walks
    all_walks = []
    for i in range(5) :
        random_walk = [0]
        for x in range(100) :
            step = random_walk[-1]
            dice = np.random.randint(1,7)
            if dice <= 2:
                step = max(0, step - 1)
            elif dice <= 5:
                step = step + 1
            else:
                step = step + np.random.randint(1,7)
            random_walk.append(step)
        all_walks.append(random_walk)

    # Convert all_walks to NumPy array: np_aw
    np_aw = np.array(all_walks)

    # Plot np_aw and show
    plt.plot(np_aw)
    plt.show()

    # Clear the figure
    plt.clf()

    # Transpose np_aw: np_aw_t
    np_aw_t = np.transpose(np_aw)

    # Plot np_aw_t and show
    plt.plot(np_aw_t)
    plt.show()

def implement_clumsiness():
    np.random.seed(123)

    # clear the plot so it doesn't get cluttered if you run this many times
    plt.clf()

    # Simulate random walk 20 times
    all_walks = []
    for i in range(20) :
        random_walk = [0]
        for x in range(100) :
            step = random_walk[-1]
            dice = np.random.randint(1,7)
            if dice <= 2:
                step = max(0, step - 1)
            elif dice <= 5:
                step = step + 1
            else:
                step = step + np.random.randint(1,7)

            # Implement clumsiness
            if np.random.rand() <= 0.005 :
                step = 0

            random_walk.append(step)
        all_walks.append(random_walk)

    # Create and plot np_aw_t
    np_aw_t = np.transpose(np.array(all_walks))
    plt.plot(np_aw_t)
    plt.show()

def plot_the_distribution():
    np.random.seed(123)

    # Simulate random walk 500 times
    all_walks = []
    for i in range(500) :
        random_walk = [0]
        for x in range(100) :
            step = random_walk[-1]
            dice = np.random.randint(1,7)
            if dice <= 2:
                step = max(0, step - 1)
            elif dice <= 5:
                step = step + 1
            else:
                step = step + np.random.randint(1,7)
            if np.random.rand() <= 0.001 :
                step = 0
            random_walk.append(step)
        all_walks.append(random_walk)

    # Create and plot np_aw_t
    np_aw_t = np.transpose(np.array(all_walks))

    # Select last row from np_aw_t: ends
    ends = np_aw_t[-1,:]

    # Plot histogram of ends, display plot
    plt.hist(ends)
    plt.show()
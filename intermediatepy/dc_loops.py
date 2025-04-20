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
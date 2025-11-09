EXPECTED_BAKE_TIME=40

def bake_time_remaining(minutes_in_already):
    """Calculate the remaining bake time.

    :param minutes_in_already: int - baking time already elapsed.
    :return: int - remaining bake time in minutes.
    
    This function takes the actual minutes the lasagna has been in the
    oven as an argument and subtracts it from the expected bake time.
    """
    return EXPECTED_BAKE_TIME-minutes_in_already

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total preparation time (2 min per layer).
    
    This function takes the number of layers and multiplies
    them by the time it takes to prepare one layer.
    """
    PREPARATION_TIME=0
    for n in range(number_of_layers):
        print("...")
        PREPARATION_TIME+=2
    return PREPARATION_TIME
    
        
def elapsed_time_in_minutes(number_of_layers,minutes_in_already):
    """Calculate the total elapsed time in minutes.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param minutes_in_already: int - baking time already elapsed.
    :return: int - total elapsed time (preparation + baking).
    
    This function calculates the total time spent cooking so far by
    adding the preparation time to the time already spent in the oven.
    """
    return (preparation_time_in_minutes(number_of_layers))+minutes_in_already
    




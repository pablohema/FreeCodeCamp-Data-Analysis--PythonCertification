import numpy as np


def calculate(numbers):
    # List must contain 9 numbers.
    if not len(numbers) == 9:
        raise ValueError("List must contain nine numbers.")

    # Declare empty dictionary
    calculations = {}

    # Shape list to 3X3 matrix
    arr = np.array(numbers)
    np_arr = arr.reshape((3, 3))

    # Calculate mean
    calculations['mean'] = [list(np.mean(np_arr, axis=0)), list(np.mean(np_arr, axis=1)), np.mean(arr)]

    # Calculate variance
    calculations['variance'] = [list(np.var(np_arr, axis=0)), list(np.var(np_arr, axis=1)), np.var(arr)]
    
    # Calculate standard deviation
    calculations['standard deviation'] = [list(np.std(np_arr, axis=0)), list(np.std(np_arr, axis=1)), np.std(arr)]
    
    # Calculate max
    calculations['max'] = [list(np.max(np_arr, axis=0)), list(np.max(np_arr, axis=1)), np.max(arr)]
    
    # Calculate min
    calculations['min'] = [list(np.min(np_arr, axis=0)), list(np.min(np_arr, axis=1)), np.min(arr)]
    
    # Calculate sum
    calculations['sum'] = [list(np.sum(np_arr, axis=0)), list(np.sum(np_arr, axis=1)), np.sum(arr)]

    return calculations
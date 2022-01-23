from timeit import timeit
import numpy as np
import pandas as pd



# Remember that unlike Python lists, NumPy is constrained to arrays that all contain the same type. If types do not match, NumPy will upcast if possible (here, integers are up-cast to floating point):

# Basic array manipulations:
# Attributes of arrays: Determining the size, shape, memory consumption, and data types of arrays
# Indexing of arrays: Getting and setting the value of individual array elements
# Slicing of arrays: Getting and setting smaller subarrays within a larger array
# Reshaping of arrays: Changing the shape of a given array
# Joining and splitting of arrays: Combining multiple arrays into one, and splitting one array into many

print(timeit("sum([1, 23, 4])"))
print(timeit("np.sum([1, 23, 4])"))

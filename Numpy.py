# import numpy as np
# salary = np.array([20000, 30000, 40000])
# print(salary * 1.10)

# import numpy as np
# arr = np.array([10,20,30])
# print(arr + arr)

# import numpy as np
# marks = np.array([85, 90, 78, 92])
# print(marks)

# import numpy as np
# sales = np.array([12000, 15000, 18000, 20000])
# print(sales)

# import numpy as np
# employee_data = np.array([
#     [101, 25000],
#     [102, 30000],
#     [103, 35000]
# ])
# print(employee_data)

# Creating Array using zeros()//
# import numpy as np
# my_array = np.zeros(5)
# print(my_array)

# import numpy as np
# my_array = np.zeros((3,4))
# print(my_array)

# Creating Array using ones()//
# import numpy as np
# my_array = np.ones(5)
# print(my_array)

# import numpy as np
# my_array = np.ones((3,4))
# print(my_array)

# Using arange()//
# import numpy as np
# range = np.arange(1,11)
# print(range)

# import numpy as np
# range = np.arange(1,11,2)
# print(range)

# import numpy as np
# range = np.arange(0,11,2)
# print(range)

# Using linspace()//
# import numpy as np
# range = np.linspace(1,10,5)
# print(range)

# Random Number Generation//                    #Random Integers//
# import numpy as np
# range = np.random.randint(1,100,10)
# print(range)

                                                # Random Decimal Values//
# import numpy as np
# range = np.random.random(5)
# print(range)

#  Array Properties//
# ndim//                #shows dimensions//
# import numpy as np
# arr = np.array([[1,2],[3,4]])
# print(arr.ndim)

# shape//            # Shows rows and columns//
# import numpy as np
# arr = np.array([[1,2],[3,4]])
# print(arr.shape)

# size//            # Total number of elements//
# import numpy as np
# arr = np.array([[1,2],[3,4]])
# print(arr.size)

# dtype//           # Shows datatype//
# import numpy as np
# arr = np.array([[1,2],[3,4]])
# print(arr.dtype)

# Indexing in 1D Array//
# import numpy as np
# sales = np.array([10000,15000,20000,25000])
# print(sales[0])
# print(sales[2])

# Negative Indexing//
# import numpy as np
# sales = np.array([10000,15000,20000,25000])
# print(sales[-1])
# print(sales[-2])
# print(sales[-3])
# print(sales[-4])

# Slicing in NumPy//                #array[start:end]//
# import numpy as np
# arr = np.array([10,20,30,40,50])
# print(arr[1:4])

# Step Slicing//
# import numpy as np
# arr = np.array([10,20,30,40,50])
# print(arr[0:5:2])

# 2D Array Indexing & Slicing//
# import numpy as np
# employee = np.array([
#     [101,25000],
#     [102,30000],
#     [103,35000]
# ])
# print(employee[1])                  #Access Row//
# print(employee[1,1])                # Access Specific Value//

# import numpy as np
# employee = np.array([
#     [101,25000],
#     [102,30000],
#     [103,35000]
# ])
# print(employee[:,1])                    #Access Full Column//

# Creating and importing modules
import math_utils

print(math_utils.add(5, 3))
print(math_utils.sub(5, 3)) 

# Importing specific functions

from math_utils import add

print(add(5, 3))

# Built-in Modules
import math
print(math.sqrt(16))

print("module says ",__name__)

import sys
print(sys.path)

import random
print(random.randint(1, 10))

import sys
sys.path.append("C:/my_modules")

import sys
print(sys.version)

import os
print(os.getcwd())

from datetime import datetime
print(datetime.now())

# dir() function
nums = [1, 2, 3]
print(dir(nums))
print(dir())

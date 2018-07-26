#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
  rotated_list = (d[a[1]:] + d[:a[1]])
  return ' '.join(str(rotated_list))

a = [5, 3]
d = [1, 2, 3, 4, 5]
print(rotLeft(a, d))
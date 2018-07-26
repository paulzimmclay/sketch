#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):

  a_count = 0
  b_count = 0

  zipped_score = zip(a, b)
  for pair in zipped_score:
    if pair[0] > pair[1]:
      a_count += 1
    elif pair[0] < pair[1]:
      b_count += 1

  return a_count, b_count
print(compareTriplets([1, 9, 3], [2, 3, 8]))
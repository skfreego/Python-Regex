"""
Task:- Neo has a complex matrix script. The matrix script is a N X M grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).
Input Format:- The first line contains space-separated integers N (rows) and M (columns) respectively.
The next N lines contain the row elements of the matrix script.
Output Format :- Print the decoded matrix script.
"""

"""
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!
"""

# import math
# import os
# import random
import re
# import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
# start
matrix = list(zip(*matrix))

sample = str()

for words in matrix:
    for char in words:
        sample += char

print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', sample))
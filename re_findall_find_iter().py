"""
Task:- You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of S that contains 2 or more vowels.
Input Format:- A single line of input containing string S.
Output Format:- Print the matched substrings in their order of occurrence on separate lines.
If no match is found, print -1.
"""

"""
rabcdeefgyYhFjkIoomnpOeorteeeeet
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

Storage = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', input().strip(), re.IGNORECASE)

if Storage:
    for i in Storage:
        print(i)
else:
    print(-1)
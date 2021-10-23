"""
Task:- You are given a string S.Your task is to find the first occurrence of an alphanumeric character in S(read from left to right) that has consecutive repetitions.
Input Format:-A single line of input containing the string S.
Output Format:-Print the first occurrence of the repeating character. If there are no repeating characters, print -1.
"""

"""
..12345678910111213141516171820212223
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

expression = r"([a-zA-Z0-9])\1+"

m = re.search(expression,input())

if m:
    print(m.group(1))
else:
    print(-1)


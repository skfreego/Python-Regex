"""
Task:- You are given a string S.
Your task is to find the indices of the start and end of string k in S.
Input Format:- The first line contains the string S.
The second line contains the string k.
Output Format:-  Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).
"""
"""
aaadaa
aa
"""



# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S, k = input(), input()
matches = re.finditer(r'(?=(' + k + '))', S)

anymatch = False
for match in matches:
    anymatch = True
    print((match.start(1), match.end(1) - 1))

if anymatch == False:
    print((-1, -1))
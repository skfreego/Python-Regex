"""
Input Format :-
The first line contains an integer N, the number of inputs.
N lines follow, each containing some string.
Output Format :
For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.
"""

"""
2
9587456281
1252478965
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())

for i in range(N):
    number = input()
    if(len(number)==10 and number.isdigit()):
        output = re.findall(r"^[789]\d{9}$",number)
        if(len(output)==1):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
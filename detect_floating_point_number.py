"""
Task:- a valid float number must satisfy all of the following requirements:
Number can start with +,- or . symbol
Number must contain 1 decimal value
Number must have exactly one . symbol
Number must not give any exceptions when converted using float(N)
Input Format:- The first line contains an integer T, the number of test cases.
The next T line(s) contains a string N.
Output Format:- Output True or False for each test case.
"""


"""
4
4.0O0
-1.00
+4.54
SomeRandomStuff
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


class Main:
    def __init__(self):
        self.n = int(input())

        for i in range(self.n):
            self.s = input()
            print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', self.s)))


if __name__ == '__main__':
    obj = Main()

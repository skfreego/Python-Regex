"""
Task:-  The company has assigned you the task of validating all the randomly generated UIDs.
Input Format:- The first line contains an integer T, the number of test cases.
The next T lines contains an employee's UID.
Output Format:- For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.
"""

"""
2
B1CD102354
B1CDEF2354
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for i in range(int(input())):
    N = input().strip()
    if N.isalnum() and len(N) == 10:
        if bool(re.search(r'(.*[A-Z]){2,}',N)) and bool(re.search(r'(.*[0-9]){3,}',N)):
            if re.search(r'.*(.).*\1+.*',N):
                print('Invalid')
            else:
                print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')

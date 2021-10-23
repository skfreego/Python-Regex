"""
Input Format:- The first line of input contains an integer N.
The next N lines contain credit card numbers.
Output Format:- Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.
"""

"""
6
4123456789123456
5123-4567-8912-3456
1234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    S = input().strip()
    pre_match = re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$',S)
    if pre_match:
        processed_string = "".join(pre_match.group(0).split('-'))
        final_match = re.search(r'(\d)\1{3,}',processed_string)
        if final_match:
            print('Invalid')
        else :
            print('Valid')
    else:
        print('Invalid')
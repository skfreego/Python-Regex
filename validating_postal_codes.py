"""
Task:- to provide two regular expressions regex_integer_in_range and regex_alternating_repetitive_digit_pair.
Input Format:- Locked stub code in the editor reads a single string denoting P from stdin and uses provided expression and your regular expressions to validate if P is a valid postal code.
Output Format:- You are not responsible for printing anything to stdout. Locked stub code in the editor does that.

"""

"""
110000
"""

regex_integer_in_range = r"^[1-9][\d]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.

import re
P = input()

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
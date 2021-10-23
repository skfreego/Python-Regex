"""
Task:- You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print True. Otherwise, print False. Try to create a regular expression for a valid Roman numeral.
Input Format:- A single line of input containing a string of Roman characters.
Output Format:-  Output a single line containing True or False according to the instructions above.
"""

"""
CDXXI
"""

thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
digit = '(I[VX]|V?I{0,3})'
regex_pattern = r"%s%s%s%s$" % (thousand, hundred, ten, digit)	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))
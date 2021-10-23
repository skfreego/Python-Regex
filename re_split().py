"""
Task:- to complete the regex_pattern defined below, which will be used to re.split() all of the , and . symbols in s.
It’s guaranteed that every comma and every dot in s is preceeded and followed by a digit.
"""

"""
100,000,000.000
"""


regex_pattern = r"[,.]" 	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

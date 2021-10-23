"""
Task:- You are given N lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.
Input Format:- The first line contains N, the number of code lines.
The next N lines contains CSS Codes.
Output Format:- Output the color codes with '#' symbols on separate lines.
"""

"""
11
#BED
{

    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
}
#Cab
{
    background-color: #ABC;

    border: 2px dashed #fff;

}
"""

import re

T = int(input())
in_css = False
for _ in range(T):
    s = input()
    if '{' in s:
        in_css = True
    elif '}' in s:
        in_css = False
    elif in_css:
        for color in re.findall('#[0-9a-fA-F]{3,6}', s):
            print(color)
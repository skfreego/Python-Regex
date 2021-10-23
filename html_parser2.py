"""
Task:-You are given an HTML code snippet of N lines.
Your task is to print the single-line comments, multi-line comments and the data.
Input Format:- The first line contains integer N, the number of lines in the HTML code snippet.
The next N lines contains HTML code.
Output Format:- Print the single-line comments, multi-line comments and the data in order of their occurrence from top to bottom in the snippet.
Format the answers as explained in the problem statement.
"""

"""
4
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->
"""

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if (len(data.split('\n')) != 1):
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data.replace("\r", "\n"))

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
"""
Task:- You are given an HTML code snippet of N lines.
Your task is to detect and print all the HTML tags, attributes and attribute values.
Input Format :- The first line contains an integer N, the number of lines in the HTML code snippet.
The next N lines contain HTML code.
Output Format :- Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the snippet.
Format your answers as explained in the problem statement.
"""

"""
9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
"""

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print("->", attr, ">", value)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print("->", attr, ">", value)

html = ''
for _ in range(int(input())):
    html += input().rstrip() + '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

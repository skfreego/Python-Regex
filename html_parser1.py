"""
Task:-You are given an HTML code snippet of N lines.
Your task is to print start tags, end tags and empty tags separately.
Input Format:- The first line contains integer N, the number of lines in a HTML code snippet.
The next N lines contain HTML code.
Output Format:- Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the given snippet.
Use proper formatting as explained in the problem statement
"""


"""
2
<html><head><title>HTML Parser - I</title></head>
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>
"""


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ('Start :', tag)
        for ele in attrs:
            print ('->', ele[0], '>', ele[1])

    def handle_endtag(self, tag):
        print ('End   :', tag)

    def handle_startendtag(self, tag, attrs):
        print ('Empty :', tag)
        for ele in attrs:
            print ('->', ele[0], '>', ele[1])

parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())
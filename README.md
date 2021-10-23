#### HackerRank Challenges
### Domain:Python
## Sub Domain: Regex

### re
	A regular expression (or RegEx) specifies a set of strings that matches it.
A regex is a sequence of characters that defines a search pattern, mainly for the use of string pattern matching.
The re.search() expression scans through a string looking for the first location where the regex pattern produces a match.
It either returns a MatchObject instance or returns None if no position in the string matches the pattern.
The re.match() expression only matches at the beginning of the string.
It either returns a MatchObject instance or returns None if the string does not match the pattern.


## Detect_Floating_Point_Number
	You are given a string N.Your task is to verify that N is a floating point number. 
Number can start with +, - or . symbol.
    For example:
    ✔+4.50
    ✔-1.0
    ✔.5
    ✔-.7
    ✔+.4
    ✖ -+4.5
> Number must contain at least decimal value.
For example:
✖ 12.
✔ 12.0 
> Number must have exactly one . symbol.
> Number must not give any exceptions when converted using float(N). 

##### Explanation :-
40O0 :O is not a digit.
- 1.00: is valid.
+4.54: is valid.
SomeRandomStuff: is not a number. 




## Re.Split()
	The re.split() expression splits the string by occurrence of a pattern.
   Code:-
>>> import re
>>> re.split(r"-","+91-011-2711-1111")
['+91', '011', '2711', '1111']


## Group()_Groups()_GroupDict
   ##### group()
	    A group() expression returns one or more subgroups of the match
   Code:- 
>>> import re
>>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
>>> m.group(0)       # The entire match 
'username@hackerrank.com'
>>> m.group(1)       # The first parenthesized subgroup.
'username'
>>> m.group(2)       # The second parenthesized subgroup.
'hackerrank'
>>> m.group(3)       # The third parenthesized subgroup.
'com'
>>> m.group(1,2,3)   # Multiple arguments give us a tuple.
('username', 'hackerrank', 'com')
  
    ##### groups()
	     A groups() expression returns a tuple containing all the subgroups of the match.
    Code:- 
>>> import re
>>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
>>> m.groups()
('username', 'hackerrank', 'com')

    ##### groupdict()
	     A groupdict() expression returns a dictionary containing all the named subgroups of the match, keyed by the subgroup name.
     Code:-
>>> m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
>>> m.groupdict()
{'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}

##### Explanation:-

.. is the first repeating character, but it is not alphanumeric.
1 is the first (from left to right) alphanumeric repeating character of the string in the substring 111.



#### Re.findall() and Re.finditer()
	###### re.findall()
		The expression re.findall() returns all the non-overlapping matches of patterns in a string as a list of strings.
Code:-
>>> import re
>>> re.findall(r'\w','http://www.hackerrank.com/')
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
	
	###### re.finditer()
		The expression re.finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string.
Code:-
>>> import re
>>> re.finditer(r'\w','http://www.hackerrank.com/')
<callable-iterator object at 0x0266C790>
>>> map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

Also, these substrings must lie in between 2 consonants and should contain vowels only.
Note :
Vowels are defined as: AEIOU and aeiou.
Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.

##### Explanation:-
ee is located between consonant d and f.
Ioo is located between consonant k and m.
Oeo is located between consonant p and r.
eeeee is located between consonant t and t. 


#### Re.start() & Re.end()
	##### start() & end()
		These expressions return the indices of the start and end of the substring matched by the group.
Code:-
>>> import re
>>> m = re.search(r'\d+','1234')
>>> m.end()
4
>>> m.start()
0




#### Regex Substitution
The re.sub() tool (sub stands for substitution) evaluates a pattern and, for each valid match, it calls a method (or lambda).
The method is called for all matches and can be used to modify strings in different ways.
The re.sub() method returns the modified string as an output.

Learn more about re.sub().

###### Transformation of Strings
Code:-
import re

#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)
print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9")
Output
1 4 9 16 25 36 49 64 81

####### Replacements in Strings
Code:-
import re
html = """
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie"  value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
"""

print re.sub("(<!--.*?-->)", "", html) #remove comment

Output

<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">

  <param name="quality" value="high"/>
</object>





#### Validating Roman Numerals

#### Validating Phone Numbers
	Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.
	A valid mobile number is a ten digit number starting with a 7, 8 or 9.
Concept :
A valid mobile number is a ten digit number starting with a 7, 8 or 9.
Regular expressions are a key concept in any programming language. A quick explanation with Python examples is available here. You could also go through the link below to read more about regular expressions in Python. 


#### Validating and Parsing Email Addresses
	A valid email address meets the following criteria:

    It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
    The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
    The domain and extension contain only English alphabetical characters.
    The extension is 1, 2, or 3 characters in length.
Given n pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.

Hint : Try using Email.utils() to complete this challenge. For example, this code:

import email.utils
print email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>')
print email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com'))


produces this output:

('DOSHI', 'DOSHI@hackerrank.com')
DOSHI <DOSHI@hackerrank.com>

##### Explanation :
dexter@hotmail.com is a valid email address, so we print the name and email address pair received as input on a new line.
virus!@variable.:p is not a valid email address because the username contains an exclamation point (!) and the extension contains a colon (:). As this email is not valid, we print nothing.


#### Hex Color Code
	CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).
	Specifications of HEX Color Code
	■It must start with a '#' symbol.
	■ It can have 3 or digits 6.
	■ Each digit is in the range of 0 to F. ( 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, B, C, D, E and F).
	■ A - F letters can be lower case. (a, b, c, d, e and f are also valid digits).
CSS Code Pattern

Selector
{
	Property: Value;
}
##### Explanation
#BED and #Cab satisfy the Hex Color Code criteria, but they are used as selectors and not as color codes in the given CSS.
Hence, the valid color codes are:
#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff
Note: There are no comments ( // or /* */) in CSS Code.

#### HTML PARSER 1
	HTML
Hypertext Markup Language is a standard markup language used for creating World Wide Web pages.

Parsing
Parsing is the process of syntactic analysis of a string of symbols. It involves resolving a string into its component parts and describing their syntactic roles.

HTMLParser
An HTMLParser instance is fed HTML data and calls handler methods when start tags, end tags, text, comments, and other markup elements are encountered.

Example (based on the original Python documentation):

Code

from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Found a start tag  :", tag
    def handle_endtag(self, tag):
        print "Found an end tag   :", tag
    def handle_startendtag(self, tag, attrs):
        print "Found an empty tag :", tag

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed("<html><head><title>HTML Parser - I</title></head>"
            +"<body><h1>HackerRank</h1><br /></body></html>")

Output

Found a start tag  : html
Found a start tag  : head
Found a start tag  : title
Found an end tag   : title
Found an end tag   : head
Found a start tag  : body
Found a start tag  : h1
Found an end tag   : h1
Found an empty tag : br
Found an end tag   : body
Found an end tag   : html


.handle_starttag(tag, attrs)

This method is called to handle the start tag of an element. (For example: <div class='marks'>)
The tag argument is the name of the tag converted to lowercase.
The attrs argument is a list of (name, value) pairs containing the attributes found inside the tag’s <> brackets.

.handle_endtag(tag)

This method is called to handle the end tag of an element. (For example: </div>)
The tag argument is the name of the tag converted to lowercase.

.handle_startendtag(tag,attrs)

This method is called to handle the empty tag of an element. (For example: <br />)
The tag argument is the name of the tag converted to lowercase.
The attrs argument is a list of (name, value) pairs containing the attributes found inside the tag’s <> brackets.


#### HTML PARSER 2
	.handle_comment(data)
This method is called when a comment is encountered (e.g. <!--comment-->).
The data argument is the content inside the comment tag:

from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
          print "Comment  :", data


	.handle_data(data)
This method is called to process arbitrary data (e.g. text nodes and the content of <script>...</script> and <style>...</style>).
The data argument is the text content of HTML.

from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        print "Data     :", data



#### Detect HTML Tags,Attributes and Attribute Values
	Tag1
	Tag2
	-> Attribute2[0] > Attribute_value2[0]
	-> Attribute2[1] > Attribute_value2[1]
	-> Attribute2[2] > Attribute_value2[2]
	Tag3
	-> Attribute3[0] > Attribute_value3[0]
The -> symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value.
The > symbol acts as a separator of attributes and attribute values.

If an HTML tag has no attribute then simply print the name of the tag.

Note: Do not detect any HTML tag, attribute or attribute value inside the HTML comment tags (<!-- Comments -->). Comments can be multiline.
All attributes have an attribute value.

##### Explanation :

    head tag: Print the head tag only because it has no attribute.
    title tag: Print the title tag only because it has no attribute.
    object tag: Print the object tag. In the next 4 lines, print the attributes type, data, width and height along with their respective values.
    <!-- Comment --> tag: Don't detect anything inside it.
    param tag: Print the param tag. In the next 2 Lines, print the attributes name along with their respective values.


#### Validating UID
	ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.
A valid UID must follow the rules below:

    It must contain at least 2 uppercase English alphabet characters.
    It must contain at least 3 digits ( 0 - 9).
    It should only contain alphanumeric characters ( a - z, A - Z & 0 - 9).
    No character should repeat.
    There must be exactly 10 characters in a valid UID. 


#### Validating Credit Card Numbers
		 You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. 
You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:
► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.
 
##### Explanation :-

4123456789123456 : Valid
5123-4567-8912-3456 : Valid
61234-576-8912-3456 : Invalid, because the card number is not divided into equal groups of 4.
4123356789123456 : Valid
5133-3367-8912-3456 : Invalid, consecutive digits 3333 is repeating 4 times.
5123 - 4567 - 8912 - 3456 : Invalid, because space ' ' and - are used as separators. 

##### Validating Postal Codes
	A valid postal code P have to fullfil both below requirements:

    P must be a number in the range from 100000 to 999999 inclusive.
    P must not contain more than one alternating repetitive digit pair.

Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.
For example:

121426 # Here, 1 is an alternating repetitive digit.
523563 # Here, NO digit is an alternating repetitive digit.
552523 # Here, both 2 and 5 are alternating repetitive digits.

regex_integer_in_range should match only integers range from 100000 to 999999 inclusive
regex_alternating_repetitive_digit_pair should find alternating repetitive digits pairs in a given string.
Both these regular expressions will be used by the provided code template to check if the input string P is a valid postal code using the following expression: 
	(bool(re.match(regex_integer_in_range, P)) 
	and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)




#### Matrix Script
	To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.
If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability. 
Neo feels that there is no need to use 'if' conditions for decoding. 
Alphanumeric characters consist of: [A-Z, a-z, and 0-9].


##### Explanation :
The decoded script is:

This$#is% Matrix#  %!


Neo replaces the symbols or spaces between two alphanumeric characters with a single space ' ' for better readability.
So, the final decoded script is:

This is Matrix#  %!




##### Innominion_Oct_2021
###### Innomatics Research Labs
####### Internship.








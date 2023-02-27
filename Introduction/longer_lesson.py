import re

# Escape chars
# . ^ $ * + ? { } [ ] \ | ( )     To escape, place a backslash infront of the char

# Raw strings, no escaped chars
print("\tTab")
print(r"\tTab")

pattern = re.compile(r"abc")  # we can now apply this regex pattern to search through texts
test_text = "abcABC hahahaha we will find out abc"
matches = pattern.finditer(test_text)  # returns a list of Match objects that contain the span of what we found. This pairs well with string splicing in Python

for match in matches:
    print(match)   # will print out two matches, (0, 3) and (33, 36) spans

list_of_useful_chars = r"""
Notice that the capitals imply the inverse of their lowercase counterpart

.  - Any character except newline
\d - Digit (0 - 9)
\D - Not a Digit (0 - 9)
\w - Word character (a-z, A-Z, 0-9), think of this as alphanumeric
\W - Not a Word Character 
\s - Whitespace (space, tab, newline)
\S - Not whitespace

\b - word boundary (whitespace or a non alphanumeric char)
\B - Not a word boundary
^ - Beginning of a string
$ - End of a string

| - Either or
( ) - Group
"""


# demonstrating carrots and dollar-signs
pattern = re.compile(r'^Start')   # also re.compile(r'end$') will give us things that end with "end"
sentence = "Start a sentence and then bring it to an end"
matches = pattern.finditer(sentence)
for match in matches:
    print(match)

phone_numbers = """
321-555-4321
123.555.1234    
                """

pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")  # xxx (anything) xxx (anything) xxxx for a phone number
matches = pattern.finditer(phone_numbers)
for match in matches:
    print(match)

# But what if we wanted to only match a dot or a dash? right now we accept everything by using .
pattern = re.compile(r"\d\d\d[-.]\d\d\d[-.]\d\d\d\d")  # xxx (anything) xxx (anything) xxxx for a phone number
matches = pattern.finditer(phone_numbers)
for match in matches:
    print(match)

# When the dash is placed between things, it represents a range of values
pattern = re.compile(r"[1-5]")  # look for 1 through 5
pattern_2 = re.compile(r"[a-zA-Z]")  # look for a lowercase followed by an uppercase
pattern_3 = re.compile(r"[^a-zA-Z]")  # match anything that is not a lowercase or an uppercase letter

# Using Quantifiers to match for more than one character

"""
Quantifiers:

*  -  0 or more
+  -  1 or more
?  -  0 or one
{k}  -  exact number
{k, i}  - exact range (minimum, maximum INCLUSIVE)
"""
# Redo of phone number with quantifiers
pattern = re.compile(r"\d{3}.\d{3}.\d{4}")

# Match titles of people such as Mr.; Mr; Mrs; Mrs.; etc
pattern = re.compile(r"Mr\.?\s[A-Z]\w*")
pattern = re.compile(r"M(r|s|rs)\.?\s[A-Z]\w*")  # the group captures Mr, Ms, Mrs

emails = """
        CoreyMSchafer@gmail.com
        corey.schafer@university.edu
        corey-321-schafer@my-work.net
"""  # we want a regex that fits all three of these email addresses
pattern = re.compile(r"[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)")

urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
        """

pattern = re.compile(r"https?://(www\.)?[a-z]+\.(gov|com)")
pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")

# EXTRACTING PARTICULAR FIELDS

matches = pattern.finditer(urls)
for match in matches:    # we save the GROUPS that we collect in the regex
    print(match.group(0))

# substitutions  -  SLASH OUT the groups you want to extract
subbed_urls = pattern.sub(r"\2\3", urls)
print(subbed_urls)

# the findall method returns a list of the matches but only for the groups
# the match method returns the first match of the regex you are searching for (only works for the start of a string)
# the search method looks in there

# FLAGS
sentence = "Start a sentence and then end it"
pattern = re.compile(r"start", re.IGNORECASE)  # so we don't have to bother with making complex regex



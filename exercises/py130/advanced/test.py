import re

def p1(regex, text):
    print(re.findall(regex,
                     text,
                     flags=re.IGNORECASE | re.MULTILINE))

def p2(regex, text):
    print(re.findall(regex,
                     text,
                     flags=re.IGNORECASE))

text = ("cat\ncot\nCATASTROPHE\nWILDCAUGHT\n" +
        "wildcat\n-GET-\nYacht")

p1(r'\Ac.t', text) # ['cat']
# p1(r'c.t\z', text) # ['cht']
p1(r'c.t\Z', text) # ['cht']

p2(r'\Ac.t', text) # ['cat']
# p2(r'c.t\z', text) # ['cht']
p2(r'c.t\Z', text) # ['cht']
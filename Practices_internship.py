#!/usr/bin/env python
# coding: utf-8

# In[6]:


def func(a, b):
    return b if a == 0 else func(b % a, a)

print(func(30, 75))


# In[7]:


numbers = (4, 7, 19, 2, 89, 45, 72, 22)
sorted_numbers = sorted(numbers)
even = lambda a: a % 2 == 0
even_numbers = filter(even, sorted_numbers)
print(type(even_numbers))


# In[8]:


numbers = (4, 7, 19, 2, 89, 45, 72, 22)
sorted_numbers = sorted(numbers)


# In[10]:


sorted_numbers


# In[15]:


even = lambda a: a % 2 == 0
even_numbers = filter(even, sorted_numbers)
print(type(even_numbers))


# In[14]:


even_numbers


# In[23]:


set1 = {14, 3, 55}
set2 = {82, 49, 62}
set3 = {99,22,17}

print(len(set1+set2+set3))    #In Python, you cannot use the + operator to concatenate sets, as you can with lists or strings. 
                              #Sets do not support the + operator because they are unordered collections of unique elements


# In[19]:


set1 = {14, 3, 55}
set2 = {82, 49, 62}
set3 = {99,22,17}

print(len(set1|set2|set3))       #To combine sets, you should use the union operator (|) or the union() method. 
                                 #Here's how you can get the length of the union of set1, set2, and set3:


# In[24]:


print(4**3 + (7 + 5)**(1 + 1))


# In[25]:


captains = { "Enterprise": "Picard", "Voyager": "Janeway", "Defiant": "Sisko", }


# In[26]:


captains


# In[27]:


captains = { "Enterprise": "Picard", "Voyager": "Janeway", "Defiant": "Sisko", "Discovery": "unknown"}


# In[28]:


captains


# In[29]:


captains["Discovery"].pop()    #wrong syntax --- it will be --- captains.pop("Discovery")


# In[30]:


del captains["Discovery"]


# In[31]:


captains


# In[ ]:


# Regular Expression: 

Regular Expression is a powerful tools for pattern matching and text manipulation, they provide a concise and flexible 
way to search, extract and manipulate string of text based on specific patterns.

However, Regular expression can be complex and tricky to work with, especially for complex pattern. it essential to understand
the syntax and behaviour of regular expression before using them. Python re modules provides a set of functions and methods
to work with regular expression such as search(), match(), findall(), and sub() which make it easier to leverage their
power within your Python code.

Also Regex are instrumental in extracting information from text such as long files, spreadsheet, or even textual documents.
Regex are used in various task such as data preprocessing rule based information minning system, pattern matching, text feature 
engineering, web scraping, data extraction etc.

for example:
Searching and replacing text in files.
Validating text input, such as password and email address.
Rename a hundred files at a time, for example you can change the extension of all files using a RegEx patterns.

functions: Findall--- returns a list containing all matches search --- returns a match objects if there is a match anywhere

in the string split. Returns a list where the string has been split at each match.

substitute --- Replaces one or many matches with a string

Findall --- matching a specific word


findall
search
split
substitute


# In[ ]:


# FindAll


# In[34]:


import re

pattern = 'Data science'
text = 'Data science is a stream and it is a part of AI you can solve many complex problem using Data science'


matches = re.findall(pattern,text)

print(matches)


# In[35]:


len(matches)


# In[ ]:


Extracting digit from a string:

This code finds all sequences of digit within the text it will print ['123', '456'].


# In[36]:


pattern = '\d+'
text = 'There are 123 apple and 456 oranges.'

matches = re.findall(pattern,text)

print(matches)


# In[37]:


# Extracting digits from a lsit of string
price = ['Apple costs Rs 50', 'Rs 60 for each pineapple', 'Rs 150 per watermelon']
for msg in price:
    matches = re.findall('\d+', msg)
    print(matches)


# In[ ]:


# Search


# In[38]:


text = 'india china usa'
x = re.search('india',text)    # it will give 'india' starting index and ending index (0,5)

print(x)


# In[39]:


msges = ['Bananas are not only very delicious pieces of fruit',
        'they are also super healthy.',
        'Eating two bananas a day can do wonders for your health',
        'for example. but did you ever think of sticking a needle into a banana? probably not.',
        'but you should, because it is super handy!']

for msg in msges:
    search = re.search('banana',msg)
    print(search)


# In[40]:


# msg1 = 'This product is really great'
# msg2 = 'This product is really great right'      # starting should be 'This' and ending 'Great'

msg1 = 'This product is really Great'

search = re.search('^This.*Great$', msg1)

print(search)


# In[ ]:


#Split


# In[41]:


# split at each white-space charecter(\s is split by space)
text = 'India is a beautiful country'

x = re.split('\s', text)

print(x)


# In[42]:


# start splitting by position
splitbyposition = 'How is this possible'
x = re.split('\s', splitbyposition, 2)   # split untill index 2

print(x)


# In[ ]:


# Substitute


# In[43]:


sub = 'This function replaces spaces by assigned char'
x = re.sub('\s', '&', sub)

print(x)


# In[44]:


y = 'Rs'
z = r'[oe]'

text = 'This item costs Rs 2500'
 
replacetext = re.sub(y, '$', text)

print(replacetext)


# In[45]:


y = 'Rs'
z = r'[oe]'

text = 'This item costs Rs 2500'

replacetext = re.sub(z, '$', text)

print(replacetext)


# In[46]:


import re


# In[47]:


import regex as re


# In[48]:


print(help(re))


# In[53]:


for i in dir(re):
    print(i,end=",")


# In[54]:


print(len(dir(re)))


# In[ ]:


Meta-character are special character with a special meaning that affect how the Regex around them are interpreted.
meta character dont match themselves, instead they indicate that some rules characters or sign like |,+ or * are special
characters.for Exp caret(^) meta character used to match the RegEx patterns only at the start of the string.

Meta characters also called as operators, sign, or symbols.


# In[ ]:


.(DOT)--- Matches any characters excepts new line characters
^(Caret)--- Matches pattern only at the start of the string(starts with)
$(Dollar)--- Matches patterns at the end of the string(ends with)
*(asterisk)--- Matches 0 or more repetitions of the RegEx (zero or more occurances)
+(Plus)--- Matches 1 or more repetitions of the RegEx(one or more occurances)


# In[ ]:


1.Kbps = kilo bits per second
2.Gbps = Giga bits per second
3.KBps = kilo bytes per second

small 'b'   = unit of memory (Lowest unit of memory)
capital 'B' = Bytes

1B = 8bits


# In[56]:


'data'*3


# In[57]:


'data'+'science'


# In[ ]:


Findall --- the findall() scans the target string from left to right as per the regular expression pattern and returns all 
matches in the order they were found.

it returns None if it falls to locate the occurances of the pattern or such a pattern does not exist in a target string.

syntax: re.findall(pattern, target_string)


# In[ ]:


Matching a specific word


# In[58]:


import re
pattern = 'data Science|Data Science'

text = 'Data Science is a stream and it is a part of AI. you can solve many complex problem using data Science tools and techs'

matches = re.findall(pattern, text)
print(matches)


# In[60]:


import re
pattern = 'Data Science|stream|tools|AI'

text = 'Data Science is a stream and it is a part of AI. you can solve many complex problem using Data Science tools and techs'

matches = re.findall(pattern, text)
print(matches)


# In[ ]:


Extracting digits from a string:
This code finds all sequences of digits within the text, it will print ['123','456'] checking character by character


# In[65]:


pattern = '\d+'

text = '''India 10-1year bond yield hits 28 month low after fed hints at Sep rate cut.
Indian government bond yields fell to a 28-month low after U.S yields following Federal Reserve dovish comments.
The 10-year yield dropped to 6.9045%, its lowest since April 2022. U.S Investor expect rate cuts next year.'''

matches = re.findall(pattern, text)
print(matches)


# In[68]:


pattern = '\d+'
text = 'There are 123 apple and 456 oranges.'

matches = re.findall(pattern,text)

print(matches)


# In[69]:


pattern = '123|456'
text = 'There are 123 apple and 456 oranges.'

matches = re.findall(pattern,text)

print(matches)


# In[70]:


pattern = '[0-9]'
text = 'There are 123 apple and 456 oranges.'

matches = re.findall(pattern,text)

print(matches)


# In[72]:


pattern = '[0-9]+'
text = 'There are 123 apple and 456 oranges.'

matches = re.findall(pattern,text)

print(matches)


# In[74]:


pattern = '[0126]'
text = 'There are 123 apple and 456 oranges.'

matches = re.findall(pattern,text)

print(matches)


# In[75]:


pattern = '\D+'            # "D" it will fetch anything except numbers
text = 'There are 123 apple and 456 oranges. @#'

matches = re.findall(pattern,text)

print(matches)


# In[77]:


# Extracting digits from a lsit of string
price = ['Apple costs Rs 50', 'Rs 60 for each pineapple', 'Rs 120 per watermelon']
for msg in price:
    matches = re.findall('\d+', msg)
    print(matches)


# In[78]:


target_string = 'APJ Abdul Kalam was an Indian aerospace scientist also known as the Missile Man of India #@,'

result = re.findall(r"\w{4}", target_string)

print("Match object:", result)


# In[81]:


target_string = 'APJ Abdul Kalam was an Indian aerospace scientist also known as the Missile123456 12kja_President Man of India trignometry'

result = re.findall(r"\w{11}", target_string)

print("Match object:", result)


# In[82]:


target_string = 'APJ Abdul Kalam was an Indian aerospace scientist also known as the Missilesdgfhg Man of India'

result = re.findall(r"\w{4,6}", target_string)

print("Match object:", result)


# In[86]:


pattern = '[a-z,A-Z,0-9]+'

text = 'My name is Ali and my date of birth is 05 jan 1991' 

matches = re.findall(pattern, text)

print(matches)


# In[116]:


pattern = 'ab*'                             # Matches: 'a' followed by zero or more 'b's
test_strings = 'a ab abb abbb' 


# Matches: 'a' followed by two 'b's
# Matches: 'a' followed by three 'b's
# Does not match: does not start with 'a'
# Does not match: 'a' followed by 'a'
# Does not match: two 'a's

matches = re.findall(pattern,test_strings)

print(matches)


# In[117]:


pattern = 'ab*'                               # Matches: 'a' followed by one or more 'b's
test_strings = 'ab abb abbb'

matches = re.findall(pattern,test_strings)

print(matches)


# In[119]:


pattern = 'ab*'                               # Matches: 'a' followed by zero or one 'b'
test_strings = 'a ab'

matches = re.findall(pattern,test_strings)

print(matches)


# In[127]:


pattern = 'ab*'                               # Matches: 'a' followed by three 'b'
test_strings = 'abbb w re r ewe'

matches = re.findall(pattern,test_strings)

print(matches)


# In[139]:


pattern = 'ab*'                               # Matches: 'a' followed by two to three 'b'   
test_strings = 'abb wed re r abbb'

matches = re.findall(pattern,test_strings)

print(matches)


# In[227]:


pattern =  'a[\w@,]+b'                              # Matches: 'a' followed by anything ending with 'b' 'A[\w@,]+j|A[\w*]+1'
text = 'acb a12_3b Ab ah@,gvjb  ac88fdfb Aweer@b fgghb adr45'

matches = re.findall(pattern, text)

print('match found:',  matches)


# In[211]:


string = 'acb a765b ab ahgfd12@,b'
pattern = 'a[\w@,]+b'

result = re.findall(pattern, string)

print('Match found:', result)


# In[163]:


pattern = '^\w+'                           # it will match the word at begining (a-z, A-Z, 0-9, '_' )

text = 'Hello _999 Today is the most66 Beautiful_day'

matches = re.findall(pattern, text)

print(matches)


# In[164]:


pattern = '\w+$'                           # it will match the word at the end (a-z, A-Z, 0-9, '_' )

text = 'Hello _999 Today is the most66 Beautiful_day'

matches = re.findall(pattern, text)

print(matches)


# In[196]:


pattern = '\w{4}'                            # it will match the word upto 4 character as per condition{4} except special char
target_string = 'what is your Name please Answer123 quickly 1235@.'

matches = re.findall(pattern, target_string)

print(matches)


# In[193]:


pattern = '\w{4}'                            # it will matches anything except any special char like @#$& 
target_string = '01 0132 231875 1458 301 2725@.'

matches = re.findall(pattern, target_string)

print('Match object:',  matches)


# In[177]:


target_string = '01 0132 231875 14587754 301 2725@.'

result = re.findall(r'\w{4}', target_string)



print('match object:', result)


# In[189]:


target_string = 'APJ Abdul Kalam was an Indian aerospace scientist also known as the Missile Man of India #@,'

result = re.findall(r"\w{4}", target_string)

print("Match object:", result)


# In[190]:


target_string = 'APJ Abdul Kalam was an Indian aerospace scientist also known as the Missile123456 12kja_President Man of India trignometry'

result = re.findall(r"\w{11}", target_string)

print("Match object:", result)


# In[191]:


target_string = 'APJ Abdul Kalam was an Indian aerospace scientist also known as the Missilesdgfhg Man of India'

result = re.findall(r"\w{4,6}", target_string)

print("Match object:", result)


# In[232]:


#Extracting string which begins with A and ends with j or string begins with A and ends with 1 from the given string
import re
string = 'AP12ik,@j Abdu_*1 kalam Awas@ an indian aerospace scientist'
pattern = 'A[\w@,]+j|A[\w*]+1'

result = re.findall(pattern, string)

print(result)


# In[235]:


string = 'aP12ik@j Abdu_*1 kalam Awas@ an indian aerospace scientist'
pattern = 'a[\w@]+j|A[\w*]+1'

result = re.findall(pattern, string)

print(result)


# In[240]:


string = """As rescue operations entered the fifth day on Saturday, 12
the toll in kerala's worst natural calamity touched 330 with several people still missing 246 after 
the massive landslides and floods at wayanad."""

pattern = '\d+'

result = re.split(pattern, string,2)   # Max split can give 2 3 4 it will split wherever number matches

print(result)


# In[241]:


string = """As rescue operations entered the fifth day on Saturday, 12
the toll in kerala's worst natural calamity touched 330 with several people still missing 246 after 
the massive landslides and floods at wayanad."""

pattern = '\d+'

result = re.split(pattern, string,3)   # Max split can give 2 3 4 it will split wherever number matches

print(result)


# In[242]:


string = """As rescue operations entered the fifth day on Saturday, 12
the toll in kerala's worst natural calamity touched 330 with several people still missing 246 after 
the massive landslides and floods at wayanad."""

pattern = '\d+'

result = re.split(pattern, string,)   # Max split can give 2 3 4 it will split wherever number matches

print(result)


# In[244]:


string = 'Twelve:12 Eighty nine:89,'
pattern = '\d+'

result = re.split(pattern, string,)

print(result)


# In[245]:


string = 'Twelve:12 Eighty nine:89,'
pattern = '\d+'

result = re.split(pattern, string, 1)

print(result)


# In[249]:


# split at each white space character (\s is split by white space)
text = 'India is a beautiful country Bharat'
x = re.split('\s', text, 3) 

print(x)


# In[247]:


#split by position
split_by_position = 'How is this possible data science position'
x = re.split('\s', split_by_position, 2)

print(x)


# In[251]:


# split string by three delimiters (- , :) Here we are using 3 delimiter (- , :) and using OR(|) operator 
# to combine two or more pattern, Max limit 2 for split the target string.
target_string = '12,45+78,85-17-89:45'
result = re.split(r"-|,|:", target_string, 2)

print(result)


# In[253]:


# Sub(Substitute) : This method is used to find a substring where a regex pattern matches, and then it replaces the matched
# substring with a different string, if the pattern is not found, re.sub() returns the original string.
# syntax = re.sub(pattern, replacement, string, flags)

sub_ = 'This function replaces spaces by assigned char'
x = re.sub('\s', '++', sub_)

print(x)


# In[254]:


y = 'Rs'
text = 'This item costs Rs 2500 and rs 3000'

replaced_text = re.sub(y, '$', text)

print(replaced_text)


# In[255]:


y = 'Rs'
text = 'This item costs Rs 2500 and rs 3000'

replaced_text = re.sub(y, '$', text, flags=re.IGNORECASE)   # flags can ignore cases capital or small

print(replaced_text)


# In[256]:


# Remove all spaces, including single or multiple spaces(pattern to remove '\s+')
target_string = "APJ   Abdul Kalam was      an indian aerospace scientist also known as missile man of india"
res_string = re.sub(r'\s+', "", target_string) 

print(res_string)


# In[259]:


# Removing trailing spaces (pattern to remove ending white space and starting white space)
target_string = "        APJ Abdul Kalam was an indian aerospace scientist also known as missile man of india     "
print(target_string)

res_string = re.sub(r'\s+$|^\s+', "", target_string) 

print(res_string)


# In[265]:


substitute = re.sub(r'[0-9]+', r'*', 'abc00123xyz456_0')

print(substitute)


# In[266]:


#subn() it is similiar to sub() and used to find a substring where a regex pattern matches,
#and then it replaces the matched substring with a different string along with the number of replacements 
# it will count how many time replacements
substitute_and_count = re.subn(r'[0-9]+', r'*', 'abc001 23xyz456_0#05@26')

print(substitute_and_count)


# In[267]:


#Match object : Python re.match method looks for the regex pattern only at the begining of the target string and returns match
#objects, if match found, otherwise it will return None.

#Here the result will be None because no 4 digit number is persent at the begining of the string.

target_string = 'Virat is a cricket player 1988 who was born on November 5, 1988'

result = re.match(r'\d{4}', target_string)

print(result)


# In[269]:


target_string = '2024 Virat is a cricket player 1988 who was born on November 5, 1988'

# match at begining of the string
result = re.match(r'\d{4}', target_string)

print(result)


# In[270]:


target_string = '2024 Virat is a cricket player 1988 who was born on November 5, 1988'
# match at the end
result = re.findall(r'\d{4}', target_string)

print(result)


# In[273]:


target_string = '123abc is an alphanumeric number'

y = re.match("\w+", target_string)

print(y)


# In[272]:


target_string = '123abc is an alphanumeric @ \n # number'

y = re.match(".+", target_string)

print(y)


# In[ ]:


# Search() : Python regex re.search() methods looks for occurances of the regex pattern inside the entire target string 
# and returns the corresponding match objects instance where the match found.


# In[274]:


msges = ['Bananas are not only very delicious pieces of fruit',
        'they are also super healthy.',
        'Eating two bananas a day can do wonders for your health',
        'for example. but did you ever think of sticking a needle into a banana? probably not.',
        'but you should, because it is super handy!']

for msg in msges:
    search = re.search('banana',msg)
    print(search)


# In[275]:


msges = ['20 lakh Bananas are not only very delicious pieces of fruit',
        'they are also super healthy.',
        'Eating two bananas a day can do wonders for your health',
        'for example. 1000 but did you ever think of sticking a needle into a banana? probably not.',
        'but you should, banana because it is super handy!']

for msg in msges:
    search = re.search('\d+|banana', msg)     # it will give result only first instance in the case of search.
    print(search)


# In[279]:


msges = ['20 lakh Bananas are not only very delicious pieces of 5 fruit',
        'they are also super healthy.',
        'Eating two bananas a day can do wonders for your health',
        'for example. 1000 but did you ever think of sticking a needle into a banana? probably not.',
        'but you should, banana because it is super handy!']

for msg in msges:
    search = re.findall('\d+|banana', msg)     # it will give result all the matches in the case of findall.
    print(search)


# In[280]:


msg1 = 'This product is really Great'

search = re.search('^This.*Great$', msg1)

print(search)


# In[ ]:


#Group in RegEx : A group is a part of regex pattern enclosed in parenthesis () meta char, we create a group by placing the 
regex pattern inside the set of parenthesis and capturing groups are a way to treat multiple char as a single unit.
they are created by placing the charecter to be grouped inside a set of parenthesis().

We can use the group() method to extract each group result separately by specifying a group index in between parenthesis().

please note that unlike string indexing start from 0 but group numbering always start at 1.


# In[285]:


target_string = 'Rohit Sharma has scored 43 CENTURIES and 91 HALFCENTURIES in his cricket career'

result = re.search(r"(\b\d+).+(\b[A-Z]+\b).+(\b\d+).+(\b[A-Z]+\b)", target_string) # word char starting with digit one or more

print(result)

print(result.group())   # Extract matching values of all groups

print(result.group(1))  # Extract matching values of group 1

print(result.group(2,3))   # Extract matching values of group 2 and group 3


# In[ ]:


# Regex capture groups multiple times
The search method will return only the first match for each group, but what if a string contains multiple occurances of a 

regex group and you want to extract all matches.

to capture all matches of regex group we need to use finditer() method.

The finditer() methods finds all matches and returns an iterator yielding match object matching the regex pattern.

don't use findall() method

So always use finditer() if you wanted to capture all matches to the group. 


# In[286]:


target_string = 'Rohit Sharma has scored 43 CENTURIES and 91 HALFCENTURIES in his cricket career'

pattern = re.compile(r"(\b\d+\b).(\b[A-Z]+\b)")

#find all matches to groups
for match1 in pattern.finditer(target_string):
    print(match1)
    print(match1.group())
    
    #Extract number
    #print(match1.group(2))


# In[287]:


# remove all consecutive Duplicates words if any word between duplicates word it will not removed.

string_1 = "Ram went went to to his home"

regex = r'\b(\w+)(?:\W+\1\b)+'

x = re.sub(regex, r'\1', string_1)

print(x)


# In[ ]:


The details of the above regular expression can be understood as:
    
"\b" : A word boundary Boundaries are needed for special cases for example: "My thesis is great", is won't be matched twice.
        
"\w+" : A word charecter: [a-zA-Z_0-9]
        
"\W+" : A non word character. [^\w]
    
"\1"  : Matches whatever was matched in the first group of parentheses. which in this case is the (\w+)
    
"+"   : Matches whatever it's placed after 1 or more times


# In[290]:


with open("/content/url_related.txt") as file:
    for line in file:
        urls = re.findall('(https?://(?:[-\w.]|(?:%[\da-zA-Z0-9]{2}))+', line)
        
        print(urls)


# In[289]:


with open("/content/url_related.txt") as file:
    for line in file:
        urls = re.findall('(https?://[^\s]+)', line)
        
        print(urls)


# In[291]:


import pandas as pd
import regex as re


# In[ ]:


Pandas Series.str.contains() function is used to test if pattern or regex is contained within a string of a series(column)
or index. The functions return boolean (True/False) series(column) or index based on whether a given pattern or regex is 
contained within a string of a series or index.

syntax: Series.str.contains(pat,case=True, flags=0, na=nan, regex=True)
    
Parameter:
    
pat: character sequence or regular expression
    
case: if True, case sensitive.
    
flags: flags to pass through to the re module, re.IGNORECASE

NA: Fill value for missing values
    
regex: if True assumes the pat is a regular expression.


# In[292]:


df = pd.DataFrame({'City':['New york', 'Parague', 'new Delhi', 'Venice', 'new Orleans'],
                  'Event':['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'],
                  'Cost': [10000, 5000, 15000, 2000, 12000]})

df


# In[293]:


df['City'].str.contains('^N.*', case=False)


# In[294]:


df['City'].str.contains('^N.*', case=True)


# In[295]:


df[df['City'].str.contains('^N.*', case=False)==True]


# In[303]:


df = pd.read_csv('titanic_train')

df.head()


# In[305]:


df.drop(['Unnamed: 0'], axis = 1, inplace = True)


# In[306]:


df.head()


# In[ ]:


# 1.Filtering a DataFrame s.str.contains(pattern)


# In[308]:


pattern = r'^W.*n'         # start with capital W and followed by anything but conataining 'n'

mask = df['Name'].str.contains(pattern)

df[mask].head(10)


# In[309]:


pattern = r'C\.?A\.?'

mask = df['Ticket'].str.contains(pattern)

df[mask].head(10)


# In[ ]:


# 2. Pandas Series.str.extract() : function is used to extract capture groups in the regex pattern as columns in a 
# DataFrame. for each subject string in the series, extract groups from the first match of regular expression.

syntax: Series.str.extract(pat, flags=0, expand=True)
    
expand = if true, return dataframe with one column per capture group


# In[310]:


df['Name'].sample(5)


# In[ ]:


extract all unique titles such as Mr, Mrs, Miss from passenger name


# In[313]:


pattern = '\s(\w+)\.'
all_ts = df['Name'].str.extract(pattern, expand= False)

unique_ts = all_ts.value_counts()

unique_ts


# In[314]:


df['Name'].head(10)


# In[ ]:


# 3. Pandas Series.str.replace() : Function is used to replace each occurance of pattern/regex in the series/index

syntax: Series.str.replace(pat,repl,n=1, case=None, flags=0, regex=True)
    
n: The maximum number of replacements to make. by default there is no limit as to how many replacements are made.
    
replacing value in a column - s.str.replace(pattern, repl)

Replace all the title with capital letters.


# In[315]:


pattern = r'\s(\w+)\.'
df['Name'].str.replace(pattern, lambda m:m.group().upper(), regex= True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





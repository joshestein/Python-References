# A cheat sheet for regex
# ***********************
# Steps:
# import rex
# Create an object using re.compile() to create the regex pattern. Use a raw string to simplify your life.
# Pass the string into the object's search() method, which returns a 'Match' object
# Alternatively, use findall() to find all matches
# Call the Match object's group() to find matched text

"""
\d -- any digit from 0-9
\D -- not a digit from 0-9
\w -- any letter, digit or underscore
\W -- not a ltter, digit or underscore
\s -- any space, tab or newline
\S -- any character that is not a spacei, tab or newline
() -- create a sub-group
{x} -- repeate preceding regex instruction x number of times. \d\d\d == \d{3}
{3,5} -- matches at least 3 and at most 5 of the preceding group
{3,5}? -- nongreedy match of the preceding group
| -- OR
? -- optional match
* -- zero or more matches
+ -- one or more matches
^spam -- string must begin with spam
spam$ -- string must end with spam
[] -- custom character class. [aeiou] matches all lowercase vowels.
[^] -- not the custom character class. [^abc] matches everything that is not a, b or c.
. -- wildcard (any character except newline)
.* -- anything

"""
import re
import unittest


# ---------------------------------------------------------------
# Basic matching and groups
# ---------------------------------------------------------------

# Use r'' to create a raw string
# Assume phone number = string of 3 digits, a hyphen, string of 3 more digits, another hyphen, 4 digits
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Use curly praces to repeat a pattern a specific number of times. This is equivalent to the above expression.
phone_num_regex_2 = re.compile(r'\d{3}-\d{3}-\d{4}')


# If a pattern is found, the search() method returns a Match object.
# Otherwise the search() method returns None
mo_found = phone_num_regex.search('Number is 021-444-1234')
mo_not_found = phone_num_regex.search('Number is missing')

print("Number is '021-444-1234'. Match object:")
print(mo_found)
print("Number is missing. Match object:")
print(mo_not_found)

# To find the match, use mo.group()
print("Number found: " + mo_found.group())

# Groups can be used to find sub-patterns within bigger patterns.
# To create groups, use parentheses.
# group(0) is the entire matched text. group(1) is the first group, group(2) the second, etc.
# For example, consider finding the area codes:
area_code_regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = area_code_regex.search("Number is 021-444-1234")

print("group(1): " + mo.group(1))
print("group(2): "+ mo.group(2))
print("group() == group(0): " + mo.group())

# If you want to search for parentheses, you need to escape them. Consider a phone number of the form (xxx) xxx-xxxx:

parentheses_regex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
mo = parentheses_regex.search("Number is (021) 444-1234")
print(mo)
print("Number is (021) 444-1234")
print(mo.group())

# To get all the groups, use groups()

print("Groups:")
print(mo.groups())

# ---------------------------------------------------------------
# Using the pipe(|) = OR
# This allows you to match multiple strings
# If both occurrunces occur, the first occurrence is returned
# ---------------------------------------------------------------

pipe_regex = re.compile(r'alpha|beta')
mo_1 = pipe_regex.search("alpha")
mo_2 = pipe_regex.search("beta")
mo_3 = pipe_regex.search("alpha and beta")

print()
print("| OR matching")
print("r'alpha|beta'")
print("Search: 'alpha'")
print(mo_1.group())

print()
print("Search: 'beta'")
print(mo_2.group())

print()
print("Search: 'alpha and beta'. Note first occurrence.")
print(mo_3.group())

# The pipe can be used to match one of several patterns.
# Consider matching 'Selfish', 'Self-love', 'Self-absorbed', 'Self-esteem'
# NOTE: this seems to not be working in Python 3.6

self_regex = re.compile(r'self(|ish|love|absorbed|esteem)')
mo = self_regex.search('selflove is cool')
print()
print("r'self(|ish|love|absorbed|esteem)'")
print("Search: 'selflove'")
print(mo.group())
print(mo.group(1))


# ---------------------------------------------------------------
# ? is for optional matching
# ---------------------------------------------------------------

optional_regex = re.compile(r'star(wars)?')
print()
print("? optional matching")
print("r'star(wars)?'")
print("A star is pretty")

mo_1 = optional_regex.search("A star is pretty")
mo_2 = optional_regex.search("starwars is awesome")

print(mo_1.group())
print("starwars is awesome")
print(mo_2.group())
print("group(1): " + mo_2.group(1))

# Consider an optional area-code:

optional_area_code_regex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
print()
print(r'(\d{3}-)?\d{3}-\d{4}')

mo_1 = optional_area_code_regex.search("Number is 021-444-1234")
mo_2 = optional_area_code_regex.search("Number is 444-1234")

print("Number is 021-444-1234")
print(mo_1.group())
print("group(1): " + mo_1.group(1))
print("Number is 444-1234")
print(mo_2.group())

# ---------------------------------------------------------------
# *  is for zero or more matches
# ---------------------------------------------------------------

bat_regex = re.compile(r'Bat(wo)*man')
print()
print("* for zero or more matches")
print("r'Bat(wo)*man'")

mo_1 = bat_regex.search('Batman')
mo_2 = bat_regex.search('Batwoman')
mo_3 = bat_regex.search('Batwowowoman')

print('Batman')
print(mo_1.group())
print('Batwoman')
print(mo_2.group())
print('Batwowowoman')
print(mo_3.group())


# ---------------------------------------------------------------
# +  is for one or more matches
# ---------------------------------------------------------------

one_or_more_regex = re.compile(r'(man)+')
mo_1 = one_or_more_regex.search("A man a plan a canal")
mo_2 = one_or_more_regex.search("manmanman that sucks")
mo_3 = one_or_more_regex.search("Nothing here buddy")

print()
print("+ for one or more")
print("r'(man)+'")
print("A man a plan")
print(mo_1.group())
print("manmanman that sucks")
print(mo_2.group())
print("Nothing here buddy")
print(mo_3)

# ---------------------------------------------------------------
# {} for repetitions
# ---------------------------------------------------------------

print()
print("Curly braces ({}) are your friend")

print("\nExact number")
print("r'(foo){3}'")
exact_number = re.compile(r'(foo){3}')
mo_1 = exact_number.search("No such thing as foofoofoo")
mo_2 = exact_number.search("Alas, foofoo is not enough")
print("No such thing as foofoofoo")
print(mo_1.group())
print("Alas, foofoo is not enough")
print(mo_2)

# You can specify a range {n,m}
# You can also specify a range {n, }, meaning n or more occurrences
# Likewise, you can specify {, m}, meaning 0 to m occurrences
some_range = re.compile(r'(bar){2,4}')
mo_1 = some_range.search("Let's go to the barbar")
mo_2 = some_range.search("Nah, let's rather do the barbarbar")
mo_3 = some_range.search("You guys are idiots. Let's go to the bar.")

print("\nA range")
print("r'(bar){2,4}'")
print("Let's go to the barbar")
print(mo_1.group())
print("Nah, let's rather do the barbarbar")
print(mo_2.group())
print("You guys are idiots. Let's go to the bar.")
print(mo_3)

# By default, Python is gready, meaning it searches for the longest match
print("\nGreedy mofo")
greedy = re.compile(r'(long){2,4}')
mo_1 = greedy.search("A longlonglonglong lost fucking time ago there was a longlong boy")

print("r'(long){2,4}'")
print("A longlonglonglong lost fucking time ago there was a longlong boy")
print(mo_1.group())

# You can change to non-greedy by using the question mark (?) after the range
print("\nNon greedy")
non_greedy = re.compile(r'(long){2,4}?')
mo_1 = non_greedy.search("A longlonglonglong lost fucking time ago there was a longlong boy")

print("r'(long){2,4}?'")
print("A longlonglonglong lost fucking time ago there was a longlong boy")
print(mo_1.group())


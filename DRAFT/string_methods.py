# a = "Hello World, 124aBc"

# # title() method capitalizes the first letter of each word in the string & 
# # the letter after a number, while converting all other letters to lowercase.

# b = a.title()
# print(b)  # Output: "Hello World, 124Abc"


# # capitalize() method capitalizes only the first letter of the entire string,
# # converting all other letters to lowercase.
# c = a.capitalize()
# print(c)  # Output: "Hello world, 124abc"

# # upper() method converts all letters in the string to uppercase.
# d = a.upper()
# print(d)  # Output: "HELLO WORLD, 124ABC"

# # lower() method converts all letters in the string to lowercase.
# e = a.lower()
# print(e)  # Output: "hello world, 124abc"

# # swapcase() method swaps the case of each letter in the string:
# f = a.swapcase()
# print(f)  # Output: "hELLO wORLD, 124AbC"

# # strip() method removes leading and trailing whitespace from the string.
# g = "   Hello World   "
# print(g.strip())  # Output: "Hello World"
# # lstrip() method removes leading whitespace from the string.
# print(g.lstrip())  # Output: "Hello World   "
# # rstrip() method removes trailing whitespace from the string.
# print(g.rstrip())  # Output: "   Hello World"

# # strip() method can also remove specified characters from both ends of the string.
# h = "###Hello World###"
# print(h.strip("#"))  # Output: "Hello World"
# # lstrip() method can also remove specified characters from the start of the string.
# print(h.lstrip("#"))  # Output: "Hello World###"
# # rstrip() method can also remove specified characters from the end of the string.
# print(h.rstrip("#"))  # Output: "###Hello World"

# # replace() method replaces occurrences of a specified substring with another substring.
i = "Hello World, Welcome to the World of Python"
# j = i.replace("World", "Universe")
# print(j)  # Output: "Hello Universe, Welcome to the Universe of Python"

# # find() method returns the lowest index of the substring if found in the string.
# # If not found, it returns -1.
# k = i.find("World")
# print(k)  # Output: 6
# l = i.find("Java")
# print(l)  # Output: -1
# # rfind() method returns the highest index of the substring if found in the string.
# # If not found, it returns -1.
# m = i.rfind("World")
# print(m)  # Output: 30
# n = i.rfind("Java")
# print(n)  # Output: -1

# # index() method returns the lowest index of the substring if found in the string.
# # If not found, it raises a ValueError.
# o = i.index("World")
# print(o)  # Output: 6
# # rindex() method returns the highest index of the substring if found in the string.
# p = i.rindex("World")
# print(p)  # Output: 30

# # count() method returns the number of occurrences of a substring in the string.
# q = i.count("World")
# print(q)  # Output: 2

# # split() method splits the string into a list of substrings based on a specified delimiter.
r = i.split(", ")
print(r)  # Output: ['Hello World', 'Welcome to the World of Python']

# # rsplit() method splits the string into a list of substrings from the right based on a specified delimiter.
rs = i.rsplit(" ", 3)
print(rs)  # Output: ['Hello World, Welcome to the', 'World', 'of', 'Python']

# # join() method joins elements of an iterable (like a list) into a single string,
# # with a specified separator.
# s = ", ".join(r)
# print(s)  # Output: "Hello World, Welcome to the World of Python"   

# # format() method formats specified values into a string.
# t = "Hello, {}. Welcome to {}!"
# formatted_string = t.format("Alice", "Wonderland")
# print(formatted_string)  # Output: "Hello, Alice. Welcome to Wonderland!"

# # f-strings (formatted string literals) provide a way to embed expressions inside string literals.
# name = "Bob"
# age = 30
# f_string = f"My name is {name} and I am {age} years old."
# print(f_string)  # Output: "My name is Bob and I am 30 years old."

# # zfill() method pads the string on the left with zeros to fill a specified width.
# number = "42"
# padded_number = number.zfill(5)
# print(padded_number)  # Output: "00042"

# # ljust() method left-justifies the string in a field of specified width.
# left_justified = number.ljust(5, '0')
# print(left_justified)  # Output: "42000"

# # rjust() method right-justifies the string in a field of specified width.
# right_justified = number.rjust(5, '0')
# print(right_justified)  # Output: "00042"

# # center() method centers the string in a field of specified width.
# centered = number.center(5, '0')
# print(centered)  # Output: "00420"

# # isalpha() method checks if all characters in the string are alphabetic.
# alpha_string = "HelloWorld"
# print(alpha_string.isalpha())  # Output: True
# beta_string = "Hello World"
# print(beta_string.isalpha())  # Output: False

# # isdigit() method checks if all characters in the string are digits.
# digit_string = "12345"
# print(digit_string.isdigit())  # Output: True
# gamma_string = "123a45"
# print(gamma_string.isdigit())  # Output: False

# # isalnum() method checks if all characters in the string are alphanumeric.
# alnum_string = "Hello123"
# print(alnum_string.isalnum())  # Output: True
# delta_string = "Hello 123"
# print(delta_string.isalnum())  # Output: False

# # isnumeric() method checks if all characters in the string are numeric.
# numeric_string = "12345"
# print(numeric_string.isnumeric())  # Output: True
# nonnumeric_string = "123a45"
# print(nonnumeric_string.isnumeric())  # Output: False

# # islower() method checks if all cased characters in the string are lowercase.
# lower_string = "hello world"
# print(lower_string.islower())  # Output: True
# upper_string = "Hello World"
# print(upper_string.islower())  # Output: False

# # isupper() method checks if all cased characters in the string are uppercase.
# upper_string2 = "HELLO WORLD"
# print(upper_string2.isupper())  # Output: True
# lower_string2 = "Hello World"
# print(lower_string2.isupper())  # Output: False

# # islower() method checks if the string is in lowercase.
# lower_string3 = "hello world"
# print(lower_string3.islower())  # Output: True
# mixed_string = "Hello World"
# print(mixed_string.islower())  # Output: False

# # istitle() method checks if the string is in title case.
# title_string = "Hello World"
# print(title_string.istitle())  # Output: True
# not_title_string = "Hello world"
# print(not_title_string.istitle())  # Output: False

# # endswith() method checks if the string ends with a specified suffix.
# filename = "document.txt"
# print(filename.endswith(".txt"))  # Output: True
# print(filename.endswith(".pdf"))  # Output: False

# # startswith() method checks if the string starts with a specified prefix.
# print(filename.startswith("doc"))  # Output: True
# print(filename.startswith("docu"))  # Output: True
# print(filename.startswith("documentary"))  # Output: False

# # splitlines() method splits the string at line breaks and returns a list of lines.
# multiline_string = "Hello World\nWelcome to Python\nEnjoy coding!"
# print(multiline_string.splitlines())  # Output: ['Hello World', 'Welcome to Python', 'Enjoy coding!']
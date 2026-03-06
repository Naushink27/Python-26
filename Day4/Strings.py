# Basic Python String Program (Important Methods)

text = "Hello Python World"

# 1. Length of string
print("Length:", len(text))   # counts characters

# 2. Convert case
print(text.upper())           # all uppercase
print(text.lower())           # all lowercase
print(text.title())           # first letter capital

# 3. Check start and end
print(text.startswith("Hello"))  # True if string starts with Hello
print(text.endswith("World"))    # True if string ends with World

# 4. Find position
print(text.find("Python"))    # index of word, -1 if not found

# 5. Replace text
print(text.replace("Python", "Java"))  # replace substring

# 6. Split string
words = text.split(" ")       # split by space
print(words)

# 7. Join list into string
new_text = "-".join(words)    # join using -
print(new_text)

# 8. Remove spaces
s = "   coding   "
print(s.strip())              # remove spaces both sides
print(s.lstrip())             # remove left spaces
print(s.rstrip())             # remove right spaces

# 9. Check string type
print("123".isdigit())        # True if all digits
print("hello".isalpha())      # True if only letters
print("hello123".isalnum())   # True if letters+numbers

# 10. Count occurrences
print(text.count("o"))        # how many times 'o' appears

# 11. Access characters
print(text[0])                # first character
print(text[-1])               # last character

# 12. Slicing
print(text[0:5])              # Hello
print(text[6:12])             # Python
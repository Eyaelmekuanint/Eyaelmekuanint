my_string = "Hello, world!"

print("original string:", my_string)
l=len(my_string)
print("length:",l)
print("Uppercase:", my_string.upper())
print("Lowercae:",my_string.lower())
another_substring = "this is python"
m = my_string +" "+ another_substring

print("concatenated string:" ,m)

print("occurrence of 'l'",my_string.count("l"))

substring = "Hello"

if my_string.startswith(substring):
    print("starts with 'Hello':", "true")
else:
    print("false")

print("Replaced String:",my_string.replace('world', 'python'))

print("Word",my_string.split())
    

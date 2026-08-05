"""
File handling example: How do I read from and write to a text file safely?
"""

filename = "sample.txt"

# Write text to a file
with open(filename, "w", encoding="utf-8") as file:
    file.write("Hello, AI Solution Architect learning journey!\n")
    file.write("This file demonstrates file handling in Python.\n")

# Read text from the file
with open(filename, "r", encoding="utf-8") as file:
    content = file.read()

print("File content:")
print(content)

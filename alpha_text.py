#!/usr/bin/python3
"""
alpha_text.py
removes all non-alphabetic characters from a file, preserving whitespace.
"""

input_file_path = input("Input name of file you want to clean\n -->  ")
name, extension = input_file_path.split('.')
output_file_path = name + "_alphabetic." + extension

with open(input_file_path) as input_file:
  with open(output_file_path, 'w') as output_file:
    for char in input_file.read():
      if char.isalpha() or char.isspace():
        output_file.write(char)


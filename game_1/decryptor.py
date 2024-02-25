#!/usr/bin/python3
from matrix_utils import *
"""
matrix_utils.py
- bytes_to_matrix(_bytes): Converts a bytes object of length 16 into a 4x4 matrix
- matrix_to_bytes(mat): Converts a 4x4 matrix back into a bytes object
- mat_mul(a, b): Multiplies two 4x4 matrices (a and b) together and returns the result
- mat_inv(mat): Calculates the inverse of a 4x4 matrix
- mat_det(mat): Calculates the determinant of any size matrix
"""
from crypto_utils import *
"""
crypto_utils.py
- get_file_path(default)
- get_password(default)
- stretch_key(key)
- get_text(textfile_path)
- write_buffer_with_name(buffer, name, ext): just give it the path of the input file and it will take care of the rest
"""

def main():
  text_path = get_file_path(default='test_enc.txt')
  text = get_text(text_path)
  i = text.index('#')
  padding = int.from_bytes(text[:i])
  text = text[i+1:]

  key = get_password(defualt='pass')
  key = stretch_key(key)
  key_mat = bytes_to_matrix(key)
  inv_key_mat = mat_inv(key_mat)
  
  decrypted = bytes(0)
  
  # iterate for each 16 byte block in text
  for i in range(0, len(text), 16):
    block = text[i:i+16]
    text_mat = bytes_to_matrix(block)
    for i in range(0):
      text_mat = mat_mul(inv_key_mat, text_mat)
    decrypted += matrix_to_bytes(text_mat)
  
  write_buffer_with_name(decrypted, text_path, 'decrypted')

if __name__ == '__main__':
  main()





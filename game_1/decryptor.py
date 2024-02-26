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
  PASSES = get_passes(1)

  text_path = get_file_path(default='encrypted_test.txt')
  text = get_text(text_path)
  padding = text[0]
  text = text[1:]

  key = get_password(default='pass')
  key = stretch_key(key)
  key_mat = bytes_to_matrix(key)
  
  decrypted = bytes(0)
  # iterate for each 32 byte block in text
  for i in range(0, len(text), 32):
    block = text[i:i+32]
    text_mat = bytes_to_matrix(block, 2)
    for i in range(PASSES):
      text_mat = undo_mat_mul(key_mat, text_mat)
    dec_mat = matrix_to_bytes(text_mat)
    decrypted += dec_mat
  
  decrypted = decrypted[:-padding]
  write_buffer_with_name(decrypted, text_path, 'decrypted')

if __name__ == '__main__':
  main()





#!/usr/bin/python3
from matrix_utils import *
from crypto_utils import *

def main():
  ### TAKING INPUTS ###
  key = get_password(default='pass')
  key = stretch_key(key)
  key_mat = bytes_to_matrix(key)
  
  text_path = get_file_path(default='encrypted_test.txt')
  text = get_text(text_path)
  padding = text[0]
  PASSES = text[1]
  text = text[2:]

  decrypted = bytes(0)

  # see documentation for explanation
  byte_size = ceil((math_log2(255**(PASSES+1))*len(key)**PASSES)/8)
  BLOCK_SIZE = len(key)**2 * byte_size

  #### PERFORMING DECRYPTION ###
  for i in range(0, len(text), BLOCK_SIZE):
    block = text[i:i+BLOCK_SIZE]
    text_mat = bytes_to_matrix(block, byte_size)
    for i in range(PASSES):
      text_mat = undo_mat_mul(key_mat, text_mat)
    dec_block = matrix_to_bytes(text_mat, 1)
    decrypted += dec_block
  
  decrypted = decrypted[:-padding]
  write_buffer_with_name(decrypted, text_path, 'decrypted')

if __name__ == '__main__':
  main()





#!/usr/bin/python3
from matrix_utils import *
from crypto_utils import *

def main():
  ### TAKING INPUTS ###
  PASSES = get_passes(1)

  key = get_password(default='pass')
  BLOCK_SIZE = len(key) ** 2
  key = stretch_key(key)
  key_mat = bytes_to_matrix(key)
  if mat_det(key_mat) == 0:
    print("invalid passphrase, determinant zero")
    exit()

  text_path = get_file_path(default='test.txt')
  text = get_text(text_path)
  padding = (BLOCK_SIZE - len(text) % BLOCK_SIZE) % BLOCK_SIZE
  text += bytes(padding)
  encrypted = bytes()
  encrypted += padding.to_bytes()
  encrypted += PASSES.to_bytes()
  
  # see documentation for explanation
  byte_size = ceil((math_log2(255**(PASSES+1))*len(key)**PASSES)/8)

  ### PERFORMING ENCRYPTION ###
  for i in range(0, len(text), BLOCK_SIZE):
    block = text[i:i+BLOCK_SIZE]
    text_mat = bytes_to_matrix(block, 1)
    for i in range(PASSES):
      text_mat = mat_mul(key_mat, text_mat)
    enc_block = matrix_to_bytes(text_mat, byte_size)
    encrypted += enc_block
  
  write_buffer_with_name(encrypted, text_path, 'encrypted')
  
if __name__ == '__main__':
  main()





#!/usr/bin/python3
def bytes_to_matrix(_bytes):
  matrix = []
  for i in range(4):
    matrix.append([])
    for j in range(4):
      matrix[i].append(_bytes[i*4 + j])
  return matrix

def matrix_to_bytes(mat):
  str_bytes = '0b'
  for row in mat:
    for value in row:
      str_bytes += bin(value)[2:]
  return int(str_bytes, 2).to_bytes(16 * 8)

def mat_mul(a, b):
  result = []
  for i in range(4):
    result.append([])
    for j in range(4):
      result[i].append(0)
      for k in range(4):
        result[i][j] += a[i][k] + b[k][j]
  return result

def main():

  ################## Take Input ##################
  key = '00000000000000000000000000000000'
  key_length = len(key)
  TEXT_PATH = input("Input name of file to encrypt\n --> ")
  TEXT_PATH = TEXT_PATH if TEXT_PATH else "test.txt"
  print(f"len(key): {len(key)}, int(key): {int(key)}")
  print(f"plaintext file: {TEXT_PATH}")

  if input("continue? y|N  ") == 'y':
    pass
  else:
    print("exiting program")
    exit()
  
  ################ Key Stretching ################
  """
  key stretching algorithm is as follows:
  split the 32 bit key into 4 separate bytes a, b, c, and d
  create the new key by concatonating the bytes as follows: aaaabbbbccccdddd
  thus you will be left with a key 4 times the original length
  resulting key is 16 bytes
  """
  key = int(key, 2)
  key = key.to_bytes(32)
  a = key[0:8]
  b = key[8:16]
  c = key[16:24]
  d = key[24:32]
  key = a*4 + b*4 + c*4 + d*4

  ############## Open and Read File ##############
  with open(TEXT_PATH, 'rb') as file:
    plaintext = file.read()
    padding = 16 - len(plaintext) % 16
    plaintext += bytes(padding)
    encrypted = f"p{padding}ks{len(key)}".encode('utf-8')
  
  ######### Iterate For Each 16 Byte Block #########
  key_mat = bytes_to_matrix(key)
  for i in range(0, len(plaintext), 16):
    block = plaintext[i:i+16]
    text_mat = bytes_to_matrix(block)

    ######### Perform Matrix Multiplication 10 times  #########
    for i in range(0):
      text_mat = mat_mul(key_mat, text_mat)
    
    ######### Append Result to Encrypted Data #########
    encrypted += matrix_to_bytes(text_mat)
  

  ###########  Open and Write Encrypted File  ###########
  name, *ext = TEXT_PATH.split('.')
  ext = '.' + ext[0] if ext else ''
  output_path = name + "_decrypted" + ext
  from pathlib import Path
  i = 1
  while Path(output_path).is_file():
    output_path = name + f"_encrypted_{i}" + ext
    i += 1
  
  with open(output_path, 'wb') as file:
    file.write(encrypted)
  
  print("------------------------------")
  print("encryption finished :D")

if __name__ == '__main__':
  main()







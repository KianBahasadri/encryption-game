#!/usr/bin/python3
class Byte(bytes):
  """
  Passing an int to Byte() will return a valid Byte object
  """
  def __new__(cls, source):
    length = 8
    if isinstance(source, int):
      return super().__new__(cls, source.to_bytes(length))
    elif isinstance(source, bytes):
      return super().__new__(cls, source)
    else:
      raise TypeError("Byte can be initialized with int or bytes only")

  def __add__(self, other):
    if isinstance(other, bytes): 
      return Byte(int.from_bytes(self) + int.from_bytes(other))
    elif isinstance(other, int):
      return Byte(int.from_bytes(self) + other)


def main():

  ################## Take Input ##################
  KEY = '00000000000000000000000000000000'
  KEY_LENGTH = len(KEY)
  TEXT_PATH = "plaintext.txt"
  print(f"len(KEY): {len(KEY)}, int(KEY): {int(KEY)}")
  print(f"plaintext file: {TEXT_PATH}")

  if input("continue? y|N") == 'y':
    pass
  else:
    exit()

  ############## Open and Read File ##############
  with open(TEXT_PATH, 'rb') as file:
    TEXT = file.read()
    padding = 32 - len(plaintext) % 32
    plaintext += ' ' * padding
    encrypted = f"p{padding}ks{len(KEY)}"

  ######### Perform Encryption Per Block #########
  for i in range(0, len(plaintext), 32):
    block = plaintext[i:i+32]
    current_matrix = []
    for j in range(0, 32, 8):
      current_matrix.append(block[j:j+8])
    
    


if __name__ == '__main__':
  main()







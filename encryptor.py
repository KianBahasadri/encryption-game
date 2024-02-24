#!/usr/bin/python3
class Byte(bytes):
  """
  Passing an int to Byte() will return a valid Byte object
  """
  def __init__(self, value):
    if type(value) == int:
      self = Byte(value.to_bytes())
    if type(value) == bytes:
      self.

  def __add__(self, other):
    return Byte(int.from_bytes(self) + int.from_bytes(other))


def main():
  KEY = '00000000000000000000000000000000'
  KEY_LENGTH = len(KEY)
  TEXT_PATH = "plaintext.txt"
  print(f"len(KEY): {len(KEY)}, int(KEY): {int(KEY)}")
  print(f"plaintext file: {TEXT_PATH}")

  if input("continue? y|N") == 'y':
    pass
  else:
    exit()

  with open(TEXT_PATH, 'rb') as file:
    TEXT = file.read()
    padding = 32 - len(plaintext) % 32
    plaintext += ' ' * padding
    encrypted = f"p{padding}ks{len(KEY)}"

  for i in range(0, len(plaintext), 32):
    block1 = plaintext[i:i+8]

if __name__ == '__main__':
  main()


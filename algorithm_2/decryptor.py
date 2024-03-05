#!/usr/bin/python3

def get_file_path(default):
  from pathlib import Path

  path = input(f"File to encrypt (Default: {default})\n--> ")
  path = path if path else default

  if not Path(path).is_file():
    print("file does not exist, exiting")

  return path

def get_password(default):
  key = input(f"Input key (Default: {default})\n--> ").encode('utf-8')
  key = key if key else default.encode('utf-8')
  return key

def get_text(textfile_path):
  with open(textfile_path, 'rb') as file:
    text = file.read()
  return text

def write_buffer_with_name(buffer, name, extension):
  name = name.replace('_encrypted', '')
  name = name.replace('encrypted_', '')
  name = name.replace('_decrypted', '')
  name = name.replace('decrypted_', '')

  output_path = f"{extension}_" + name
  
  with open(output_path, 'wb') as file:
    file.write(buffer)

  print(f"created {output_path}")
  

"""
- get_file_path(default): returns string
- get_password(default): returns bytes
- get_text(textfile_path): returns bytes
- write_buffer_with_name(buffer, name, ext): just give it the path of the input file and it will take care of the rest
"""

path = get_file_path(default="encrypted_test.txt")
key = get_password(default="pass")
keysize = len(key)

PASSES = 1001
text = bytearray(get_text(path))
for _ in range(PASSES):
  for i in range(len(text)):
   text[i] = text[i] ^ key[i % keysize]

write_buffer_with_name(text, path, 'decrypted')


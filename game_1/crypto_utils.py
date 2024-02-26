"""
crypto_utils.py
- get_passes(default): returns int
- get_file_path(default): returns string
- get_password(default): returns bytes
- stretch_key(key): takes a bytes array, returns an array of size n^2, where n was the size of the input
- get_text(textfile_path): returns bytes
- write_buffer_with_name(buffer, name, ext): just give it the path of the input file and it will take care of the rest
"""

def math_log2(x):
  return 1 if x <= 2 else 1 + math_log2(x/2)

def get_passes(default):
  passes = input(f"How many passes? (Default: {default})\n--> ")
  passes = int(passes) if passes else default
  if passes > 4:
    print("this shit is not multithreaded buddy")
  if passes > 9:
    print("okay buddy, your funeral lmfao")
  return passes

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

def stretch_key(key):
  """
  key stretching algorithm:
  rotate the key as many times as it is long, concat at each iteration
  e.g. given a 4 byte key:
  create the new key by rotating and concatonating the bytes: abcd-dabc-cdab-bcda
  thus you will be left with a key n^2 times the original length
  importantly: the matrix will probably have a non-zero determinant
  """
  new_key = bytes()
  for i in range(len(key)):
    new_key += key
    key = key[-1].to_bytes() + key[:-1]
  return new_key

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
  



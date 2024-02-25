"""
crypto_utils.py
- get_file_path(default)
- get_password(default)
- stretch_key(key)
- get_text(textfile_path)
- write_buffer_with_name(buffer, name, ext): just give it the path of the input file and it will take care of the rest
"""

def get_file_path(default):
  from pathlib import Path

  path = input(f"File to encrypt (Default: {default})\n--> ")
  path = path if path else default
  
  if not Path(path).is_file():
    print("file does not exist, exiting")

  return path

def get_password(default):
  key = input("Please provide a 4 character password").encode('utf-8')
  key = key if key else default.encode('utf-8')
  return key

def stretch_key(key):
  """
  key stretching algorithm:
  split the 32 bit key into 4 separate bytes a, b, c, and d
  create the new key by concatonating the bytes as follows: abcd-dabc-cdab-bcda
  thus you will be left with a key 4 times the original length
  importantly: the 4x4 matrix will probably have a non-zero determinant
  resulting key is 16 bytes or 128 bits
  """
  new_key = bytes()
  for i in range(4):
    new_key.extend(key[:i:-1] + key[i:])
  return new_key

def get_text(textfile_path):
  with open(textfile_path, 'rb') as file:
    text = file.read()
  return text

def write_buffer_with_name(buffer, name, extension):
  from pathlib import Path
  
  if '.' in name:
    name, ext = name.split('.')
    ext = '.' + ext
  else:
    ext = ''

  output_path = name + f"_{extension}" + ext
  #i = 1
  #while Path(output_path).is_file():
  #  output_path = name + f"_encrypted_{i}" + ext
  #  i += 1
  
  with open(output_path, 'wb') as file:
    file.write(buffer)
  





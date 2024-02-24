#!/usr/bin/python3
password = '00000000000000000000000000000000'
print(f"len(password): {len(password)}, int(password): {int(password)}")
with open("plaintext.txt") as file:
  plaintext = file.read()

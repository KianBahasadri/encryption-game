#!/usr/bin/python3
from cryptanalysis.crypta_utils import *
PATH = 'plaintext.txt'
with open(PATH) as file:
  lines = file.readlines()
text = ('\n').join(lines)

results = freq_anal_attack(text)
for t1 in results:
  t2 = sorted([(v, k) for k, v in t1.items()], reverse=True)
  continue
display_freq_attack_output(results)



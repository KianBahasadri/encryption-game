"""
crypta_utils.py
"""
from collections import defaultdict
eng_freq = {" ":20.0, "A":8.2, "B":1.5, "C":2.8, "D":4.3, "E":12.7, "F":2.2, "G":2.0, "H":6.1, "I":7.0, "J":0.15, "K":0.77, "L":4.0, "M":2.4, "N":6.7, "O":7.5, "P":1.9, "Q":0.095, "R":6.0, "S":6.3, "T":9.1, "U":2.8, "V":0.98, "W":2.4, "X":0.15, "Y":2.0, "Z":0.074}

def freq_anal(iterable):
  d = defaultdict(int)
  for x in iterable:
    d[x] += 1
  return d

def freq_anal_attack(iterable, upto=1):
  results = []
  for i in range(0, upto+1):
    d = defaultdict(int)
    for j in range(i):
      for k, v in freq_anal(iterable[j::i]).items():
        d[k] += v
    results.append(d)
  total = len(iterable)
  for result in results:
    for k in result.keys():
      result[k] = round(result[k]/total, 2)
  return results

def print_freq_dict(d):
  l = sorted([(v, k) for k, v in d.items()], reverse=True)
  head = []
  for i in range(min(10, len(l))):
    head.append(f"'{l[i][1]}' {str(l[i][0]).ljust(4, '0')}%")
  print(" | ".join(head))

def display_freq_attack_output(results):
  print("English Text:")
  print_freq_dict(eng_freq)
  for i in range(len(results)):
    print(f"Interval {i+1}:")
    print_freq_dict(results[i])

def save_var_to_file(var, name):
  with open(name, 'w') as file:
    file.write(repr(var))



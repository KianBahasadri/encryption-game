# encryption-game
a game i made that involves hella math and algorithms

```haskell
=============== The Game I Just Made Up ===============
rules:
1. we both come up with our own encryption algorithm in python (no libraries allowed)
2. we encrypt 1 MiB of modern plain English with a 32 bit password
3. we swap the python code and the encrypted data
4. whoever gets the most points within 1 week wins, if its a tie, you play another round

scoring:
3 points - produce code that can decrypt the opponent's data without ever finding the password
2 points - produce code that can decrypt any data encrypted with the opponent's algorithm without ever finding the password
1 point  - brute force the opponent's password
```

## Resources
good plaintext here: (https://www.gutenberg.org/)


## Included Scripts
#### alpha_text.py
removes all non-alphabetic characters from a file, preserving whitespace. This can make analysis of an encrypted text easier


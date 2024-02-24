# encryption-game
a game i made that involves hella math and algorithms

```haskell
=============== The Game I Just Made Up ===============
how to play:
1. we both come up with our own encryption algorithm (no libraries allowed)
2. we encrypt 1 MiB of plain English with a 32 bit password
3. we swap the python code and the encrypted data
4. whoever gets the most points within 1 week wins, if its a tie, you play another round

scoring:
5 points - decrypt the opponent's data without requiring the password
4 points - (find the opponent's password or decrypt the opponent's data) by abusing a weakness in their encryption algorithm
3 points - decrypt any data encrypted with the opponent's algorithm without requiring the password
2 points - find opponent's password by brute force. You must not modify the opponent's algorithm whatsoever.
1 point  - demonstrate that a collision attack is possible on the opponents algorithm


rules:
- you may use any language you want, even for brute forcing
- you may not use any code that you have not written yourself for this specific project
- you must produce code that can demonstrate any function that you claim to have achieved
- you and your opponent must agree on the amount of time spent building your algorithms
- the 3 point challenge can be accomplished on **any** data
- if the 4 point challenge exhausts the key space (brute force), it must be significantly faster than the solution to the 2 point challenge
```

## Resources
good plaintext here: (https://www.gutenberg.org/)


## Included Scripts
#### alpha_text.py
removes all non-alphabetic characters from a file, preserving whitespace. This can make analysis of an encrypted text easier


## Contributing
please make suggestions on how I could improve this game. Thanks


# encryption-game
a game i made up that involves hella math and algorithms

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


## Helper Scripts
#### alpha_text.py
removes all non-alphabetic characters from a file, preserving whitespace. This can make analysis of an encrypted text easier


## Contributing
please make suggestions on how I could improve this game. Thanks



# Game 1
In the first game, I decided to make an encryption algorithm that uses matrix multiplication to encrypt data, and multiplication by an inverse matrix to decrypt data.
Here is how a file is encrypted, in GREAT DETAIL!!!
## Encryption
### Inputs
This algorithm takes 3 inputs, the file to be encrypted, the key, and the number of passes of encryption to be performed.
The output is an encrypted file, the size in bytes can be calculated using the following formula:
$` \text{size}(\text{input\_file}) \times \lceil \log_2(255^{(\text{passes}+1)} \times \text{size}(\text{key})^{\text{passes}}) / 8 \rceil `$
If this looks funky see the section [Matrix To Bytes Conversion](#matrix-to-bytes-conversion)
### Key Stretching
First the key is taken from the user and passed through a key stretching algorithm. This algorithm takes a key of length n, and returns a key of length $n^2$.
The algorithm rotates the key as many times as it is long, and concatonates the current string at each iteration.  
e.g. given a 4 byte key: 'abcd', the resulting key would be 'abcddabccdabbcda', or for better readibility: **a**bcd-d**a**bc-cd**a**b-bcd**a**. So as you can see, its just simply being rotated at each iteration.  
The most important consideration I had to make while developing this algorithm, was that later when the key is transformed into a matrix, this matrix must not have a determinant of zero. Unfortunately, some keys will still cause that to happen, and so there is a check in the code, that prevents you from using a key that would later result in a zero determinant matrix.
### Block Size & Padding
Based on the size of the key from the previous step, the block size is set. If the length of the file is not perfectly divisible by the block size, null bytes are added to the end of the file (called padding), this makes it so that during the encryption process, the matrix taken from the text file always has enough bytes to fill it up.  
After the padding is added, the first byte of the resulting encrypted file is set as the amount of padding that was required. e.g. if 9 bytes of padding were required, the first byte of the encrypted file will be 00001001
### Matrix Multiplication
This is the most computationally intensive part of the algorithm.  
First, a key matrix is constructed by filling in an n * n matrix by the stretched key in order. (Note the stretched key was of size $n^2$).  
Second, the plaintext is divided into blocks, each block being of size $n^2$, and thus a matrix can be constructed for it in the same way.  
The algorithm then iterates over each block in the plaintex, and multiplies the key matrix by the plaintext matrix, as many times as the input of passes.
e.g.
```
passes = 0: (text_matrix)
passes = 1: (key_matrix * (text_matrix))
passes = 2: (key_matrix * (key_matrix * (text_matrix)))
etc.
```
The resulting matrix is then converted to bytes and appended to the file containing the encrypted data
### Matrix To Bytes Conversion
This part is a little bit tricky. The problem is that the value of a single byte can only go up to 255, but given a high number of passes, element values can reach the millions.
The way to solve this problem is by using more bytes to store each value. My solution to choosing the number of bytes to use is to make a generous guess.
The highest theoretical value that can be reached, is $255^{(\text{passes}+1)} \times \sqrt{\text{blocksize}}^{\text{passes}}$. So thats scaling preeety fast.
So, to choose the number of bytes per element, I just calculate that value and find n for 2^(8*n) > than that value. This is not efficient but it's safe, so who cares I do it :D

## Decryption
### Inputs
Unlike encryption there are only 2 inputs, the file to be decrypted and the key. This time, the number of passes is stored at the beginning of the encrypted file, so we dont need to tell the algorithm.

### Key Stretching
Key stretching is performed just as before

### Reversing Effects of Matrix Multiplication
To recap, we had a key matrix K and a plaintext matrix T. We did KT and now we have an encrypted matrix E. To go back to T, only given E and K, we need to do $K^{-1}E$.  
Unfortunately, this poses quite a big problem for modern computers. $K^{-1}$ is calculated using the reciprocal of the determinant, which is a fraction. In short, $K^{-1}$ is full of floating point numbers.  
To solve this problem, I broke down the inverse matrix into its various components and applied them individually.
```
inverse(A) = 1/det(A)  *  adj(A)
Now recall that multiplication is commutative here,
so (1/det(A) * adj(A)) * B is the same as 1/det(A) * (adj(A) * B)
Thus, to "undo" the matrix multiplication we did earlier, we can simply do
1/det(key_mat) * (adj(key_mat) * enc_mat)
and thats how we get back the original matrix :)
```
So that's how the algorithm is able to do inverse matrix multiplication without dealing with floating point values

### Removind Padding
The last bytes are removed based on how much padding was added by the algorithm

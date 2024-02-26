"""
matrix_utils.py
- bytes_to_matrix(_bytes, size=1): Converts bytes to a square matrix, where 'size' indicates the byte length of each number.
- matrix_to_bytes(mat, size=1): Converts a square matrix back into bytes, with 'size' specifying the byte length of each number.
- mat_mul(a, b): Performs multiplication of two square matrices.
- undo_mat_mul(key_mat, enc_mat): Decrypts encrypted text by applying matrix multiplication's inverse operation using a key matrix and an encrypted matrix.
- mat_adjoint(mat): Calculates the adjoint of a matrix.
- mat_det(mat): Computes the determinant of a matrix.
- mat_cofactor(mat, i, j): Determines the cofactor of an element in a matrix.
- mat_transpose(mat): Transposes a matrix.
"""

def bytes_to_matrix(_bytes, size):
  """
  size represents the number of bytes in a number
  always expect size of _bytes to be a perfect square * size
  matrix will be of size n*n
  """
  n = int((len(_bytes) // size) ** 0.5)
  matrix = [[0]*n for _ in range(n)]
  for i in range(0, n):
    for j in range(0, n):
      index = i*size*n + j*size
      val = int.from_bytes(_bytes[index:index+size])
      matrix[i][j] = val
  return matrix

def matrix_to_bytes(mat, size):
  """ size represents the number of bytes in a number """
  _bytes = bytes()
  for row in mat:
    for value in row:
      _bytes += value.to_bytes(size)
  return _bytes

def mat_mul(a, b):
  result = []
  for i in range(len(a)):
    result.append([])
    for j in range(len(a)):
      result[i].append(0)
      for k in range(len(a)):
        result[i][j] += a[i][k] * b[k][j]
  return result

def undo_mat_mul(key_mat, enc_mat):
  """
  To decrypt the encrypted text, we need to perform the following calculation:
  inverse(key_mat) * enc_mat
  the problem is that if we directly inverse the key_mat we will get floating points because of the reciprocal of the determinant
  So we can do some sneaky shenanigans, and break down the inverse(key_mat) into components:
  inverse(A) = 1/det(A)  *  adj(A)
  Now recall that multiplication is commutative here,
  so (1/det(A) * adj(A)) * B is the same as 1/det(A) * (adj(A) * B)
  Thus, to "undo" the matrix multiplication we did earlier, we can simply do
  1/det(key_mat) * (adj(key_mat) * enc_mat)
  and thats how we get dec_mat :)
  References:
  https://en.wikipedia.org/wiki/Invertible_matrix#In_relation_to_its_adjugate
  """
  adj_key_mat = mat_adjoint(key_mat)
  new_mat = mat_mul(adj_key_mat, enc_mat)
  det = mat_det(key_mat)
  for i in range(len(key_mat)):
    for j in range(len(key_mat)):
      new_mat[i][j] //=  det # should be a whole number anyways
  return new_mat

def mat_adjoint(mat):
  cofactor_mat = [[0]*len(mat) for _ in range(len(mat))]
  for i in range(len(mat)):
    for j in range(len(mat)):
      cofactor_mat[i][j] = mat_cofactor(mat, i, j)
  adjoint_mat = mat_transpose(cofactor_mat)
  return adjoint_mat

def mat_det(mat):
  """
  Simple recursive cofactor expansion
  formula from https://en.wikipedia.org/wiki/Laplace_expansion
  """
  if len(mat) == 2:
    return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
  
  det = 0
  for i in range(1):
    for j in range(len(mat)):
      det += mat_cofactor(mat, i, j) * mat[i][j]
  return det

def mat_cofactor(mat, i, j):
  """
  I split this away from mat_det because its also used in calculating the adjoint matrix
  formula from https://en.wikipedia.org/wiki/Laplace_expansion
  """
  sub_mat = [row[:] for row in mat]
  del sub_mat[i]
  for row in sub_mat:
    del row[j]
  return (-1)**(i+j) * mat_det(sub_mat)

def mat_transpose(mat):
  """
  formula from https://en.wikipedia.org/wiki/Transpose
  """
  new_mat = [[0]*len(mat) for _ in range(len(mat))]
  
  for i in range(len(mat)):
    for j in range(len(mat)):
      new_mat[i][j] = mat[j][i]
  return new_mat



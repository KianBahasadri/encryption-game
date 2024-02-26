"""
matrix_utils.py
- bytes_to_matrix(_bytes): Converts a bytes object of length 16 into a 4x4 matrix
- matrix_to_bytes(mat): Converts a 4x4 matrix back into a bytes object
- mat_mul(a, b): Multiplies two 4x4 matrices (a and b) together and returns the result
- mat_inv(mat): Calculates the inverse of any size matrix
- mat_det(mat): Calculates the determinant of any size matrix
"""

def bytes_to_matrix(_bytes, size=1):
  """ size represents the number of bytes in a number """
  matrix = [[], [], [], []]
  for i in range(0, 16*size, size):
    val = int.from_bytes(_bytes[i:i+1*size])
    matrix[i//(4*size)].append(val)
  return matrix

def matrix_to_bytes(mat, size=1):
  """ size represents the number of bytes in a number """
  _bytes = bytes()
  for row in mat:
    for value in row:
      _bytes += value.to_bytes(size)
  return _bytes

def mat_mul(a, b):
  result = []
  for i in range(4):
    result.append([])
    for j in range(4):
      result[i].append(0)
      for k in range(4):
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
  det = mat_det(mat)
  for i in range(len(mat)):
    for j in range(len(mat)):
      new_mat[j][i] = new_mat // det # should be a whole number anyways
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



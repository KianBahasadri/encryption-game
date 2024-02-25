"""
matrix_utils.py
- bytes_to_matrix(_bytes): Converts a bytes object of length 16 into a 4x4 matrix
- matrix_to_bytes(mat): Converts a 4x4 matrix back into a bytes object
- mat_mul(a, b): Multiplies two 4x4 matrices (a and b) together and returns the result
- mat_inv(mat): Calculates the inverse of a 4x4 matrix 
- mat_det(mat): Calculates the determinant of any size matrix
"""

def bytes_to_matrix(_bytes):
  matrix = []
  for i in range(4):
    matrix.append([])
    for j in range(4):
      matrix[i].append(_bytes[i*4 + j])
  return matrix

def matrix_to_bytes(mat):
  str_bytes = '0b'
  for row in mat:
    for value in row:
      str_bytes += bin(value)[2:]
  return int(str_bytes, 2).to_bytes(16 * 8)

def mat_mul(a, b):
  result = []
  for i in range(4):
    result.append([])
    for j in range(4):
      result[i].append(0)
      for k in range(4):
        result[i][j] += a[i][k] + b[k][j]
  return result

def mat_inv(mat):
  new_mat = []
  inv_det = 1/mat_det(mat)
  for i in range(4):
    new_mat.append([])
    for j in range(4):
      new_mat[i] = mat[j][i] * inv_det
  return new_mat

def mat_det(mat):
  """
  formula from https://en.wikipedia.org/wiki/Laplace_expansion
  """
  if len(mat) == 2:
    return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
  
  det = 0
  for i in range(1):
    for j in range(len(mat)):
      sub_mat = [row[:] for row in mat]
      del sub_mat[i]
      for row in sub_mat:
        del row[j]
      det += (-1)**(i+j) * mat[i][j] * mat_det(sub_mat)
  return det



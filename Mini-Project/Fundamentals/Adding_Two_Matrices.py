# This code performs element-wise addition of two matrices X and Y.

X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

# Initialize the result matrix with zeros
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Iterate through each element of the matrices
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

# Print the resulting matrix
for r in result:
    print(r)

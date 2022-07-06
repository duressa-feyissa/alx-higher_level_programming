#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new[i].append(matrix[i][j] * matrix[i][j])
    return new

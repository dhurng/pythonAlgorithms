"""
rotate matrix by 90 degrees
in place

runtime is O(n^2) since it has to douch all elements
"""

def main():
    print rotate()

def rotate(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]): return False
    length = len(matrix)
    for i in length/2:
        first = i
        last = length - 1 - i
        j = first
        while j < last:
            offset = j - first
            top = matrix[first][j]

            matrix[first][j] = matrix[last - offset][first]

            matrix[last - offset][first] = matrix[last][last - offset]

            matrix[last][last - offset] = matrix[i][last]

            matrix[j][last] = top
    return True

def nullifyrow(matrix, row):
    for j in len(matrix[0]):
        matrix[row][j] = 0

def nullifycolumn(matrix, col):
    for i in len(matrix):
        matrix[i][col] = 0

def nullify(matrix):
    row = [len(matrix)]
    column = [len(matrix[0])]

#     store row and column index with value 0
    for i in len(matrix):
        for j in len(matrix[0]):
            if matrix[i][j] == 0:
                row[i] = True
                column[j] = True

#     nullify rows
    for i in len(row):
        if row[i]:
            nullifyrow(matrix, i)

#     nullify columns
    for j in len(column):
        if column[j]:
            nullifycolumn(matrix, j)


if __name__ == '__main__':
    table = [[0 for i in range(4)] for j in range(4)]
    main()

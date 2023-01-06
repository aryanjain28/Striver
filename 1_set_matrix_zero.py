"""
Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.
 
Input: matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output:[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
Explanation:Since matrix[0][0]=0 and matrix[0][3]=0. Therefore 1st row, 1st column and 4th column will be set to 0

"""

def update_matrix(zero_row, zero_col, matrix):
    n_row = len(matrix)
    n_col = len(matrix[0])
    LEN = max(n_row, n_col)

    for k in range(0,LEN):
        if k < n_row and matrix[k][zero_col] != 0:
            matrix[k][zero_col] = 0
        if k < n_col and matrix[zero_row][k] != 0:
            matrix[zero_row][k] = 0

    return matrix

def main(original_matrix):
    
    # deep copy
    matrix = [x[:] for x in original_matrix]
    n_rows = len(original_matrix)
    n_cols = len(original_matrix[0])

    i = 0
    j = 0

    for i in range(0, n_rows):
        for j in range(0, n_cols):
            if matrix[i][j] == 0 and not original_matrix[i][j] != matrix[i][j]:
                matrix = update_matrix(i,j,matrix)

    return matrix

# Best solution - Leet Code
def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """

    n_rows = len(matrix)
    n_cols = len(matrix[0])

    is_row = 0 in matrix[0]
    is_col = False

    for i in range(0, n_rows):
        if matrix[i][0] == 0:
            is_col = True
        for j in range(0, n_cols):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0


    for i in range(1, n_rows):
        for j in range(1, n_cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if is_row:
        for j in range(n_cols):
            matrix[0][j] = 0

    if is_col:
        for i in range(n_rows):
            matrix[i][0] = 0

    return matrix


matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
print(setZeroes(matrix))

# print(main(matrix))



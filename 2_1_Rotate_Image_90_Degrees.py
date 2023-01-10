def rotate_image_90_degrees(matrix):

    matrix_len = len(matrix)
    
    # transpose
    for k in range(matrix_len // 2):
        matrix[k], matrix[matrix_len - k - 1] = matrix[matrix_len - k - 1], matrix[k]

    for i in range(matrix_len - 1):
        for j in range(i + 1, matrix_len):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    return matrix

input = [[1,2,3],[4,5,6],[7,8,9]]
input = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix = rotate_image_90_degrees(input)
print(matrix)
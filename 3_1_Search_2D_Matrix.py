def binary_search(target, sorted_matrix):

    row = len(sorted_matrix)
    col = len(sorted_matrix[0])
    first_pointer = 0
    last_pointer = (row * col) - 1


    while(first_pointer <= last_pointer):
        midpoint = (first_pointer + last_pointer) // 2

        if(sorted_matrix[midpoint // col][midpoint % col] == target):
            return True
        elif(sorted_matrix[midpoint // col][midpoint % col] < target):
            first_pointer = midpoint + 1
        else:
            last_pointer = midpoint - 1
        
    return False


def is_integer_exists(target, matrix):

    arr = []    
    for row in matrix:
        arr += row
    return binary_search(target, matrix)


target = 3
input_matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

output = is_integer_exists(target, input_matrix)

print("OUTPUT: ", output)
"""
3 Questions related to Pascal's

1. Get Pascal's Triangle
2. Get Element at Row,Col
3. Get Row at N

"""

# 1. To get complete Triangle
def pascals_triangle(n):
    list = []
    if n == 1: 
        list = [[1]]
    elif n == 2:
        list = [[1], [1,1]]
    else:
        list = [[1], [1,1]]
        for i in range(3, n+1):
            l = []
            last_list = list[len(list) - 1]
            l.append(1)
            for k in range(0, i-2):
                l.append(last_list[k] + last_list[k+1])
            l.append(1)
        
            list.append(l)
    
    return list

triangle = pascals_triangle(6)
# print(triangle)

def get_factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * get_factorial(n-1)

# 2. Get Element at (Row,Col)
def get_element_at_position(row, col):
    # Use (row-1)C(col-1) to get the element

    fact_row = get_factorial(row - 1)
    fact_col = get_factorial(col - 1) * get_factorial(row - col)

    return fact_row // fact_col

# print(get_element_at_position(5, 3))

# 3. Get complete row
def get_row(n):
    row = []
    for i in range(1, n+1):
        row.append(get_element_at_position(n, i))
    return row

print(get_row(20))



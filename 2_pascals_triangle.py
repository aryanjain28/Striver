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
print(triangle)



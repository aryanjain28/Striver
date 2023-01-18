def find_repeating_and_missing_freq_arr(arr):
    freq_arr = [0] * len(arr)
    for n in arr: freq_arr[n-1] += 1
    return freq_arr.index(2) + 1, freq_arr.index(0) + 1

def find_repeating_and_missing_arithmetic(arr):
    LEN = len(arr)
    s = len(arr) * (len(arr) + 1) / 2 
    p = (LEN * (LEN+1) * (2*LEN + 1)) / 6

    s1 = 0
    p1 = 0
    for a in arr:
        s1 += a
        p1 += a*a

    s_dash = s - s1
    p_dash = p - p1

    X = (s_dash + p_dash/s_dash) / 2
    Y = X - s_dash
    
    return X, Y

input_arr = [3,1,2,5,3]
output = find_repeating_and_missing_arithmetic(input_arr)
print(output)
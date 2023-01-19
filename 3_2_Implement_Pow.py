def implement_pow_binary(x, n):
    extra = 1
    if n == 0: return 1
    
    if n < 0:
        x = 1 / x
        n = -1 * n
        
    while n > 1:
        if n % 2 != 0:
            n = n - 1
            extra = extra * x

        n = n // 2
        x = x * x

    return x * extra

output = implement_pow_binary(2.00000, -2)
print(output)
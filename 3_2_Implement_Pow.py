def implement_pow_binary(x, n):
    extra = 1
    while n > 1:
        if n % 2 != 0:
            n = n - 1
            extra = extra * x

        n = n // 2
        x = x * x

    return x * extra

output = implement_pow_binary(3.0000, 4)
print(output)


# fib number


def fib(num):

    prev1 = 0
    prev2 = 1

    for _ in range(2, num+1):
        curr = prev2 + prev1
        prev1 = prev2
        prev2 = curr

    print(curr)
    return curr

    # dp = [-1] * (num+1)
    # dp[0] = 0
    # dp[1] = 1

    # for i in range(2, num+1):
    #     dp[i] = dp[i-1] + dp[i-2]

    # print(dp)
    # return dp[-1]

    # def helper(n):

    #     if dp[n] != -1:
    #         return dp[n]

    #     if n <= 1:
    #         return n

    #     dp[n] = helper(n-1) + helper(n-2)
    #     return dp[n]

    # return helper(num)


print(fib(6))

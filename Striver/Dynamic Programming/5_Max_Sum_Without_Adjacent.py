def maximumNonAdjacentSum(nums):

    n = len(nums)

    # dp = {}

    # def rec(i):

    #     if i == 0:
    #         return nums[0]

    #     if i in dp:
    #         return dp[i]

    #     maximum = -1
    #     for j in range(2, i+1):
    #         maximum = max(maximum, rec(i-j) + nums[i])

    #     dp[i] = maximum
    #     return dp[i]

    # return rec(n-1)

    dp = [0] * n
    dp[0] = nums[0]

    for i in range(1, n):
        maximum = -1
        for j in range(2, i+1):
            maximum = max(maximum, dp[i-j] + nums[i])

        dp[i] = maximum

    return dp[-1]


print(maximumNonAdjacentSum([5, 5, 10, 100, 10, 5]))
print(maximumNonAdjacentSum([3, 2, 5, 10, 7]))
print(maximumNonAdjacentSum([3, 2, 7, 10]))

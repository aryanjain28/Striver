def maximumNonAdjacentSum(nums):

    # pick
    # nPick

    # dp = {}

    # def rec(index):

    #     if index in dp:
    #         return dp[index]

    #     if index < 0:
    #         return 0

    #     pick = nums[index] + rec(index-2)
    #     nPick = 0 + rec(index-1)

    #     dp[index] = max(pick, nPick)
    #     return dp[index]

    # return rec(len(nums)-1)

    # tabulation

    n = len(nums)
    dp = [nums[0]] * n

    for i in range(1, n):
        nPick = dp[i-1]

        pick = nums[i]
        if i > 1:
            pick += dp[i-2]

        dp[i] = max(pick, nPick)

    return dp[-1]


    # dp = {}
    # def rec(i):
    #     if i in dp:
    #         return dp[i]
    #     if i == 0:
    #         return nums[0]
    #     if i <= 0:
    #         return 0
    #     pick = nums[i] + rec(i-2)
    #     nPick = rec(i-1)
    #     dp[i] = max(pick, nPick)
    #     return dp[i]
    # return rec(len(nums)-1)
    # dp[i] = maximum
    # return dp[i]
    # res = []
    # for m in range(n-1, -1, -1):
    #     res.append(rec(m))
    # return max(res)
    # n = len(nums)
    # dp = [nums[0]] * n
    # for i in range(1, n):
    #     print(dp, nums[i])
    #     maximum = nums[i]
    #     for j in range(2, i+1):
    #         if i >= j:
    #             maximum = max(maximum, dp[i-j] + nums[i])
    #     dp[i] = max(dp[i-1], maximum)
    # print(dp)
    # return dp[-1]
# print(maximumNonAdjacentSum([5, 5, 10, 100, 10, 5]))
# print(maximumNonAdjacentSum([3, 2, 5, 10, 7]))
# print(maximumNonAdjacentSum([3, 2, 7, 10]))
# print(maximumNonAdjacentSum([9, 9, 8, 2]))
# print(maximumNonAdjacentSum([3, 10, 10, 7]))
print(maximumNonAdjacentSum([2, 1, 4, 9]))

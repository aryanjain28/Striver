  
# def frogJump(n: int, heights):


#     # # Write your code here.
#     dp = {}
#     def rec(i, energy):

#         if i >= n-1:
#             return energy

#         if (i, energy) in dp:
#             return dp[(i, energy)]

#         left = rec(i+1, energy + abs(heights[i] - heights[i+1]))

#         if i + 2 >= n:
#             return left

#         right = rec(i+2, energy + abs(heights[i] - heights[i+2]))

#         dp[(i, energy)] = min(left, right)
#         return dp[(i, energy)]


#     dp = [0] * n
#     dp[0] = 0
#     dp[1] = 0
    
#     for i in range(1, n):
#         left = dp[i-1] + abs(heights[i] - heights[i-1])

#         right = left
#         if i >= 2:
#             right = dp[i-2] + abs(heights[i] - heights[i-2])

#         dp[i] = min(left, right)

#     print(dp)

    
#     prev2 = 0
#     prev1 = abs(heights[1] - heights[0])

#     for i in range(2, n):        
#         curr = min(prev2 + abs(heights[i] - heights[i-2]), prev1 + abs(heights[i] - heights[i-1]))
#         prev2 = prev1        
#         prev1 = curr

#     return curr





# print(frogJump(4, [10, 20, 30, 10]))




def frogJumpK(n, heights, k):

    # def rec(index):

    #     if index == 0:
    #         return 0

    #     minimum = float("inf")
    #     for i in range(1, k+1):
    #         if 0 <= j <= i:
    #             minimum = min(minimum, rec(index-i) + abs(heights[index] - heights[index-i]))
        
    #     return minimum

    # return rec(n-1)

    if k > n:
        return 0


    dp = [0] * n
    dp[0] = 0

    for i in range(1, n):
        minimum = float("inf")
        for j in range(1, k+1):
            if i >= j:
                minimum = min(minimum, dp[i-j] + abs(heights[i] - heights[i-j]))
 
        dp[i] = minimum

    return dp[-1]


    # for i in range(1, n):
    #     dp[index-i] + abs(heights[index] - heights[index-i])









height = [30, 10, 60, 10, 60, 50]
n = len(height)
k = 2

print(frogJumpK(n, height, k))

height = [10, 30, 40, 50, 20]
n = len(height)
k = 3

print(frogJumpK(n, height, k))

height = [10, 20, 10]
n = len(height)
k = 1

print(frogJumpK(n, height, k))

height = [10, 10]
n = len(height)
k = 100

print(frogJumpK(n, height, k))


height = [40, 10, 20, 70, 80, 10, 20, 70, 80, 60]
n = len(height)
k = 4


print(frogJumpK(n, height, k))

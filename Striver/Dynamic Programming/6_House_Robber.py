

def houseRobber(money):

    def rec(m, index):

        if index in dp:
            return dp[index]

        if index < 0:
            return 0

        pick = m[index] + rec(m, index-2)
        nPick = 0 + rec(m, index-1)

        dp[index] = max(pick, nPick)
        return dp[index]

    m1, m2 = money[:-1], money[1:]

    dp = {}
    r1 = rec(m1, len(m1) - 1)
    dp = {}
    r2 = rec(m2, len(m2) - 1)
    return max(r1, r2)


def houseRobber_dp(money):

    n = len(money)
    dp = [money[0]] * n

    for i in range(1, n):

        nPick = 0 + dp[i-1]
        pick = money[i]
        if i > 1:
            pick = money[i] + dp[i-2]

        dp[i] = max(pick, nPick)

    return dp[-1]


def houseRobber_dp_space_op(money):

    prev0 = prev1 = money[0]

    for i in range(1, len(money)):

        nPick = 0 + prev1
        pick = money[i]
        if i > 1:
            pick = money[i] + prev0

        curr = max(pick, nPick)
        prev0 = prev1
        prev1 = curr

    return curr


money = [2, 1, 4, 9]
r1 = houseRobber_dp_space_op(money[1:])
r2 = houseRobber_dp_space_op(money[:-1])
print(max(r1, r2))

# def rec(m, index):

#     if index in dp:
#         return dp[index]

#     if index < 0:
#         return 0

#     pick = m[index] + rec(m, index-2)
#     nPick = 0 + rec(m, index-1)

#     dp[index] = max(pick, nPick)
#     return dp[index]

#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

import collections
# @lc code=start
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        

        parent = list(range(len(accounts)))

        def find(v):
            if v != parent[v]:
                parent[v] = find(parent[v])
            return parent[v]

        def union(v1, v2):
            parent[find(v1)] = find(v2)


        ownership = {}
        for index, account in enumerate(accounts):
            for email in account[1:]:
                if email in ownership:
                    union(index, ownership[email])
                ownership[email] = index



        res = collections.defaultdict(list)
        for email, owner in ownership.items():
            res[find(owner)].append(email)

        return [[accounts[index][0]] + sorted(val) for index, val in res.items()]
        


# @lc code=end
Solution().accountsMerge(
    [
        ["David","David0@m.co","David3@m.co","David4@m.co","David5@m.co"],
        ["David","David1@m.co","David2@m.co"]
    ]
)





[
    ["David","David0@m.co","David1@m.co"],
    ["David","David3@m.co","David4@m.co"],
    ["David","David4@m.co","David5@m.co"],
    ["David","David2@m.co","David3@m.co"],
    ["David","David1@m.co","David2@m.co"]
    ]



def subseq_k(nums, k):

    n = len(nums)

    def rec(index, arr, curr):

        if curr == k:
            return 1

        if index >= n:
            return 0

        return rec(index+1, arr + [nums[index]], curr + nums[index]) + rec(index+1, arr, curr)

    return rec(0, [], 0)


print(subseq_k([1, 2, 1], 2))

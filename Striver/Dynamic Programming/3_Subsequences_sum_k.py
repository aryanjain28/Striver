

def subseq_k(nums, k):

    n = len(nums)

    def rec(index, arr, curr):

        if curr == k:
            print(arr)
            return

        if index >= n:
            return

        # pick
        rec(index+1, arr + [nums[index]], curr + nums[index])

        # not pick
        rec(index+1, arr, curr)

    return rec(0, [], 0)


subseq_k([1, 2, 1], 2)

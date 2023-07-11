

def subseq_k(nums, k):

    n = len(nums)

    def rec(index, arr, curr):

        if curr == k:
            print(arr)
            return True

        if index >= n:
            return False

        if rec(index+1, arr + [nums[index]], curr + nums[index]):
            return True

        if rec(index+1, arr, curr):
            return True

        return False

    return rec(0, [], 0)


subseq_k([1, 2, 1], 2)

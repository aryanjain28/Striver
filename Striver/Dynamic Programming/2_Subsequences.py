

def subseq(nums):

    sub = []
    n = len(nums)

    def rec(index, arr: list):

        if index >= n:
            print(arr)
            sub.append(arr)
            return

        rec(index+1, arr + [nums[index]])
        rec(index+1, arr)

    rec(0, [])


subseq([3, 1, 2])

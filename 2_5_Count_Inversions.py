class Solution:

    def __init__(self):
        self.inversions = 0

    # def count_inversions_brute(arr):
    #     inversions = 0

    #     for i in range(len(arr) - 1):
    #         for j in range(i, len(arr)):
    #             if arr[i] > arr[j]:
    #                 inversions += 1

    #     return inversions

    def merge(self, left, right):
        i = 0
        j = 0
        result = []

        while i < len(left) and j < len(right):
            if(left[i] < right[j]):
                result.append(left[i])
                i += 1
            else:
                self.inversions += 1
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1
            
        while j < len(right):
            result.append(right[i])
            j += 1

        return result

    def merge_sort(self, arr):

        if len(arr) == 1 or len(arr) == 0:
            return arr

        mid_point = len(arr) // 2 
        left_arr = self.merge_sort(arr[:mid_point])
        right_arr = self.merge_sort(arr[mid_point:])

        merged_arr = self.merge(left_arr, right_arr)
        return merged_arr



input_arr = [5,3,2,1,4]
input_arr = [5,4,3,2,1]
input_arr = [1,2,3,4,5]
input_arr = []

s = Solution()

output = s.merge_sort(input_arr)
print(output)
print(s.inversions)

# output = count_inversions_brute(input_arr)
# output = merge_sort(input_arr, 0)
# print(output)
# print(inversions)
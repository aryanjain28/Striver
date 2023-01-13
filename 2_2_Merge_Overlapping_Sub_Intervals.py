def merge(first, second):
    return [min(first[0], second[0]), max(first[1], second[1])]

def can_merge(first, second):
    return (first[0] <= second[0] <= first[1]) or (second[0] <= first[0] <= second[1])

# def merge_overlapping_sub_intervals(intervals):
#     result = []
#     i = 0

#     if len(intervals) < 2:
#         return intervals

#     result = [intervals[0]]
#     while i < len(intervals) - 1:

#         current_interval = intervals[i]
#         next_interval = intervals[i+1]
        
#         if can_merge(current_interval, next_interval):
#             # merge
#             merged_interval = merge(current_interval, next_interval)
#             intervals[i+1] = merged_interval

#             if result[-1][0] == current_interval[0] and result[-1][1] == current_interval[1]:
#                 result[-1] = merged_interval
                
#                 # Going backwards
#                 j = len(result) - 1
#                 while j > 0:
#                     current_res_interval = result[j]
#                     previous_res_interval = result[j-1]

#                     if can_merge(previous_res_interval, current_res_interval):
#                         result[j-1] = merge(previous_res_interval, current_res_interval)
#                         result.pop()
#                     else:
#                         j = -1 # break
                    
#                     j -= 1
#             else:
#                 result.append(merged_interval)

#         else:
#             result.append(next_interval)

#         i += 1

#     return result


# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,3],[2,6],[5,10],[9,18]]
# intervals = [[1,4],[5,6]]
# intervals = [[1,3]]
# intervals = [[1,4],[0,1]]
# intervals = [[1,4],[0,0]]
# intervals = [[1,4],[0,4]]
# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
# intervals = [[2,4],[3,5],[4,7],[8,9],[1,10],[11,12],[12,13]]
# print(merge_overlapping_sub_intervals(intervals))

# Not the best way to sort though!!
def sort_intervals(intervals):
    return sorted(intervals)
    # for i in range(len(intervals)):
    #     minimum_index = i
    #     for j in range(i, len(intervals)):
    #         if intervals[j][0] < intervals[minimum_index][0]:
    #             minimum_index = j
    #         if intervals[j][0] == intervals[minimum_index][0]:
    #             if intervals[j][1] < intervals[minimum_index][1]:
    #                 minimum_index = j
        
    #     intervals[i], intervals[minimum_index] = intervals[minimum_index], intervals[i]
        
    # return intervals

def merge_intervals(intervals):
    merged_intervals = []
    i = 0

    if len(intervals) < 2:
        return intervals

    merged_intervals = [intervals[0]]
    while i < len(intervals) - 1:
        current_interval = intervals[i]
        next_interval = intervals[i+1]
        
        if can_merge(current_interval, next_interval):
            # merge
            merged_interval = merge(current_interval, next_interval)
            intervals[i+1] = merged_interval

            if merged_intervals[-1][0] == current_interval[0] and merged_intervals[-1][1] == current_interval[1]:
                merged_intervals[-1] = merged_interval
            else:
                merged_intervals.append(merged_interval)
        else:
            merged_intervals.append(next_interval)

        i += 1

    return merged_intervals


def merge_overlapping_sub_intervals_(intervals):
    sorted_intervals = sort_intervals(intervals)
    merged_intervals = merge_intervals(sorted_intervals)
    print(merged_intervals)
    

intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,3],[8,10],[2,6],[15,18],[9,9]]
intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
intervals = [[1,3],[2,6],[5,10],[9,18]]
# intervals = [[1,4],[5,6]]
# intervals = [[1,3]]
# intervals = [[1,4],[0,1]]
# intervals = [[1,4],[0,0]]
# intervals = [[1,4],[0,4]]
# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
intervals = [[2,4],[3,5],[4,7],[8,9],[1,10],[11,12],[12,13]]
# print(merge_overlapping_sub_intervals(intervals))
merge_overlapping_sub_intervals_(intervals)

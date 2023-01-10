# Brute Force
def stock_max_profit_brute(list):
    min_index = 0
    max_profit = 0

    while min_index < len(list) - 1:
        profit = max(list[min_index + 1:]) - list[min_index]
        if max_profit < profit:
            max_profit = profit 
        min_index += 1

    return max_profit


# O(n)
def stock_max_profit(nums):
    max_profit = 0
    minimum = nums[0]

    i = 0
    while(i < len(nums)):
        if nums[i] < minimum:
            minimum = nums[i]

        if max_profit < nums[i] - minimum:
            max_profit = nums[i] - minimum
        
        i += 1

    return max(0, max_profit)

stocks = [7,1,5,3,6,4] 
stocks = [7,6,4,3,1]
print(stock_max_profit(stocks))
# print(stock_max_profit_brute(stocks))

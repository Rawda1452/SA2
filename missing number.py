listy=[1,2,3,4,6,7,8]
def find_missing_number(nums):
    n = len(nums) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    missing_number = total_sum - actual_sum
    return missing_number
print (find_missing_number(listy))
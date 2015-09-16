# practice question from talk by parker from interview cake
# given a list of integers, find the greatest difference between any two numbers in that list

# solution 1

def get_greatest_diff_1(list_nums):
    list_diffs = []
    for num1 in list_nums:
        for num2 in list_nums:
            list_diffs.append(num1 - num2)
    return max(list_diffs)

# throws an error when given an empty list
# time cost: O(n^2)
# space cost: O(n^2)


# solution 2

def get_greatest_diff_2(list_nums):
    nums_sorted = sorted(list_nums)
    return nums_sorted[-1] - nums_sorted[0]

# throws an error when given an empty list
# time cost: O(nlogn)
# space cost: O(n)


# solution 3

def get_greatest_diff_3(list_nums):
    if len(list_nums) < 2:
        return None
    max = list_nums[0]
    min = list_nums[0]
    for num in list_nums:
        if num > max:
            max = num
        if num < min:
            min = num
    return max - min

# time cost: O(n)
# space cost: O(1)

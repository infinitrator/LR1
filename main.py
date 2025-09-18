def two_sum(nums, target):
    num_map = {}
    if len(nums) > 1:
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], index]
            num_map[num] = index
    else: return None
    return []


print(two_sum([3, 3], 6))           # Output: [0, 1]
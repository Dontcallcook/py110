def twoSum(nums, target):
    idx1 = 0
    idx2 = 0

    while nums[idx1] + nums[idx2] != target:
        idx2 += 1
        if nums[idx1] + nums[idx2] == target:
            return [idx1, idx2]

        if idx2 == (len(nums) - 1):
            idx1 += 1
            idx2 = idx1 + 1



print(twoSum([3,2,4], 6))
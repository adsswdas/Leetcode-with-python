class Solution(object):
    def searchInsert(self, nums, target):
        nums.append(target+1)
        for i in range(len(nums)-1, -1, -1):
            if nums[i] >= target and nums[i-1] < target:
                return i
        return 0

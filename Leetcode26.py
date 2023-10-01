class Solution(object):
    def removeDuplicates(self, nums):
        for num in nums:
            for num1 in nums[nums.index(num)+1:]:
                if num == num1:
                    nums.remove(num)
                else:
                    break
        return len(nums)

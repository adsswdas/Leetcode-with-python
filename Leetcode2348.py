class Solution(object):
    def ZeroFilledSubarray(self, nums):
        sub_array = 0
        n = len(nums)

        list = []
        sub_list = []

        for i in nums:
            if i == 0:
                sub_list.append(i)
            else:
                list.append(sub_list)
                sub_list = []

        if sub_list != []:
            list.append(sub_list)

        print(list)

        for i in list:
            for j in range(0, len(i)):
                sub_array = sub_array + (len(i) - j)

        return sub_array

s = Solution()
print(s.ZeroFilledSubarray([0,1,0,0,0,0,0,1]))

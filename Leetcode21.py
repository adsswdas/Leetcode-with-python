class Solution(object):
    def mergeTwoLists(self, list1, list2):
        list3 = list1 + list2
        for i in range(len(list3)):
            for j in range(i+1, len(list3)):
                if list3[j] < list3[i]:
                    list3[i], list3[j] = list3[j], list3[i]
        return list3


a = Solution()
print(a.mergeTwoLists([1, 2, 3], [2, 4, 5]))


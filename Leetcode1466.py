class Solution(object):
    def minReorder(self, n, connections):
        result = n-1
        list = []
        for i in connections:
            if i[1] == 0:
                list.append(i[0])
                result -= 1
        return result
        
s = Solution()
print(s.minReorder(5, [[0, 1], [1, 0], [1, 2], [2, 3], [3, 0]]))

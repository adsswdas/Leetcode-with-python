class Solution(object):
    def longestCommonPrefix(self, strs):
        n = strs[0]
        for i in range(len(strs)):
            if len(strs[i]) < len(n):
                n = strs[i]

        print(n)
        prefix = ""
        for i in range(len(n)):
            for j in strs:
                if j[i] != n[i]:
                    return prefix
            prefix += n[i]

        return prefix
s = Solution()
print(s.longestCommonPrefix(["lower", "flow", "flight", "flo"]))
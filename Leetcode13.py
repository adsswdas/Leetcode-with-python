class Solution(object):
    def romanToInt(self,s):
        d =        {'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000}
        i = 0
        for k in range(len(s)-1):
            if d[s[k]] >= d[s[k+1]]:
                i = i + d[s[k]]

            else:
                i = i - d[s[k]]

        i += d[s[-1]]
        return i

s = Solution()
print(s.romanToInt('XIX'))

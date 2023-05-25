# Tf even is this?
# class Solution(object):
#     def isValid(self, s):
#         def ok(s):
#             print(s)
#             d = {'(': ')', '{': '}', '[': ']'}
#             slice = []
#             if len(s) == 0:
#                 return True
#             if s.count('[') == s.count(']') and s.count('{') == s.count('}') and s.count('(') == s.count(')'):
#                 if s.count('[') + s.count(']') >= s.count('{') + s.count('}') and s.count('[') + s.count(
#                         ']') >= s.count('(') + s.count(')'):
#                     most_brackets = (s.count('[') + s.count(']')) // 2
#
#                 elif s.count('{') + s.count('}') >= s.count('[') + s.count(']') and s.count('{') + s.count(
#                         '}') >= s.count('(') + s.count(')'):
#                     most_brackets = (s.count('{') + s.count('}')) // 2
#
#                 else:
#                     most_brackets = (s.count('(') + s.count(')')) // 2
#
#                 for i in range(most_brackets):
#                     if s[i] == '(' or s[i] == '{' or s[i] == '[':
#                         slice = s[s.index(s[i]) + 1: s.index(d[s[i]])]
#                         if s[i] not in slice and len(slice) % 2 != 0:
#                             return False
#                         elif s[i] not in slice and len(slice) % 2 == 0:
#                             if slice.count('[') == slice.count(']') and slice.count('{') == slice.count(
#                                     '}') and slice.count('(') == slice.count(')'):
#                                 s = s[:s.index(s[i])] + s[s.index(d[s[i]]):]
#                                 if len(s) == i + 1:
#                                     return True
#
#                             else:
#                                 return False
#
#                         else:
#                             slice = slice.replace(s[i], '')
#                             print(slice)
#                             if len(slice) == 0:
#                                 return True
#                             elif len(slice) % 2 == 1:
#                                 return False
#                             else:
#                                 if slice.count('[') == slice.count(']') and slice.count('{') == slice.count(
#                                         '}') and slice.count('(') == slice.count(')'):
#                                     ok(slice)
#                                 else:
#                                     return False
#                 return False
#
#             else:
#                 return False
#         ok(s)
#
#
# a = Solution()
# print(a.isValid('()[[{(})]]'))



# Wrong
# class Solution(object):
#     def isValid(self, s):
#         d = {'(': ')', '{': '}', '[': ']'}
#
#         if s.count('[') == s.count(']') and s.count('{') == s.count('}') and s.count('(') == s.count(')'):
#             for i in range(len(s)-1):
#                 if s[i] in d.keys():
#                     if s[i + 1] != d[s[i]] and any(s[i + 1] in value for value in d.values()):
#                         return False
#                 else:
#                     continue
#             return True
#         else:
#             return False
#
#
# a = Solution()
# print(a.isValid('({())}'))


# Correct solution
# class Solution(object):
#     def isValid(self, s):
#         d = {'(': ')', '{': '}', '[': ']'}
#         temp = s + '/'
#         result = 0
#
#         if s.count('[') == s.count(']') and s.count('{') == s.count('}') and s.count('(') == s.count(')'):
#             for i in range(len(s)//2):
#                 for k in range(len(temp)):
#                     if temp[k] in d.keys():
#                         if temp[k + 1] == d[temp[k]]:
#                             temp = temp[:k] + temp[k + 2:]
#                             print(temp)
#                             result = 1
#                             break
#                         else:
#                             result = 0
#                             continue
#
#                 if result == 0:
#                     return False
#
#             return True
#
#         else:
#             return False
#
#
# a = Solution()
# print(a.isValid('({)}'))


# Shortest method
# class Solution(object):
#     def isValid(self, s):
#         d = {'(': ')', '{': '}', '[': ']'}
#         temp = []
#         for i in s:
#             if i in d.keys():
#                 temp.append(i)
#             elif temp != [] and i == d[temp[-1]]:
#                 temp.pop()
#             else:
#                 return False
#         return temp == []
#
# a = Solution()
# print(a.isValid('{{)}'))


#My shortest method

class Solution():
    def isvalid(self, s):
        d = {"(": ")", "{": "}", "[": "]"}
        temp = []
        for i in s:
            if i in d.keys():
                temp.append(i)

            elif temp and d[temp[-1]] == i:
                temp.remove(temp[-1])

            else:
                return False

        if temp:
            return False

        return True

a = Solution()
print(a.isvalid("{{}"))
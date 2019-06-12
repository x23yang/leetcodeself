# class Solution:
#     def letterCombinations(self, digits: str) -> list:
#         if digits =='':
#             return ''
#         if digits == '2':
#             return ['a','b','c']
#         if digits == '3':
#             return ['d','e','f']
#         if digits == '4':
#             return ['g','h','i']
#         if digits == '5':
#             return ['j','k','l']
#         if digits == '6':
#             return ['m','n','o']
#         if digits == '7':
#             return ['p','q','r','s']
#         if digits == '8':
#             return ['t','u','v']
#         if digits == '9':
#             return ['w','x','y','z']
#         last = digits[-1]
#         digits = digits[:-1]
#         li = self.letterCombinations(digits)
#         res = []
#         if last == '2':
#             for l in li:
#                 res.extend([l+'a',l+'b',l+'c'])
#         if last == '3':
#             for l in li:
#                 res.extend([l+'d',l+'e',l+'f'])
#         if last == '4':
#             for l in li:
#                 res.extend([l+'g',l+'h',l+'i'])
#         if last == '5':
#             for l in li:
#                 res.extend([l+'j',l+'k',l+'l'])
#         if last == '6':
#             for l in li:
#                 res.extend([l+'m',l+'n',l+'o'])
#         if last == '7':
#             for l in li:
#                 res.extend([l+'p',l+'q',l+'r',l+'s'])
#         if last == '8':
#             for l in li:
#                 res.extend([l+'t',l+'u',l+'v'])
#         if last == '9':
#             for l in li:
#                 res.extend([l+'w',l+'x',l+'y',l+'z'])
#         return res
class Solution:
    def letterCombinations(self, digits: str) -> list:
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if digits =='':
            return []
        if len(digits) ==1:
            return list(dic[digits])
        last = digits[-1]
        digits = digits[:-1]
        li = self.letterCombinations(digits)
        res = []
        for l in li:
            temp = list(dic[last])
            while temp:
                res.extend([l+temp.pop()])
        return res
if __name__=='__main__':
    s=Solution()
    print(s.letterCombinations('23'))

# class Solution:
#     def threeSum(self, nums: list) -> list:
#         res = []
#         while nums:
#             c = nums.pop(0)
#             dic = {}
#             del_list = []
#             for j ,a in enumerate(nums):
#                 b = 0 - c - a
#                 if b in dic:
#                     t = [c,b,a]
#                     t.sort()
#                     if t not in res:
#                         res.append(t)
#                 else:
#                     dic[a] = j
#         return res
class Solution:
    def threeSum(self, nums: list) -> list:
        res = []
        s =set ()
        while nums:
            c = nums.pop(0)
            if c in s:
                continue
            s.add(c)
            dic = {}
            for j ,a in enumerate(nums):
                b = 0 - c - a
                if b in dic:
                    t = [c,b,a]
                    t.sort()
                    if t not in res:
                        res.append(t)
                else:
                    dic[a] = j
        return res
if __name__ =='__main__':
    s=Solution()
    print(s.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))
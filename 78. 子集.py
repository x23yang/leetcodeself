#递归
class Solution:
    def subsets_rc(self, nums: list) -> list:
        if nums == []: return [[]]
        res = []
        last = nums.pop(0)
        for li in self.subsets(nums):
            res.append(li)
            res.append(li+[last])
        return res

    def subsets(self, nums: list) -> list:
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])
        helper(2, [1])
        return res
if __name__=='__main__':
    s=Solution()
    a =[1,2,3]
    print(s.subsets(a.copy()))
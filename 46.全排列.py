class Solution:
    def permute(self, nums: list) -> list:
        if  len(nums) ==1 or len(nums) == 0:
            return [nums]
        res = []
        last = nums.pop()
        li = self.permute(nums)
        for l in li:
            for i in range(len(l)+1):

                temp = l[:]
                temp.insert(i,last)
                res.append(temp)
        return res
if __name__=='__main__':
    s=Solution()
    print(s.permute([1,2,3,4]))
    r=[1,2,3]
    r=r[:-1]
    print(r)
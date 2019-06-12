class Solution:
    def maxSubArray(self, nums: list) -> int:
        sub_sum = nums[0]
        opt = nums[0]
        for i in range(1,len(nums)):
            opt = max (nums[i],opt+nums[i])
            if opt > sub_sum:
                sub_sum = opt
        return sub_sum
if __name__=='__main__':
    s=Solution()
    print (s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

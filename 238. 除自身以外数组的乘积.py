class Solution:
    def productExceptSelf(self, nums: list) -> list:
        left = [nums[0] for _ in range(len(nums))]
        right = [nums[-1] for _ in range(len(nums))]
        res = [0 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            left[i] = left[i-1] * nums[i]
            right[i] = right[i-1] *nums[len(nums)-1-i]
        right.reverse()
        res[0] = right[1]
        res[-1] = left[-2]
        for i in range(1,len(nums)-1):
            res[i] = left[i-1] * right[i+1]
        return res

if __name__ =="__main__":
    s=Solution()
    print(s.productExceptSelf([1,2,3,4]))
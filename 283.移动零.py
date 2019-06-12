class Solution:
    def moveZeroes_1(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zero = 0
        index = 0
        while index < len(nums):
            if nums[index] == 0:
                nums.pop(index)
                count_zero += 1
            else:
                index += 1
        nums.extend([0 for _ in range(count_zero)])
        print(nums)

    def moveZeroes(self, nums: list) -> None:
        count_zero = 0
        for  i in range(len(nums)):
            if nums[i] == 0:
                count_zero += 1
            else:
                nums[i-count_zero] = nums[i]
        for i in range(len(nums)-1,len(nums)-1-count_zero,-1):
            nums[i] = 0
        print(nums)


s=Solution()
s.moveZeroes([0,1,0,3,12])
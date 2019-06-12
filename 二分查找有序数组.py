class Solution:
    def search(self, nums: list, target: int) -> int:
        lenth = len(nums)
        if lenth == 0:
            return
        
        if lenth == 1 and nums[0] == target:
            return 0
        if lenth == 1 and nums[0] != target:
            return 
        if nums[0] <= target <= nums[lenth//2 - 1]:
            if target == nums[lenth//2 - 1]:
                return lenth//2 - 1
            elif target == nums[0]:
                return 0
            else:
                nums[:] = nums[0:lenth//2]
                return self.search(nums,target)
        elif nums[lenth//2] <= target <= nums[lenth-1]:
            if target ==nums[lenth//2]:
                return lenth//2
            elif target ==nums[lenth-1]:
                return lenth-1
            else:
                nums[:] = nums[lenth//2 : ]
                temp = self.search(nums,target)
                if temp:
                    return temp + lenth//2
                else: return None
        else:
            return None
        
s=Solution()
print(s.search([1,2,3,5],4))


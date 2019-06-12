class Solution:
    def search(self, nums: list, target: int) -> int:
        lenth = len(nums)
        if lenth == 1 or not lenth:
            if lenth == 1 and target == nums[0]:
                return 0
            else:
                return 

        def findRotation() -> int:
            lenth = len(nums)
            #while len(nums) >= 2:
            print(nums)
            if nums[lenth //2 ] < nums[lenth // 2 -1] and nums[lenth // 2 ] < nums[lenth // 2 +1]:
                return lenth // 2 
            left = nums[:lenth // 2 ]
            right= nums[lenth // 2:]
            if left[0] > left[-1]:
                return findRotation(left)
            else:
                return findRotation(right) + lenth//2 
        temp = findRotation(nums) 
        print(temp)


s=Solution()
s.search([4,5,6,7,0,1,2],9)
class Solution:
    def binSearch(self,nums: list, target: int) -> int:
        lenth = len(nums)
        if lenth == 0:
            return
        if lenth == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        if lenth == 2 :
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else: return -1
        if nums[0] <= target <= nums[lenth // 2 - 1]:
            if target == nums[lenth // 2 - 1]:
                return lenth // 2 - 1
            elif target == nums[0]:
                return 0
            else:
                nums[:] = nums[0:lenth // 2]
                return self.search(nums, target)
        elif nums[lenth // 2] <= target <= nums[lenth - 1]:
            if target == nums[lenth // 2]:
                return lenth // 2
            elif target == nums[lenth - 1]:
                return lenth - 1
            else:
                nums[:] = nums[lenth // 2:]
                temp = self.binSearch(nums, target)
                if temp == -1:
                    return -1
                else:
                    return temp + lenth // 2
        else:
            return -1
    def search(self, nums: list, target: int) -> int:
        lenth = len(nums)
        if lenth == 1 or not lenth:
            if lenth == 1 and target == nums[0]:
                return 0
            else:
                return -1

        def findRotation(nums:list) -> int:
            lenth = len(nums)
            if lenth == 1:return 0
            if lenth == 2:
                if nums[0] < nums[1]:
                    return 0
                else:
                    return 1
            left = nums[:lenth // 2 ]
            right= nums[lenth // 2:]
            if left[0] > left[-1]:
                return findRotation(left)
            elif right[0] > right[-1]:
                return findRotation(right) + lenth//2
            else:
                if nums[0] <= nums[lenth //2]:
                    return 0
                else: return lenth //2


        start = findRotation(nums)
        #print(start)
        if nums[start] <= target <= nums[-1]:
            temp = self.binSearch(nums[start:],target)
            #print(temp)
            if temp != -1:
                return start+temp
            else:
                return -1
        elif nums[0] <= target <= nums[start-1]:
            return self.binSearch(nums[0:start],target)
        else:
            return -1


s=Solution()
#print(s.binSearch([1,3,5],4.5))
print(s.search([1,3,5],4))
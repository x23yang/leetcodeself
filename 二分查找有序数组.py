#递归二分，存在返回下标，不存在返回-1
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


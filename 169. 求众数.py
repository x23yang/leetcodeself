class Solution:
    def count(self,nums,tar):
        cnt = 0
        for num in nums:
            if num ==tar:
                cnt += 1
        return cnt
    def majorityElement(self, nums: list) -> int:
        li = list(set(nums))
        for l in li:
            if self.count(nums,l) > len(nums)/2:
                return l
        return None
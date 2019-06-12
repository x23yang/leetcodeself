#双指针
class Solution:
    def maxArea(self, height: list) -> int:
        maxArea = 0
        pre = 0
        behind = len(height)-1
        while pre != behind:
            s = min(height[pre],height[behind]) * (behind - pre)
            if s >maxArea:
                maxArea = s
            if height[pre] < height[behind]:
                pre += 1
            else:
                behind -=1
        return maxArea
if __name__ =='__main__':
    s=Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
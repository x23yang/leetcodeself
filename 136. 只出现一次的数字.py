class  Solution:
    def singleNumber(self, nums: list) -> int:
        s = set()
        for num in nums:
            if num in s:
                s.discard(num)
            else:
                s.add(num)
        return s.pop()
if __name__ =="__main__":
    s  = Solution()
    print(s.singleNumber([4,1,2,1,2]))
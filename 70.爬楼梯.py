class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        list = [ 0  for i in range(n)]
        list[0] = 1
        list[1] = 2
        for i in range (2,n):
            list[i] = list[i-1] + list[i-2]
        return list[-1]
    def rec_s(self,n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.rec_s(n-1)+self.rec_s(n-2)
if __name__=="__main__":
    s=Solution()
    print(s.climbStairs(5))
    print(s.rec_s(5))
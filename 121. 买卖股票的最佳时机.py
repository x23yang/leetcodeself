#递归
class Solution:
    def find_min(self,price,n):
        min = price[0]
        index = 0
        for i in range(1,n):
            if price[i] < min :
                min = price[i]
                index = i
        return index
    def rec_s(self,price,n):
        if n == 0:
            return 0
        else:
            return max (self.rec_s(price,n-1),price[n]-price[self.find_min(price,n)])
    def maxProfit(self, prices: list) -> int:
        if prices == []:
            return 0
        return self.rec_s(prices,len(prices)-1)

if __name__=="__main__":
    li = [7,1,5,3,6,4]
    s=Solution()
    print(s.maxProfit(li))
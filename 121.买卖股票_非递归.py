class Solution():
    def maxProfit(self, prices: list) -> int:
        if prices == []:
            return 0
        li = [0 for i in range(len(prices)) ]
        min = prices[0]
        min_index = 0
        for i in range(1,len(prices)):
            li[i] = max(li[i-i],prices[i]-prices[min_index])
            if prices[i] < min :
                min = prices[i]
                min_index = i
        return max(li)
if __name__=='__main__':
    s=Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
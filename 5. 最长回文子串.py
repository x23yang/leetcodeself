class Solution:
    def longestPalindrome(self, s: str) -> str:
        li = [[False for _ in range(len(s))] for _ in range(len(s))]
        #初始化
        for i in range(len(s)):
            for j in range(i,len(s)):
                if i == j:
                    li[i][j] = True
                elif i == j-1:
                    if s[i] == s[j]:
                        li[i][j] =True
        # #迭代,按对角线到右上顶点访问
        for dif in range(2,len(s)):
            for sta in range(len(s)-dif):
                if li[sta+1][sta+dif-1] == True and s[sta]==s[sta+dif]:
                    li[sta ][sta + dif ] =True
        max_len = 0
        start = 0
        end = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if li[i][j] ==True and (j-i) > max_len:
                    max_len = j-i
                    start ,end = i , j
        return s[start:end+1]
if __name__ =="__main__":
    s=Solution()
    temp = 'abcba'
    print(s.longestPalindrome(temp))
    dp = [0] * 5 
    print(dp)

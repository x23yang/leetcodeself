class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='' or num2=='':
            return 0
        n1 = len(num1)-1
        n2 = len(num2)-1
        a = 0
        b = 0
        for i in range(len(num1)):
            a = (ord(num1[i])-ord('0'))*10**n1 +a
            n1 -=1
        for i in range(len(num2)):
            b = (ord(num2[i])-ord('0'))*10**n2 +b
            n2 -=1
        return a*b
if __name__=="__main__":
    s=Solution()
    print(s.multiply('12','0'))
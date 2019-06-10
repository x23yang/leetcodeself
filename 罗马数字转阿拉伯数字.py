class Solution:
    def romanToInt(self, s: str) -> int:
        list_s = list(s)
        value = 0
        last =0
        a = { 'I' : 1 , 'V' : 5 , 'X' : 10 , 'L' : 50 ,'C' : 100 ,'D' :500 , 'M' : 1000 } 
        while list_s:
            current = list_s.pop()
            if a[current] >= last:
                value = a[current]+value
            else:
                value = value - a[current]
            last = a[current]
        return value       

if __name__ == "__main__":
    s=Solution()
    print(s.romanToInt('III'))
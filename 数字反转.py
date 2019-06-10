class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        if x > 0:  
            re_x = str_x [::-1]
            if int (re_x.lstrip('0'))<= 2**31-1:
                return int (re_x.lstrip('0')) 
            else: 
                return 0 
        if x < 0:
            re_x=str_x[::-1]
            if int ( re_x.lstrip('0').rstrip('-'))>= -2**31:
                return -int ( re_x.lstrip('0').rstrip('-'))
            else :
                return 0 
        if x== 0:
            return 0


if __name__ == "__main__":
    s=Solution()
    print (s.reverse(-18820))   
class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:'X',
            40:'XL',
            50:'L',
            90:'XC',
            100:'C',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M'
        }
        res =  ''
        while num:
            while num >= 1000:
                res = res + dic[1000]
                num = num -1000
            if num >= 900:
                res = res +dic[900]
                num = num - 900
            if num >= 500:
                res = res +dic[500]
                num = num - 500
            if num >= 400:
                res = res +dic[400]
                num = num - 400
            while  num >= 100:
                if num >= 100:
                    res = res +dic[100]
                    num = num - 100
            if num >= 90:
                res = res +dic[90]
                num = num - 90
            if num >= 50:
                res = res +dic[50]
                num = num - 50
            if num >= 40:
                res = res +dic[40]
                num = num - 40
            while num>=10:
                if num >= 10:
                    res = res +dic[10]
                    num = num - 10
            if num >= 9:
                res = res +dic[9]
                num = num - 9
            if num >= 5:
                res = res +dic[5]
                num = num - 5
            if num >= 4:
                res = res +dic[4]
                num = num - 4
            while num >=1:
                if num >= 1:
                    res = res +dic[1]
                    num = num - 1
        return res
if __name__=='__main__':
    s=Solution()
    print(s.intToRoman(3000))
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_x = bin(x)[2:]
        bin_y = bin(y)[2:]
        if len(bin_x) < len(bin_y):
            bin_x = bin_x.rjust(len(bin_y),'0')
        else:
            bin_y = bin_y.rjust(len(bin_x),'0')
        count = 0
        for i in range(len(bin_x)):
            if bin_x[i] != bin_y[i]:
                count += 1
        return count


s=Solution()
print(s.hammingDistance(1,4))
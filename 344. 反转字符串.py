class Solution:
    def reverseString(self, s:list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i],s[len(s)-1-i] = s[len(s)-1-i],s[i]
        print(s)
if __name__ == "__main__":
    s=Solution()
    s.reverseString(["h","e","l","l","o"])
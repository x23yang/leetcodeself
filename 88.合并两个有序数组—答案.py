class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        point_num1 = m-1
        point_num2 = n-1
        count = 0
        while point_num1 > -1 and point_num2 > -1:
            if nums2[point_num2] > nums1[point_num1]:
                nums1[m+n-1-count] = nums2[point_num2]
                count += 1
                point_num2 -= 1
                print('-',nums1)
            else:
                nums1[m+n-1-count] = nums1[point_num1]
                count += 1
                point_num1 -= 1
                print('--',nums1)
        if point_num1 == -1:
            nums1[0:m+n-count] = nums2[0:point_num2+1]
            print(nums1)
if __name__=='__main__':
    s=Solution()
    #s.merge([1,2,3,0,0,0],3,[2,5,6],3)
    s.merge([4, 0, 0, 0, 0, 0], 1, [1, 2, 3,5,6], 5)
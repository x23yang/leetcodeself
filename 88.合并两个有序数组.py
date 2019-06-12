class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        insert_success = 0
        for i in range(n):
            for j in range(m+n):
                if nums2[i] <= nums1[j]:
                    nums1.insert(j,nums2[i])
                    nums1.pop(-1)
                    insert_success += 1
                    break
        for i in range(insert_success):
            nums2.pop(0)
        if nums2 != []:
            for i in range(len(nums2)):
                nums1.pop(-1)
            nums1.extend(nums2)
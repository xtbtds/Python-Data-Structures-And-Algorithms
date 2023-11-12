class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i1=m-1
        i2=n-1
        index=m+n-1
        while i2 >= 0:
            if i1 >= 0 and nums1[i1] > nums2[i2]:
                nums1[index] = nums1[i1]
                i1 -= 1
                index -= 1
            else:
                nums1[index] = nums2[i2]
                i2 -= 1
                index -= 1
            

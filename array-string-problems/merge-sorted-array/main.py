class Solution(object):
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        nums1_index = m - 1
        nums2_index = n - 1
        current_index = m + n - 1

        while nums2_index >= 0:
            if nums1_index >= 0 and nums1[nums1_index] > nums2[nums2_index]:
                nums1[current_index] = nums1[nums1_index]
                nums1_index -= 1
            else:
                nums1[current_index] = nums2[nums2_index]
                nums2_index -= 1
            current_index -= 1

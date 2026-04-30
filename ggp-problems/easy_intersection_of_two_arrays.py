from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        inter = counter1 & counter2

        res = []
        for i in inter:
            res.extend([i] * inter[i])

        return res


"""
Follow ups:

What if the given array is already sorted? How would you optimize your algorithm?
- I would use the two pointer approach. I would initialize the pointers in the beginning of both arrays. If the values of the pointers are the same, I will add that value to my result array, and move both pointers forward. If they are not the same, I will move the smaller pointer forward and continue. I will then stop when the smallest array is finished or if they are the same size until the end of both arrays.
What if nums1's size is small compared to nums2's size? Which algorithm is better?
- If one array's size is smaller compared to the other, the two pointer approach is best if the array is sorted. If the arrays are not sorted the best time complexity will be O(n + m) since we would have to check all elements in both arrays. In that case my counter approach might be easier to implement.
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
- The counter method is best for this scenario. I can keep track of the char count for each of the arrays as I stream the data. Then once I reach the end of the arrays, I can compare the counts and build my result array.
"""

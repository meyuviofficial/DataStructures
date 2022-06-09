class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0

        buff = nums1[:m]

        for x in range(m+n):

            if j >= n or (i < m and buff[i] <= nums2[j]):
                nums1[x] = buff[i]
                i += 1
            else:
                nums1[x] = nums2[j]
                j += 1

"""
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""

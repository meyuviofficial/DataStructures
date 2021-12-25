class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ref = set(nums)

        if len(nums) == len(ref):
            return False
        else:
            return True

"""
Example 1
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Example 2
Input: nums = [1,2,3,4]
Output: false

"""
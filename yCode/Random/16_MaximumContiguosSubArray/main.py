class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = nums[0]
        max_sum = nums[0]

        n = len(nums)
        for i in range(1, n):
            curr_max = max(nums[i], curr_max + nums[i])
            max_sum = max(curr_max, max_sum)

        return max_sum

"""
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

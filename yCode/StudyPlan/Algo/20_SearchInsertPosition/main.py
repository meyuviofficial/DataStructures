class Solution:
    # def findPosition(nums: List[int], target: int) -> int:
        
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        
        
        while low <= high:
            mid = low + (high - low) // 2
            print(nums[mid])
            if nums[mid] == target:
                return mid
            if target >= nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            
        return low

"""
Example 1
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 2
Input: nums = [1,3,5,6], target = 5
Output: 2
"""

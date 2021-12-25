class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = list()
        reference = dict()

        for i in range(len(nums)):
            if target-nums[i] in reference:
                result.append(reference[target-nums[i]])
                result.append(i)
            else:
                reference[nums[i]] = i

        return result
"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
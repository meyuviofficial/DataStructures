class Solution:
    def BinarySearch(self, nums: List[int], target: int, start: int, end: int) -> int:
        # print(nums)
        if end >= start:
            mid = (start+end)//2
            if target == nums[mid]:
                return mid
            for i in range(start, end):
                if target <= nums[mid]:
                    return self.BinarySearch(nums, target, start, mid)
                else:
                    return self.BinarySearch(nums, target, mid+1, end)
        else:
            return -1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        return self.BinarySearch(nums, target, 0, len(nums)-1)
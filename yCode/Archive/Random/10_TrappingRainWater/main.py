class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        leftMax = [0]*n
        leftMax[0] = height[0]

        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i])

        rightMax = [0]*n
        rightMax[n-1] = height[n-1]
        for j in range(n-2, -1, -1):
            rightMax[j] = max(rightMax[j+1], height[j])

        capacity = 0
        for x in range(n):
            capacity += min(leftMax[x], rightMax[x])-height[x]

        return capacity

"""
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
"""
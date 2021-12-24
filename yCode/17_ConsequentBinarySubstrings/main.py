class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        prev, curr, ans = 0, 1, 0
        
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                ans += min(prev,curr)
                prev, curr = curr, 1
            else:
                curr+=1
                
        return ans+min(curr,prev)

"""
Example 1: 
Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:
Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
"""
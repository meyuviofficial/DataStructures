class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        upperlimit = ceil((2*n + 0.25) ** 0.5 - 0.5)+1
        
        for i in range(1,upperlimit):
            n -= i
            if n%i == 0:
                count += 1
        return count



"""
Example 1

Input: n = 15
Output: 4
Explanation: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

Example 2
Input: n = 9
Output: 3
Explanation: 9 = 4 + 5 = 2 + 3 + 4


"""
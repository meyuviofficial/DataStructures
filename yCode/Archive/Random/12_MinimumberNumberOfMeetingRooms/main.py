class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        start = list()
        end = list()
        buffer = list()

        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])
        end.sort()

        count = 0

        start_pointer = 0
        end_pointer = 0

        while start_pointer < len(start):
            if start[start_pointer] >= end[end_pointer]:
                count -= 1
                end_pointer += 1

            count += 1
            start_pointer += 1

        return count

"""
Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
"""
class Solution:
    def majorityElement(self, A, N):
        TargetCount = int(N/2)
        
        ref = dict()
        for i in range(N):
            if A[i] not in ref:
                ref[A[i]]=1
            else:
                ref[A[i]]+=1
                
        for key,value in ref.items():
            if value > TargetCount:
                return key
        
        return -1

"""
Input: Array will be given
Output: Find the element that occurs more than N/2 times, where N is the size of the array.
"""
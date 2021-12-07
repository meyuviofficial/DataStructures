import math
class Solution:
    def productExceptSelf(self, a, n):
        #code here
        prod=1
        flag=0
        for i in range(n):
            if a[i]==0:
                flag+=1
            else:
                prod*=a[i]
        
        for i in range(n):
            if flag>1:
                a[i]=0
            elif flag==0:
                a[i]=int(prod/a[i])
            elif flag==1 and a[i]!=0:
                a[i]=0
            else:
                a[i]=prod
        
        return a

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends

"""
Input:
n = 5
nums[] = {10, 3, 5, 6, 2}
Output:
180 600 360 300 900
Explanation: 
For i=0, P[i] = 3*5*6*2 = 180.
For i=1, P[i] = 10*5*6*2 = 600.
For i=2, P[i] = 10*3*6*2 = 360.
For i=3, P[i] = 10*3*5*2 = 300.
For i=4, P[i] = 10*3*5*6 = 900.

Input:
n = 2
nums[] = {12,0}
Output:
0 12
"""
 #Function to count the frequency of all elements from 1 to N in the array.
 def frequencyCount(self, arr, N, P):
      # code here

      ref = dict()

       for i in range(N):
            if arr[i] in ref:
                ref[arr[i]] = ref[arr[i]]+1
            else:
                ref[arr[i]] = 1

        for i in range(1, N+1):
            if i in ref:
                arr[i-1] = ref[i]
            else:
                # arr[i-1]
                arr[i-1] = 0
                # print("Not Present!!")
        # print(arr)


#{
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == "__main__":
    T = int(input())
    while(T > 0):
        N = int(input())
        arr = [int(x) for x in input().strip().split()]
        P = int(input())
        ob = Solution()
        ob.frequencyCount(arr, N, P)
        for i in arr:
            print(i, end=" ")
        print()
        T -= 1


# } Driver Code Ends

"""
Input:
N = 5
arr[] = {2, 3, 2, 3, 5}
P = 5
Output:
0 2 2 0 1
Explanation: 
Counting frequencies of each array element
We have:
1 occurring 0 times.
2 occurring 2 times.
3 occurring 2 times.
4 occurring 0 times.
5 occurring 1 time.
"""
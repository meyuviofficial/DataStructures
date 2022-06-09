
class Solution:
    def increment(self, arr, N):
        i=N-1
        ans = list()
        carry=0
        
        while i>=0:
            # print("i Value is :",i)
            if i==N-1:
                curr_sum=arr[i]+1
            else:
                curr_sum=arr[i]+carry
                
            carry = int(curr_sum/10)
            actual_sum = int(curr_sum%10)
            ans.append(actual_sum)
            # print("Actual Sum : ",actual_sum)
            i-=1
        # code here
        None if carry==0 else (ans.append(carry))
        return ans[::-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        ptr = ob.increment(arr,N)
        for i in ptr:
            print(i,end=" ")
        print()
# } Driver Code Ends

# Input : [1 2 5]
# Output : Add 1 and return [1 2 6]
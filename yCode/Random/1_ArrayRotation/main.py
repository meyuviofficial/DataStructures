class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction.
    def GCD(self,a,b):
        if b==0:
            return a
        else: 
            return self.GCD(b,a%b)
    
    def rotateArr(self,A,D,N):
        #Your code here
        D=D%N
        
        x=self.GCD(N,D)
        for i in range(x):
            temp=A[i]
            j=i
            
            while True:
                k=j+D
                if k>=N:
                    k=k-N
                if k==i:
                    break
                A[j]=A[k]
                j=k
            A[j]=temp
def solve(A):
        if A==A[::-1]:
            return 0
        else:
            temp=A[::-1]
            s=A
            i=len(temp)-1
            while(i>=0):
                s+=temp[i:]
                if s==s[::-1]:
                    return len(temp[i:])
                else:
                    s=A
                i-=1
print(solve(A))
==>TC=O(len(A)) and SC=O(A)

#another O(n) approach
def ispal(A,i,j):
    c=0
    
    while i<j:
        if A[i]!=A[j]:
            return 0
        i+=1
        j-=1
    return 1


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        i=0
        j=len(A)-1
        c=0
        
        while i<j:
            if A[i]==A[j]:
                if ispal(A,i,j):
                    return c
            i+=1
            c+=1
            
        return c




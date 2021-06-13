def solve(A):
        count=0
        i=0
        j=len(A)-1
        while(i<=j):
            if A[i]==A[j]:
                i+=1
                j-=1
            elif A[i+1]==A[j]:
                i+=1
                count+=1
            else:
                count+=1
                j-=1
        if count>1:
            return 0
        else:
            return 1
print(solve("abecba")) 
==>O(len(A))

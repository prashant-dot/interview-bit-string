def solve(self, A):
        c=0
        for i in range(len(A)):
            if A[i]=='a' or A[i]=='e' or A[i]=='i' or A[i]=='o' or A[i]=='u' or A[i]=='A' or A[i]=='E' or A[i]=='I' or A[i]=='O' or A[i]=='U':
                c+=len(A)-i    
        return c%10003
==> O(n)        

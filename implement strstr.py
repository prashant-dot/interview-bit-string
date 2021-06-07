def strStr(self, A, B):
        n=len(A)
        m=len(B)
        if n==0:
            return -1
        if m==0:
            return -1
        i=0
        while(i<n-m+1):
            if A[i:i+m]==B:
                return i
            i+=1
        return -1
==> O(n)        

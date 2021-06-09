def multiply(self, A, B):
        lenA=len(A)-1
        lenB=len(B)-1
        numA=0
        numB=0
        for i in A:
            numA+=int(i)*10**lenA
            lenA-=1
        for i in B:
            numB+=int(i)*10**lenB
            lenB-=1
        return str(numA*numB)
==> O(n+m)

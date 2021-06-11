def power( A):
        l=len(A)-1
        a=0
        for i in range(len(A)):
            a+=int(A[i])*10**l
            l-=1
        if a%2!=0:
            return 0
        
        else:
            while a!=1:
                if a%2==0:
                    a=a//2
                else:
                    return 0
        return 1
print(power("123"))
==> O(k) where k is power of base 2

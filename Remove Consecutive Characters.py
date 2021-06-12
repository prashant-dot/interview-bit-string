
def solve(A, B):
    i=0
    a=""
    while i<len(A):
        if i<=len(A)-B:
            k=A[i:i+B]
            c=False
            for j in range(0,len(k)-1):
                if k[j]!=k[j+1]:
                    c=True
                    break
            if c is False:
                i=i+B
            else:
                a+=A[i]
                i+=1
        else:
            a+=A[i]
            i+=1
    return a
print(solve("abbccd", 2))
==>TC = O(len(A)*B) and SC = O(len(A))

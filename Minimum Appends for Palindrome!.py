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

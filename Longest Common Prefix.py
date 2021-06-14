def longestCommonPrefix(A):
        if len(A)==1:
            return A[0]
        else:
            j=0
            c=True
            s=""
            while(c):
                for i in range(1,len(A)):
                    if j>=len(A[i]) or j>=len(A[0]) or A[i][j]!=A[0][j]:
                        c=False
                        break
                else:
                    s+=A[0][j]
                if c==False:
                    break
                j+=1
            return s
print(longestCommonPrefix(["jkfsdfs","jkd","jklwdw"]))
==>O(len(A)*len(str))

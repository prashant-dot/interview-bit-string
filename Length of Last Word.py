def lengthOfLastWord(A):
        count=0
        A=A.strip()
        for i in range(len(A)-1,-1,-1):
            
            if A[i]!=" ":
                count+=1
            else:
                break
        return count
print(lengthOfLastWord("qsdb dqjbdij iqnsdni   "))
==>O(len(A))

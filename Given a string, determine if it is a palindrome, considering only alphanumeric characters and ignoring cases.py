class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        A=A.lower()
        dic={',':233,' ':232,'!': 9, '\xa3': 7, '\xa2': 20, '%': 4, '$': 5, "'": 12, '&': 2, ')': 42, '(': 0, '+': 40, '*': 1, '-': 17, '/': 10,  ':': 34, '=': 16, '<': 25, '?': 21, '>': 23, '@': 8, '\xc2': 19, '#': 18, '"': 32, '[': 15, ']': 14, '\\': 13, '_': 41, '^': 3, '`': 11, '{': 38, '}': 36, '|': 29, '~': 27}
        i=0
        j=len(A)-1
        str1=""
        str2=""
        while(i<=j):
            if A[i] in dic:
                i+=1
                continue
            else:
                str1+=A[i]
                i+=1
        i=0
        j=len(A)-1
        while(i<=j):
            if A[j] in dic:
                j-=1
                continue
            else:
                str2+=A[j]
                j-=1
        #print(str1,str2)
        if str1==str2:    
            return 1
        else:
            return 0
          
 ==> TC=O(n) and SC=O(n)

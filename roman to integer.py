def romanToInt( A):
       
        d = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        ans = 0
        for i in range(len(A)-1):
            if d[A[i]] < d[A[i+1]]:
                ans -= d[A[i]]
            else:
                ans += d[A[i]]
        ans += d[A[len(A)-1]]
        return ans
 print(romanToInt( IVXLCDM))
 ==>TC=O(n)

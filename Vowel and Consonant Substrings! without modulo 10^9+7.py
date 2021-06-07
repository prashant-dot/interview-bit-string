def solve(self, A):
    vow = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
    cons = {"b": 1, "c": 1, "d": 1, "f": 1, "g": 1, "h": 1, "j": 1, "k": 1, "l": 1, "m": 1, "n": 1, "p": 1, "q": 1,
            "r": 1, "s": 1, "t": 1, "v": 1, "w": 1, "x": 1, "y": 1, "z": 1}
    tempdic = {}
    temp = 0
    for i in range(len(A) - 1):
        if A[i] in vow:
            temp = 1
        else:
            temp = 0
        j = i + 1
        while (j < len(A)):
            if temp == 1:
                if A[j] in cons:
                    if A[i:j + 1] in tempdic:
                        tempdic[A[i:j + 1]] += 1
                    else:
                        tempdic[A[i:j + 1]] = 1

            else:
                if A[j] in vow:
                    if A[i:j + 1] in tempdic:
                        tempdic[A[i:j + 1]] += 1
                    else:
                        tempdic[A[i:j + 1]] = 1

            j += 1
    return len(tempdic.keys())
    ==>TC=O(n) and SC=O(n)

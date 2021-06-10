def compareVersion(A, B):
        listA=[int(x) for x in A.split(".")]
        listB=[int(x) for x in B.split(".")]
        if len(listA)>len(listB):
            Z=len(listA)-len(listB)
            for j in range(Z):
                listB.append(0)
        else:
            Z=len(listB)-len(listA)
            for j in range(Z):
                listA.append(0)
        if listA==listB:
            return 0
        i=0
        while(i<len(listA)):
            if listA[i]>listB[i]:
                return 1
            elif listA[i]<listB[i]:
                return -1
            else:
                i+=1
print(compareVersion("12.23.32","22.4"))
==> O(max(len(A),len(B)))

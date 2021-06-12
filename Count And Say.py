def countAndSay(A):
        if A==1:
            return "1"
        else:    
            temp="11"
            t=""
            for i in range(2,A):
                j=0
                count=1
                while j<len(temp)-1:
                    if temp[j]==temp[j+1]:
                        j+=1
                        count+=1
                    else:
                        t+=str(count)+temp[j]
                        j+=1
                        count=1
                t+=str(count)+temp[-1]
                
                temp=t
                t=""
            return temp
print(countAndSay(5))
==>O(A*len(current count and sequence value))

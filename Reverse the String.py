def solve( A):
        A=A.strip()
        list1=A.split(" ")
        s=""
        i=len(list1)-1
        while(i>=0):
            if list1[i]=='':
                pass
            else:
                s+=list1[i]+' '
            i-=1
        return s.strip()
print(solve("dsv dsvf dsfdf df    dsf df  fd s   dsf sdf     "))
==>TC=O(n) and SC=O(n)

def restoreIpAddresses(self, s):
        def is_valid(ip):
            ip = ip.split(".")
            for i in ip:
                if (len(i) > 3 or int(i)<0 or int(i) > 255):
                    return False
                if len(i) > 1 and int(i) == 0:
                    return False
                if (len(i) > 1 and int(i) != 0 and
                    i[0] == '0'):
                    return False
            return True
        
        stringlenth = len(s)
        if stringlenth > 12:
            return []
        temp = s
        l = []
        for i in range(1, stringlenth - 2):
            for j in range(i + 1, stringlenth - 1):
                for k in range(j + 1, stringlenth):
                    temp = temp[:k] + "." + temp[k:]
                    temp = temp[:j] + "." + temp[j:]
                    temp = temp[:i] + "." + temp[i:]
                    if is_valid(temp):
                        l.append(temp)
                         
                    temp = s
                     
        return l

        
        
            
==>TC=O(n^3) and SC = O(n)

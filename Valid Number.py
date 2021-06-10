def isNumber(self, A):
        try:
            x=float(A)
            y=A.split('e')
            for ele in y:
                if ele=="":
                    return 0
                if ele[-1]==".":
                    return 0
                
            return 1
        except:
            return 0
==> O()

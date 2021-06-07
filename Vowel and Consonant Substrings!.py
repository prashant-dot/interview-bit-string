class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        vowdic={"a":1,"e":1,"i":1,"o":1,"u":1}
        condic={"b":1,"c":1,"d":1,"f":1,"g":1,"h":1,"j":1,"k":1,"l":1,"m":1,"n":1,"p":1,"q":1,"r":1,"s":1,"t":1,"v":1,"w":1,"x":1,"y":1,"z":1}
        vow=0
        con=0
        NoOfString=0
        for i in A:
            if i in vowdic:
                vow+=1
                NoOfString+=con
            else:
                con+=1
                NoOfString+=vow
            NoOfString%=1000000007
        return NoOfString
    ==> O(n)

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        s=[]
        temp=A
        while(temp):
            s.append(temp.val)
            temp=temp.next
        k=[s[i] for i in range(len(s)-1,-1,-1) ]
        if k==s:
            return 1
        return 0
==>TC=O(n) and SC=O(n) where n is lenth of linked list

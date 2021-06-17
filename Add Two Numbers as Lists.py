# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        list1=[]
        list2=[]
        temp1,temp2=A,B
        while(temp1):
            list1.append(temp1.val)
            temp1=temp1.next
        while(temp2):
            list2.append(temp2.val)
            temp2=temp2.next
        list1.reverse()
        list2.reverse()
        n1=int("".join([str(i) for i in list1]))
        n2=int("".join([str(i) for i in list2]))        
        list3=str(n1+n2)[::-1]
        new=ListNode(list3[0])
        temp=new
        i=1
        while(i<len(list3)):
            temp.next=ListNode(list3[i])
            temp=temp.next
            i+=1
        return new
 ==>TC=O(n) and SC=O(n) where n is lenth of max(linked list 1, 2)

'''
    # Node Class
    class Node:
         def __init__(self, data):
             self.data = data
             self.next = None
    
'''

class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        if head==None:
            return False

        slowptr =head
        fastptr =head

        while fastptr!=None and fastptr.next!=None:
            slowptr=slowptr.next
            fastptr=fastptr.next.next

            if slowptr==fastptr:
                return True

        return False
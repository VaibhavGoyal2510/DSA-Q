#User function Template for python3
'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    #Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):
        # code here
        # edit the linked list
        temp = head
        
        while temp:
            # print(temp.data)
            if temp.data==x:
                # print("Helo")
                if temp.prev==None:
                    head=temp.next
                    t2=temp.next
                    t2.prev=None
                    # temp.next=None
                    
                elif temp.next==None:
                    t2=temp.prev
                    t2.next=None
                    # temp.prev=None
                    
                else:
                    pre = temp.prev
                    nec=temp.next
                    
                    pre.next= temp.next
                    nec.prev=temp.prev
                    
            temp=temp.next
            
        return head
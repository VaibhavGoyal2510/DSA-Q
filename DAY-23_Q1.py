
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def insertionSort(self, head):
        #code here
        # This takes  O(N)+O(NlogN)+ O(N)
        # & space as O(N)
        # if head == None or head.next==None:
        #     return head
            
        # temp =head
        # l=[]
        # while temp:
        #   l.append(temp.data)
        #   temp=temp.next
           
        # # print(l)
        # l.sort()
        # temp=head
        # i=0
        # while temp and i<len(l):
        #     temp.data = l[i]
        #     i+=1
        #     temp=temp.next
        
        # return head
            
        
        # Merge sort Solution
        def findMid(head):
            slow=head
            fast=head.next
            
            while fast!=None and fast.next!=None:
                slow=slow.next
                fast=fast.next.next
                
            return slow
        
        
        def MergeSort(head):
            if (head == None) or head.next==None:
                return head;
                
            mid = findMid(head)
            left = head
            right=mid.next
            mid.next=None
            
            leftNode = MergeSort(left)
            rightNode= MergeSort(right)
            
            return merge(leftNode,rightNode)
            
        def merge(list1,list2):
            dummy = Node(-1)
            
            temp = dummy
            
            while list1!=None and list2 !=None:
                if list1.data<list2.data:
                    temp.next=list1
                    temp=list1
                    list1=list1.next
                    
                else:
                    temp.next=list2
                    temp=list2
                    list2=list2.next
                    
                
            if list1 :
                temp.next=list1
                
            else:
                temp.next=list2
                
            return dummy.next
            
        return MergeSort(head)
                    
            
# Please change the array in-place
class Solution:
    def insertionSort(self, arr):
        #code here
        # pos=0
        
        for i in range(len(arr)):
            j=i
            
            while(j>0 and arr[j]<arr[j-1]):
                arr[j],arr[j-1]=arr[j-1],arr[j]
                j-=1
                
        return arr
    
    def bubbleSort(self,arr):
        # code here
        for i in range(len(arr)-1,-1,-1):
            didswap = 0
            for j in range(0,i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    didswap=1
                    
            if didswap == 0:
                break
                    
        return arr
    
    def selectionSort(self, arr):
        #code here
        
        
        for i in range(len(arr)):
            pos=i
            
            for j in range(i+1,len(arr)):
                if arr[j]<arr[pos]:
                    pos=j
                    
            arr[pos],arr[i]=arr[i],arr[pos]
            
        return arr
# reverseInGroups
def reverseInGroups(self, arr, k):
        #code here
        
        for i in range(0,len(arr),k):
            left = i
            right = min(i+k,len(arr))
            
            arr[left:right] = arr[left:right][::-1]
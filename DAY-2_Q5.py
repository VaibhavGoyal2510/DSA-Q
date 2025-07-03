# remove duplicates in place from sorted array

def removeDuplicates(self, arr):
        #Code Here
        # This code takes time that is time limit exceeded
        # left=0
        # while left<len(arr)-1:
        #     if arr[left]==arr[left+1]:
        #         arr.pop(left+1)
                
        #     else: 
        #         left+=1
        
        # return len(arr)
        
        if len(arr)==1:
            return 1
        
        left=0
        right=1
        while right < len(arr):
            if arr[left]!=arr[right]:
                left+=1
                arr[left]=arr[right]
                right+=1
            else:
                right+=1
        
        return left+1
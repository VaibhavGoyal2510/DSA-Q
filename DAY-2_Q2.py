# Wave Array

def sortInWave(self, arr):
        # code here
        
        for i in range(0,len(arr),2):
            # print(i)
            left=i
            right=i+1
            
            if left==len(arr)-1 or right>len(arr)-1:
                break
            
            arr[left],arr[right]=arr[right],arr[left]
            
        # print(arr)
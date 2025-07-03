# Rotate Array
#Function to rotate an array by d elements in counter-clockwise direction. 
def rotateArr(self, arr, d):
    #Your code here
    
    # d=d%size of array
    # One approach could be taking the first d elements in an auxilliary array
    # Which is i=0 to i < d 
    
    # Then Shifting rest to left 
    # so start with i = d & do a[i-d] = a[i]
    
    # Then finally add the auxiliarry array elements to this array again
    
    # start from i = n-d ;i<n;i++ 
    # a[n-d] = b[i-(n-d)]
    
    
    # Now other solution to reverse in groups of d & n-d & then finally reversing 
    # the whole again
    
    # If have to write the reverse(left,right)
    # while(left<=right){
        #temp = arr[left]
        # arr[left]=arr[right]
        # arr[right]=arr[left]
        # left+=1
        # right-=1
    # }
    d=d%len(arr)
    
    arr[0:d] = arr[0:d][::-1]
    arr[d:len(arr)]=arr[d:len(arr)][::-1]
    arr[:len(arr)]=arr[0:len(arr)][::-1]
# pushZerosToEnd

def pushZerosToEnd(self,arr):
    # code here
    index = 0
    count=0
    for num in arr:
        if num==0:
            count+=1
        
        else:
            arr[index]=num
            index+=1
        
    while(count>0):
        arr[index]=0
        index+=1
        count-=1
    
    return arr
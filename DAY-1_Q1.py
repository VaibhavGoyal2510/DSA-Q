# Third Largest 

def thirdLargest(self,arr):
    # code here
    if len(arr)<3:
        return -1
        
    lar,sec,third=0,0,0
    
    for num in arr:
        if num>=lar:
            third=sec
            sec=lar
            lar=num
        
        elif num>=sec and num< lar:
            third=sec
            sec=num
        
        elif num>=third and num<sec:
            third=num
    
    return third if third!=0 else -1
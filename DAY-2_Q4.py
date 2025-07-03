# Check if array is sorted

def arraySortedOrNot(self, arr) -> bool:
        # code here
        # t=0
        for i in range(len(arr)-1):
            if arr[i]<=arr[i+1]:
                continue
            else:
                return False
                
        return True
class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        left=0
        right = len(arr)-1

        while left<=right:
            mid = (left+right)//2

            if arr[mid]==target:
                temp=mid
                while temp>=0 and arr[temp]==target:
                    temp-=1
                l=temp+1
                while mid<len(arr) and arr[mid]==target:
                    mid+=1
                r=mid-1
                return [l,r]

            elif arr[mid]>target:
                right=mid-1
            else:
                left=mid+1

        return [-1,-1]

            
        
class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        
        top=left=0
        
        right=m-1
        bottom = n-1
        ans=[]
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                ans.append(mat[top][i])
            
            top+=1
            for i in range(top,bottom+1):
                ans.append(mat[i][right])
                
            right-=1
            
            if top<=bottom:
                for i in range(right,left-1,-1):
                    ans.append(mat[bottom][i])
                    
                bottom-=1
                
            if left<=right:
                for i in range(bottom,left,-1):
                    ans.append(mat[i][left])
                    
                left+=1 
        
        # print(ans)
        return ans
        
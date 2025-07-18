class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #  Sabse pehle transpose 
        n=len(mat)
        for i in range(0,n-1):
            for j in range(i+1,n):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
                
        
        print(mat)
        
        # step two -> reverse each row
        for l in mat:
            l[0:n]=l[0:n][::-1]
        
class Solution:
    def get(self, a: int, b: int) -> tuple[int, int]:
        # code here
        # temp=0
        # if b<a:
        #     temp=a^b
        #     a=a&b
        #     b=b^temp
        # else: 
        #     temp=a^b
        #     print(temp)
        #     b=a&b
        #     print(b)
        #     a=a^temp
        
        # print("ab-> ",a,b)
        
        a=a^b
        b=a^b
        a=a^b
        return [a,b]
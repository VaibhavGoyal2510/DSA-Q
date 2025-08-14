#User function Template for python3
class Solution:
	def setBit(self, n):
		# code here
		an=n
		
		num=1
		
		while an==n:
		    n=n^num
		    num=num<<1
		    if n<an:
		        n=an
		    
		return n
		    
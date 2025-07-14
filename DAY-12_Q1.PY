class Solution:
    def frequencySort(self, s: str) -> str:
        h={}

        for ch in s:
            h[ch] = h.get(ch,0)+1
        
        # print(h)
        h=sorted(h.items(),key=lambda item:item[1],reverse=True)
        return ''.join([ch * freq for ch,freq in h])
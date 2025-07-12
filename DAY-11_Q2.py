class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix=strs[0]

        for st in strs[1:]:
            while not st.startswith(prefix):
                prefix=prefix[:-1]

                if not prefix or prefix=="":
                    return ""
        
        return prefix

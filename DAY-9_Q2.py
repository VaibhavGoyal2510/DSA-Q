
class Solution:
    def twoSum(self, arr, target):
        # code here
        
        seen={}

        for num in arr:
            diff = target-num

        if diff in seen:
            return True

        else:
            seen[num] = num

        return False
            
class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # function should return nothing
    # s is a stack (Python list, top == s[-1])
    def Sorted(self, s):
        if not s:
            return
        n = len(s)  # remember original size

        def again(s, t, c):
            # c = number of items we have scheduled to place already
            if c == n:
                # clear original stack; we'll rebuild it while unwinding
                s.clear()
                return

            # find the next maximum strictly less than t
            t1 = float('-inf')
            for num in s:
                if num < t and num > t1:
                    t1 = num

            # count how many times t1 appears
            cnt = 0
            for num in s:
                if num == t1:
                    cnt += 1

            # recurse, advancing c by the number of elements of this value
            again(s, t1, c + cnt)

            # append t1 cnt times while unwinding (this yields ascending order,
            # so largest ends up on top (s[-1])).
            for _ in range(cnt):
                s.append(t1)

        again(s, float('inf'), 0)


#  # Code here
#         def again(s,t,c):
#             if c==len(s):
#                 s.clear()
                
#                 return 
#             t1=float('-inf')
#             for num in s:
#                 if num<t:
#                     t1=max(t1,num)
                    
#             again(s,t1,c+1)
#             s.append(t1)
#             return 
        
#         again(s,float('inf'),0)
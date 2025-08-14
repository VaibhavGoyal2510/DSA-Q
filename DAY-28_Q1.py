# Coding round question
# my name is doselect

str = 'my name is doselect'

f=list(str)
print(f)
count=2
l=0
r=len(str)-1

while l<r:
    if f[l]==' ':
        count+=1
        l+=1
        continue 
    
    else:
        f[l],f[r]=f[r],f[l]
        l+=1
        r-=1
        
f.append(" "+f"{count}")
print("".join(f))
        

        
    
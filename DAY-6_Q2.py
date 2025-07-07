# Program to find non-repeating words in a string
l =  "The quick brown fox jumps over the lazy dog quick brown fox"
l=str(l.lower())
print(l)
l = l.split(" ")
seen={}
# print(l)

for word in l:
    
    if word not in seen:
        seen[word]=1
    else:
        seen[word]+=1
        
ans=""
for key,val in zip(seen,seen.values()):
    if val==1:
        ans+=key
        ans+=" "
        
print(ans)
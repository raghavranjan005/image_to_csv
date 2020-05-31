
s=input()
f=s.split('\n')
count=0
d=list(f)

for i in d:
    for j in i:
        if(j==" "):
            count=count+1
   
    break

p=s.split()

Count1=0
b=[]

for i in range(0,len(p),count+1):
    t=[]
    for l in range(count+1):
        c=p[i+l]
        t.append(c)
        
    
    b.append(t)

print(b)
Sum=0
for i in range(1,len(b)):
    for j in range(len(b[i])):
        Sum=Sum+int(b[i][1])
        break
print(Sum)

    
    
        
            
        

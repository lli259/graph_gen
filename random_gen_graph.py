import random
output={}

for i in range(1,301):
    o='node('+str(i)+').'
    output[o]=1

edge={}
while 1:
    a=random.sample(range(1,301), 1)[0]
    b=random.sample(range(1,301), 1)[0]
    if a!=b:
        o='link(' +str(a)+','+str(b)+').'
        if not o in edge.keys():
            edge[o]=1
    if len(edge)==3000:
        break

with open('out3.lp','w') as f:
    for i in output:
        f.write(i+'\n')
    for i in edge:
        f.write(i+'\n')


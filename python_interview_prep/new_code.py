x="aabbcccdde"
d={}
for a in list(x):
    if a in d.keys():
        d[a]=d[a]+1
    else:
        d[a]=1

print(d)

import sys
print(sys.argv)
if len(sys.argv) ==2:
    f=open(sys.argv[1],'w+')
    f.write("Hey I am writing to new file")

else:
    print("Please provide ethe number of arguments")

l = [1]
l.extend([10, 12])
print(l)


s=set()
s.add(12)
print(s)
s.update([12,13,14,14])
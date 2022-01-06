def tail(f):
    f.seek(0, 2)
    while True:
        line = f.readline()
        yield line


for i in tail(open("sample.csv")):
    print(i)

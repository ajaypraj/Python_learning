def printmatchtext(matchtext):
    print(f"Printing the matchtext {matchtext}")
    while True:
        line=yield(matchtext)
        if matchtext in line:
            print(line)

matcher=printmatchtext("Python")
matcher.__next__()
matcher.send("hello Python")
matcher.send("Hello")

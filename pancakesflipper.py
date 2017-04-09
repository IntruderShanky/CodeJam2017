inputfile = open("pk1.in", mode='r')
outputfile = open("output_pk_large.txt", mode='w')
t = int(inputfile.readline().strip())


def flip(p, k):
    index = p.index("-")
    validIndex = len(p) - k
    if index + k - 1 < len(p):
        validIndex = index
    for c in range(validIndex, validIndex + k):
        if p[c] is "-":
            p[c] = "+"
        else:
            p[c] = "-"
    return p, validIndex


for i in range(t):
    p, k = inputfile.readline().strip().split(' ')
    k = int(k)
    p = list(str(p))
    ans = 0
    possible = True
    alreadyFlipped = list()
    while p.count("-") > 0:
        p, index = flip(p, k)
        print("".join(p))
        if index in alreadyFlipped:
            possible = False
            break
        ans += 1
        alreadyFlipped.append(index)
    if possible:
        outputfile.write("Case #"+str(i+1)+": "+str(ans))
    else:
        outputfile.write("Case #"+str(i+1)+": "+"IMPOSSIBLE")
    outputfile.write("\n")
outputfile.close()

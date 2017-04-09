inputfile = open("bs.in", mode='r')
outputfile = open("output_bs_next.txt", mode='w')
t = int(inputfile.readline().strip())

for i in range(t):
    numOfStalls, people = map(int, inputfile.readline().strip().split(' '))
    if numOfStalls == people:
        outputfile.write("case #" + str(i + 1) + ": " + str(0) + " " + str(0))
        print("case #" + str(i + 1) + ": " + str(0) + " " + str(0))
        outputfile.write("\n")
    else:
        n = int(numOfStalls / people)
        fp = int()
        if n % 2 == 0:
            fp = int(n / 2)
        else:
            fp = int(n / 2) + 1
        left = fp - 1
        right = n - fp
        outputfile.write("case #" + str(i + 1) + ": " + str(right) + " " + str(left))
        print("case #" + str(i + 1) + ": " + str(right) + " " + str(left))
        outputfile.write("\n")
outputfile.close()
inputfile.close()

inputfile = open("bs1.in", mode='r')
outputfile = open("output_bs.txt", mode='w')
t = int(inputfile.readline().strip())


def get_empty_stalls(occupy):
    occupy.sort()
    s = 0
    position = 0
    for i in range(len(occupy) - 1, 0, -1):
        if (occupy[i] - occupy[i - 1]) >= s:
            s = occupy[i] - occupy[i - 1]
            position = occupy[i - 1]
    return s - 1, position


for i in range(t):
    numOfStalls, people = map(int, inputfile.readline().strip().split(' '))
    if numOfStalls == people:
        outputfile.write("case #" + str(i + 1) + ": " + str(0) + " " + str(0))
        print("case #" + str(i + 1) + ": " + str(0) + " " + str(0))
        outputfile.write("\n")
    else:
        numOfStalls += 2
        occupied = list()
        occupied.append(0)
        occupied.append(numOfStalls - 1)
        for _ in range(people - 1):
            space, pos = get_empty_stalls(occupied)
            if space % 2 == 0:
                occupied.append(int(space / 2) + pos)
            else:
                occupied.append(int(space / 2) + pos + 1)
        space, pos = get_empty_stalls(occupied)
        s = int()
        if space % 2 == 0:
            s = (int(space / 2) + pos)
        else:
            s = (int(space / 2) + pos + 1)
        left = s - pos - 1
        right = pos + space - s
        outputfile.write("case #" + str(i + 1) + ": " + str(right) + " " + str(left))
        print("case #" + str(i + 1) + ": " + str(right) + " " + str(left))
        outputfile.write("\n")
outputfile.close()
inputfile.close()

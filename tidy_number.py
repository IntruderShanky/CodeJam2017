inputfile = open("tn1.in", mode='r')
outputfile = open("output_tn_large.txt", mode='w')
t = int(inputfile.readline().strip())
for i in range(t):
    num = str(inputfile.readline().strip())
    actual = int(num)
    if num[len(num) - 1] is '0':
        num = int(num) - 1
        num = list(str(num))
    num = list(map(int, num))
    loop = True
    while loop:
        loop = False
        for j in range(len(num) - 1):
            if num[j] > num[j + 1]:
                num[j + 1] = 9
                temp = int("".join(list(map(str, num))))
                if temp > actual:
                    num[j] -= 1
                loop = True
                break
    num = int("".join(list(map(str, num))))
    outputfile.write("Case #" + str(i + 1) + ": " + str(num))
    outputfile.write("\n")
outputfile.close()
inputfile.close()

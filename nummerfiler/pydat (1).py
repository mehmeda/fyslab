with open('testfile6.txt','r') as f:
    l = 0
    ylist = []
    for line in f:
        for i, num in enumerate(line.split()):
            if ((i+1)%3==0):
                ylist.append(num)
            if ((i-1)%3==0):
                print(num)
        l += 1


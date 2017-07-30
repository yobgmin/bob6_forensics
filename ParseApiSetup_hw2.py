#run in Windows 10

setup = "C:\Windows\INF\\setupapi.dev.log"
USBInfo = []
start = []

with open(setup) as setupapi:
    for line in setupapi:
        if 'Device Install (Hardware initiated)' in line:
            SP = line.split('\\')
            USBInfo.append((SP[0].split('-')[1].strip(), SP[1], SP[2][:-2]))
            start.append(next(setupapi).split('start')[1].strip())

for x in range(0,len(start)):
    print 'USB Information : ',USBInfo[x][0], USBInfo[x][1], USBInfo[x][2]
    print "Starting time : ", start[x]

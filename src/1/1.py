import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(os.path.join(__location__, 'input.txt'))
Lines = file1.readlines()

maxcalories = 0
sumcal = 0  
# Strips the newline character
maxcallist=[]
for line in Lines:
    line=line.strip()
    if (line==""):
        maxcallist.append(sumcal)
        if sumcal>maxcalories:
            print (f"max cal {sumcal}")
            maxcalories=sumcal
        sumcal=0
    else:
        sumcal=sumcal+int(line)
maxcallist.sort()
sum = 0
for m in (maxcallist[-3:]):
    print(m)
    sum=sum+m
print (sum)
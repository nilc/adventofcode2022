import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(os.path.join(__location__, 'input.txt'))
Lines = file1.readlines()

def translate(input):
    if input=="A" or input=="X":
        return "rock"
    elif input=="B" or input=="Y":
        return "paper"
    else:
        return "scissor"

def winorlose(you):
    if you=="X":
        return 0#"lose"
    elif you=="Y":
        return 3#"draws"
    else:
        return 6#"win"
def getyourdraw(wantedresult):
    for t in ["X","Y","Z"]:
        if (winner(opponent,t)==wantedresult):
            return t

def winner(o,you):
    if (o=="A"):
        if you=="Y":
            return 6
        if you=="X":
            return 3
        return 0
    if (o=="B"):
        if you=="Y":
            return 3
        if you=="X":
            return 0
        return 6
    if (o=="C"):
        if you=="Y":
            return 0
        if you=="X":
            return 6
        return 3    
strategy={"A":"Y",
"B":"X",
"C":"Z"}
pointspershape={"X":1,"Y":2,"Z":3}
sumgame = 0  
# Strips the newline character
maxcallist=[]
for line in Lines:
    line=line.strip()
    arr=line.split(" ")
    opponent=arr[0]
    yourresult=arr[1]
    wantedresult=winorlose(yourresult)
    you=getyourdraw(wantedresult)
        
    pointshape=pointspershape[you]
    pointswin=winner(opponent,you)
    sumgame=sumgame+pointshape+pointswin
print (sumgame)
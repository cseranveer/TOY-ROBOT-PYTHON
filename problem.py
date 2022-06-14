"""    
     0   1   2   3   4
0   0/0 0/1 0/2 0/3 0/4
1   1/0 1/1 1/2 1/3 1/4
2   2/0 2/1 2/2 2/3 2/4
3   3/0 3/1 3/2 3/3 3/4
4   4/0 4/1 4/2 4/3 4/4
"""

x = 0
y = 0
face = ''
MAX = 4
isPositionInitialized = False
# def: displays current position
def DP():
    print('ROBOT IS AT ('+str(x)+','+str(y)+') FACING', face)
# def: prints MOVE NOT ALLOWED
def MNA():
    print('MOVE NOT ALLOWED UNDER FALL PREVENTION,', end =" ")
# initializes position of the robot
def initializePosition(ins):
    if(ins[:5] == 'PLACE'):
        global x,y,face
        x = int(ins.split('PLACE')[1].split(',')[0])
        y = int(ins.split('PLACE')[1].split(',')[1])
        face = ins.split('PLACE')[1].split(',')[2].strip()
        if x>=0 and y<=MAX and face in ['NORTH','SOUTH','WEST','EAST']:
            drawFrame()
            return True
        else:
            print("INVALID PLACE COMMAND")
            return False
    else:
        print("KINDLY INITIALIZE ROBOT POSITION FIRST EG. PLACE 0,0,NORTH")
        return False
def drawFrame():
    print()
    for i in range(5):
        for j in range(5):
            if i == x and j == y:
                if face == "NORTH":
                    print("↑ ",end = "")
                if face == "SOUTH":
                    print("↓ ",end = "")
                if face == "WEST":
                    print("← ",end = "")
                if face == "EAST":
                    print("→ ",end = "")
                continue
            print("* ",end = "")
        print()
print("INITIALIZE ROBOT")
while 1:
    ins = input('>>')
    ins = ins.upper()
    if isPositionInitialized:
        if(ins[:5] == 'PLACE'):
            initializePosition(ins)
        elif ins == 'MOVE':
            if(face =='NORTH'):
                if(x-1 <0):
                    MNA()
                else:
                    x = x-1
            if(face =='SOUTH'):
                if(x+1>MAX):    
                    MNA()
                else:
                    x = x+1
            if(face =='WEST'):
                if(y-1<0):
                    MNA()
                else:
                    y = y-1
                    DP()
            if(face =='EAST'):
                if(y+1>MAX):
                    MNA()
                else:
                    y = y+1
        elif ins == 'LEFT':
            if(face =='NORTH'):
                if(y-1 <0):
                    MNA()
                else:
                    y = y-1
            if(face =='SOUTH'):
                if(y+1>MAX):
                    MNA()
                else:
                    y = y+1
            if(face =='WEST'):
                if(x+1>MAX):
                    MNA()
                else:
                    x = x+1
            if(face =='EAST'):
                if(x-1<0):
                    MNA()
                else:
                    x = x-1
        elif ins == 'RIGHT':
            if(face =='NORTH'):
                    if(y+1 >MAX):
                        MNA()
                    else:
                        y = y+1
            if(face =='SOUTH'):
                if(y-1<0):
                    MNA()
                else:
                    y = y-1
            if(face =='WEST'):
                if(x-1<0):
                    MNA()
                else:
                    x = x-1
                    DP()
            if(face =='EAST'):
                if(x+1>MAX):
                    MNA()
                else:
                    x = x+1
        elif ins == 'REPORT':
            DP()
            drawFrame()
            continue
        else:
            print("NOT A VALID COMMAND, USE PLACE, MOVE, LEFT, RIGHT, REPORT")
        DP()
        drawFrame()
    else:
        isPositionInitialized = initializePosition(ins)
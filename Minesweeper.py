import random
import turtle
import time
startTime=time.time()#this is not important, just a timer
ned=turtle.Turtle()

                  #CONFIG
fullLength=790 #any number, 600 +/- 200 works best
rowNumber=5 #any number should work as long as there are enough pixels to accomodate a playable square
bombs=1 # 0<=bombs<=(rowNumber^2), or else it will break.

def restart():
    ned.penup()
    ned.goto((fullLength/-2),(fullLength/2))
    ned.pendown()
    ned.speed(0)
    turtle.tracer(0,0)
    ned.penup()
    ned.forward(1)
    ned.backward(1)
    ned.pendown()



def listMaker(rowNumber): #This mess of code assigns all of the tiles to a list.
    tileList=[]
    for e in range(rowNumber):
        tileListHelp=[]
        for e in range(rowNumber):
            tileListHelp+=["safe"]
        tileList+=[tileListHelp]
    return tileList

tileList=listMaker(rowNumber)

def drawGrid(fullLength,rowNumber): #This function draws the game grid
    ned.ht()
    for e in range(4):
        ned.forward(fullLength)
        ned.right(90)
    for e in range(rowNumber):
        ned.forward(fullLength/rowNumber)
        ned.right(90)
        ned.forward(fullLength)
        ned.backward(fullLength)
        ned.left(90)
    ned.right(90)
    for e in range(rowNumber):
        ned.forward(fullLength/rowNumber)
        ned.right(90)
        ned.forward(fullLength)
        ned.backward(fullLength)
        ned.left(90)
    ned.penup()
    x=(fullLength/-2)+((fullLength/rowNumber)/2)
    y=(fullLength/2)-((fullLength/rowNumber)/2)
    ned.goto(x,y)
    ned.st()
    turtle.update()
    turtle.tracer(1)
    

def assign(tileList,bombs):#This function assigns bombs to tiles
    bombAmount=0
    while bombs>0:
        assigner=random.randint(1,1000)
        assignerR=random.randint(0,len(tileList)-1)
        assignerC=random.randint(0,len(tileList)-1)
        if assigner==1:
            if tileList[assignerR][assignerC]!="bomb":
                tileList[assignerR][assignerC]="bomb"
                bombs-=1
    for r in range(len(tileList)): #this gets a full count of the bombs
        for c in range(len(tileList[0])):
            if tileList[r][c]=="bomb":
                bombAmount +=1

    print("           There are", end=" ")
    print(bombAmount, end=" ")
    print("bombs in this game.")

    return tileList

bombList=assign(tileList,bombs)

def xCoords(rowNumber):#This gives the possible coordinates of all spaces
    AX=(fullLength/-2)+((fullLength/rowNumber)/2)
    xList=[AX]
    for e in range(rowNumber-1):
        xList+=[xList[e]+fullLength/rowNumber]
    return xList
xList=xCoords(rowNumber)
def yCoords(rowNumber):
    AY=(fullLength/2)-((fullLength/rowNumber)/2)
    yList=[AY]
    for e in range(rowNumber-1):
        yList+=[yList[e]-fullLength/rowNumber]
    return yList
yList=yCoords(rowNumber)

def playGame(): #actual gameplay
    ned.color("black")
    ned.penup()
    turtle.listen()
    turtle.onkey(goRight,"Right")
    turtle.onkey(goLeft,"Left")
    turtle.onkey(goUp,"Up")
    turtle.onkey(goDown,"Down")
    turtle.onkey(flagHelp,"w")
    turtle.onkey(clearHelp,"q")
    for e in range(len(bombList)):#win test
        if "safe" in bombList[e]:
            return
        else:
            win()

def goRight():    #start of movement
    if ned.xcor()<(fullLength/2)-((fullLength/rowNumber)/2)-1:
        ned.seth(0)
        ned.forward(fullLength/rowNumber)
        return
def goLeft():
    if ned.xcor()>(fullLength/-2)+((fullLength/rowNumber)/2)+1:
        ned.seth(180)
        ned.forward(fullLength/rowNumber)
        return
def goDown():
    if ned.ycor()>(fullLength/-2)+((fullLength/rowNumber)/2)+1:
        ned.seth(270)
        ned.forward(fullLength/rowNumber)
        return
def goUp():
    if ned.ycor()<(fullLength/2)-((fullLength/rowNumber)/2)-1:
        ned.seth(90)
        ned.forward(fullLength/rowNumber)
        return     #end of movement

def flagHelp():
    flag(fullLength,rowNumber)
    
def flag(fullLength,rowNumber): #this sets a flag when the key "w" is pressed
    ned.pendown()
    ned.pensize(5)
    ned.color("red")
    ned.seth(-45)
    ned.forward(fullLength/rowNumber/2)
    ned.backward(fullLength/rowNumber)
    ned.forward(fullLength/rowNumber/2)
    ned.seth(45)
    ned.forward(fullLength/rowNumber/2)
    ned.backward(fullLength/rowNumber)
    ned.forward(fullLength/rowNumber/2)
    ned.penup()

def clearHelp():
    clear(bombList,xList,yList,rowNumber)
           
            
def clear(bombList,xList,yList,rowNumber): #this function clears a tile.
    nearBombs=0
    for e in range(1):
        for x in range(len(xList)):
            if int(xList[x]-fullLength/rowNumber/4)<int(ned.xcor())<=int(xList[x]+fullLength/rowNumber/4):
                currentRow=x
        for y in range(len(yList)):
            if int(yList[y]-fullLength/rowNumber/4)<int(ned.ycor())<=int(yList[y]+fullLength/rowNumber/4):
                currentCol=y
    if bombList[currentRow][currentCol]=="bomb":
        gameOver()
    else:
        bombList[currentRow][currentCol]="cleared"
        nearBombs=clearTest(currentRow,currentCol,nearBombs,rowNumber)
                    
    if nearBombs==0:#this is the start of the writing for the amount of bombs nearby.
        curX=ned.xcor()
        curY=ned.ycor()
        ned.seth(270)
        ned.forward(15)
        ned.write("✓","center",align="center",font=("arial",25,"normal"))
        ned.setx(curX)
        ned.sety(curY)
        
    elif nearBombs==1:
        ned.color("#0000ff")
        curX=ned.xcor()
        curY=ned.ycor()
        ned.seth(270)
        ned.forward(15)
        ned.write(1,"center",align="center",font=("arial",25,"normal"))
        ned.setx(curX)
        ned.sety(curY)
        
    elif nearBombs==2:
        curX=ned.xcor()
        curY=ned.ycor()
        ned.color("#32CD32")
        ned.seth(270)
        ned.forward(15)
        ned.write(2,"center",align="center",font=("arial",25,"normal"))
        ned.setx(curX)
        ned.sety(curY)
        
    elif nearBombs==3:
        curX=ned.xcor()
        curY=ned.ycor()
        ned.color("#FF0000")
        ned.seth(270)
        ned.forward(15)
        ned.write(3,"center",align="center",font=("arial",25,"normal"))
        ned.setx(curX)
        ned.sety(curY)
        
    elif nearBombs==4:
        curX=ned.xcor()
        curY=ned.ycor()
        ned.color("#c300ff")
        ned.seth(270)
        ned.forward(15)
        ned.write(4,"center",align="center",font=("arial",25,"normal"))
        ned.setx(curX)
        ned.sety(curY)
        
    elif nearBombs==5:
        curX=ned.xcor()
        curY=ned.ycor()
        ned.color("#ffe100")
        ned.seth(270)
        ned.forward(15)
        ned.write(5,"center",align="center",font=("arial",25,"normal"))
        ned.setx(curX)
        ned.sety(curY)
        
    elif nearBombs==6:
        curX=ned.xcor()
        curY=ned.ycor()
        ned.color("#0ca4ff")
        ned.seth(270)
        ned.forward(15)
        ned.write(6,"center",align="center",font=("arial",25,"normal"))
        ned.setx(curX)
        ned.sety(curY)
        
    elif nearBombs==7:
        curX=ned.xcor()
        curY=ned.ycor()
        ned.color("#000000")
        ned.seth(270)
        ned.forward(15)
        ned.write(7,"center",align="center",font=("arial",25,"normal"))
        ned.setx(curX)
        ned.sety(curY)
        
    elif nearBombs==8:
        curX=ned.xcor()
        curY=ned.ycor()
        ned.color("#737373")
        ned.seth(270)
        ned.forward(15)
        ned.write(8,"center",align="center",font=("arial",25,"normal"))
        ned.setx(curX)
        ned.sety(curY)

    winTest=[]
    for e in range(len(bombList)):#this is a win test
        winTest+=bombList[e]
    if "safe" in winTest:
        return
    else:
        win()
            
def clearTest(currentRow,currentCol,nearBombs,rowNumber):#this actually tests the adjacent squares

    if currentCol!=0 and currentCol!=(rowNumber-1) and currentRow!=0 and currentRow!=(rowNumber-1):#center tiles
        
        if bombList[currentRow][currentCol+1]=="bomb":#testing right
            nearBombs+=1
        if bombList[currentRow+1][currentCol+1]=="bomb":#testing down,right
            nearBombs+=1
        if bombList[currentRow-1][currentCol+1]=="bomb":#testing up,right
            nearBombs+=1
        if bombList[currentRow-1][currentCol]=="bomb":#testing up
            nearBombs+=1
        if bombList[currentRow+1][currentCol]=="bomb":#testing down
            nearBombs+=1
        if bombList[currentRow][currentCol-1]=="bomb":#testing left
            nearBombs+=1
        if bombList[currentRow+1][currentCol-1]=="bomb":#testing down,left
            nearBombs+=1
        if bombList[currentRow-1][currentCol-1]=="bomb":#testing up,left
            nearBombs+=1
            
    elif currentCol==0 and currentRow!=0 and currentRow!=(rowNumber-1):#left tiles
        
        if bombList[currentRow][currentCol+1]=="bomb":#testing right
            nearBombs+=1
        if bombList[currentRow+1][currentCol+1]=="bomb":#testing down,right
            nearBombs+=1
        if bombList[currentRow-1][currentCol+1]=="bomb":#testing up,right
            nearBombs+=1
        if bombList[currentRow-1][currentCol]=="bomb":#testing up
            nearBombs+=1
        if bombList[currentRow+1][currentCol]=="bomb":#testing down
            nearBombs+=1
            
    elif currentCol==(rowNumber-1) and currentRow!=0 and currentRow!=(rowNumber-1):#right tiles
        
        if bombList[currentRow-1][currentCol]=="bomb":#testing up
            nearBombs+=1
        if bombList[currentRow+1][currentCol]=="bomb":#testing down
            nearBombs+=1
        if bombList[currentRow][currentCol-1]=="bomb":#testing left
            nearBombs+=1
        if bombList[currentRow+1][currentCol-1]=="bomb":#testing down,left
            nearBombs+=1
        if bombList[currentRow-1][currentCol-1]=="bomb":#testing up,left
            nearBombs+=1
            
    elif currentRow==0 and currentCol!=0 and currentCol!=(rowNumber-1):#top tiles
        
        if bombList[currentRow][currentCol+1]=="bomb":#testing right
            nearBombs+=1
        if bombList[currentRow+1][currentCol+1]=="bomb":#testing down,right
            nearBombs+=1
        if bombList[currentRow+1][currentCol]=="bomb":#testing down
            nearBombs+=1
        if bombList[currentRow][currentCol-1]=="bomb":#testing left
            nearBombs+=1
        if bombList[currentRow+1][currentCol-1]=="bomb":#testing down,left
            nearBombs+=1
            
    elif currentRow==(rowNumber-1) and currentCol!=0 and currentCol!=(rowNumber-1):#bottom tiles
        
        if bombList[currentRow][currentCol+1]=="bomb":#testing right
            nearBombs+=1
        if bombList[currentRow-1][currentCol+1]=="bomb":#testing up,right
            nearBombs+=1
        if bombList[currentRow-1][currentCol]=="bomb":#testing up
            nearBombs+=1
        if bombList[currentRow][currentCol-1]=="bomb":#testing left
            nearBombs+=1
        if bombList[currentRow-1][currentCol-1]=="bomb":#testing up,left
            nearBombs+=1

    elif currentRow==0 and currentCol==0: #top left

        if bombList[currentRow+1][currentCol]=="bomb":#testing down
            nearBombs+=1
        if bombList[currentRow][currentCol+1]=="bomb":#testing right
            nearBombs+=1
        if bombList[currentRow+1][currentCol+1]=="bomb":#testing down,right
            nearBombs+=1

    elif currentRow==(rowNumber-1) and currentCol==0: #bottom left
        if bombList[currentRow][currentCol+1]=="bomb":#testing right
            nearBombs+=1
        if bombList[currentRow-1][currentCol+1]=="bomb":#testing up,right
            nearBombs+=1
        if bombList[currentRow-1][currentCol]=="bomb":#testing up
            nearBombs+=1

    elif currentRow==0 and currentCol==(rowNumber-1): #top right
        if bombList[currentRow+1][currentCol]=="bomb":#testing down
            nearBombs+=1
        if bombList[currentRow][currentCol-1]=="bomb":#testing left
            nearBombs+=1
        if bombList[currentRow+1][currentCol-1]=="bomb":#testing down,left
            nearBombs+=1


    elif currentRow==(rowNumber-1) and currentCol==(rowNumber-1): #bottom right
        if bombList[currentRow-1][currentCol]=="bomb":#testing up
            nearBombs+=1
        if bombList[currentRow][currentCol-1]=="bomb":#testing left
            nearBombs+=1
        if bombList[currentRow-1][currentCol-1]=="bomb":#testing up,left
            nearBombs+=1
    return nearBombs

            

def gameOver():
    turtle.bye()
    print("You lost! Restart the program to play again!")

def win():
    print("You win! Restart the program to play again!")
    print("It took you", end=" ")
    print(int(time.time()-startTime), end=" ")
    print("seconds to finish!")
    ned.home()
    ned.clear()
    ned.pendown()
    ned.pensize(10)
    ned.write("WINNER", align="center",font=('arial',50,'normal'))
    time.sleep(5)
    ned.clear()
    starter(random.randint(50,100),random.randint(30,50),.5,random.randint(1,3))
    #time.sleep(10)
    #quit()

def tree(iL,A,M):
    if iL<=10 and iL>0:
        leaf=random.randint(1,3)
        if leaf==1:
            ned.color("green")
        elif leaf==2:
            ned.color("#006400")
        elif leaf==3:
            ned.color("#228B22")
        else:
            ned.color("#6B8E23")
    elif iL>10:
        ned.color("#654321")
    elif iL<0:
        ned.color("black")
                              
    if abs(iL)>50:
        ned.pensize(5)
    elif abs(iL)>25:
        ned.pensize(3)
    elif abs(iL)>10:
        ned.pensize(2)
    else:
        ned.pensize(1)
        
    if abs(iL)<1:
        ned.begin_fill()
        ned.circle(5)
        ned.end_fill()
        return
    elif abs(iL)>1000:
        return
    else:
        ned.forward(iL)
        ned.right(A)
        tree((iL*M),A,M)
        ned.left(A*2)
        tree((iL*M),A,M)
        ned.right(A)
        ned.backward(iL)
        
    if iL<=10 and iL>0:
        ned.color("green")
    elif iL>10:
        ned.color("#654321")
    elif iL<0:
        ned.color("black")

def starter(iL,A,M,levels):
    turtle.tracer(0)
    ned.seth(0)
    ned.color("#d2b48c")
    ned.begin_fill()
    ned.forward(1000)
    ned.right(90)
    ned.forward(500)
    ned.right(90)
    ned.forward(2000)
    ned.right(90)
    ned.forward(500)
    ned.right(90)
    ned.forward(1000)
    ned.end_fill()
    ned.color("green")
    ned.pensize(5)
    ned.forward(1000)
    ned.backward(2000)
    ned.forward(1000)
    ned.left(90)
    turtle.update()
    turtle.tracer(1)
    tree(iL,A,M)
    tree(-1*iL,A,M)

    for e in range(levels):
        tree((2*e*iL),A,M)
        tree((2*-e*iL),A,M)
print("                      INSTRUCTIONS")
print("Use the arrow keys to move, Q to clear a tile, and W to set a flag")
print("         Go slow, or you may break something")
def play():
    restart()
    drawGrid(fullLength,rowNumber)
    playGame()
play()

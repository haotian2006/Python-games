import turtle as DrawingBorad
import time as task
#0,0 = -75,75
print("Created By Hao by using tutle as a drawing borad")
if False:# Change this to True To Emable it
    print("How This Works:")
    print("Basicly how this works is first the CreateGame Class Is Called")
    print("Then the start game function/method is called which also calls CreateGrid")
    print("In CreateGird It Creates the grid and also creates a turtle and screen attribute")
    print("Then It Calls Loop")
    print("What Loop does is it calls AskForPos which ask for a input and checks if it is valid")
    print("then it will create a x or a o depending on who the player is")
    print("then it checks if any x or o is 3 in a row by first getting a 3x3 area around itself and looking for the same icons")
    print("then it gets the direaction between itself and then goes in that direacion 3 times and see if it finds 2 other of the same")
    print("if it dosen't then check it all of the grid is filled and if it is call a stalemate")
    print("then it runs loop again")
class CreateGame():
    #settings
    speed = 10#tutle speed
    visulize = False #show tutle
    #attributes
    placed = {}
    screen = ""
    current_turtle = ""
    current_turn = 1
    winner = "None"
    StartTime = ""
    timetext = "23"
    canplacein = {"1,1","1,2", "1,3","2,1","2,2" ,"2,3","3,1", "3,2" ,"3,3"}
    GameEnded = False
    gridlayout = [[-100,50],[-100,-50],[-50,-100,90],[50,-100,90]]
    textpos = [-125,-120]
    #functions/methods
    def AskForPos(self,IsError):
        if self.GameEnded:
            return False
        text = ""
        if IsError == 1:
            text = input("Player "+str(self.current_turn)+" Please Enter A coordinate'example: 1,1' :" )
        else:
            text = input("Input was not Valid Please Enter A coordinate'example: 1,1' :" )
        if text == "end" or text == "None": 
            self.EndGame()
            return
        e = text.split(",")
        length = len(text)
        c = [*text]
        if length== 3 and c[1] == ',' and not text in self.placed and text in self.canplacein: 
            text = text
        else:
            text = self.AskForPos(2) 
        if IsError == 1:     
            text2 = "Player "+ str(self.current_turn) +" Placed At ["+ text +"]"
            color = "Green" if self.current_turn == 1 else "Red"
            self.current_turtle.up()
            if len(self.placed)%3 == 0:
                self.textpos[0] = -135
                self.textpos[1] -= 20                   
            else:
                self.textpos[0] += 125
            self.current_turtle.goto(self.textpos[0],self.textpos[1])
            style = ('Arial', 9.8,"bold")
            self.current_turtle.color(color)
            self.current_turtle.write(text2,font=style,align='center')
            self.placed[text] = self.current_turn
            self.current_turn = 2 if self.current_turn == 1 else 1
        return text
    def GoToPosition(self,Position):
        if self.GameEnded:
            return
        splitted = Position.split(",")
        x = float(splitted[0])
        y = float(splitted[1])
        self.current_turtle.goto(-75+75*(y-1),75-75*(x-1))
       # self.DrawCircle()
    def DrawCircle(self):
        if self.GameEnded:
            return
        r = 25
        self.current_turtle.color("Red")
        self.current_turtle.right(90)
        self.current_turtle.forward(r)
        self.current_turtle.left(90)
        self.current_turtle.down()
        self.current_turtle.circle(r)
        self.current_turtle.up()
        self.current_turtle.color("black")
    def DrawX(self):
        if self.GameEnded:
            return
        halfsize = 25
        self.current_turtle.down()
        self.current_turtle.color("Green")
        self.current_turtle.right(45)
        self.current_turtle.forward(halfsize)
        self.current_turtle.backward(halfsize*2)
        self.current_turtle.forward(halfsize)
        self.current_turtle.left(90)
        self.current_turtle.forward(halfsize)
        self.current_turtle.backward(halfsize*2)
        self.current_turtle.up()
        self.current_turtle.color("black")
        self.current_turtle.setheading(0)
    def CreateGrid(self):
        self.screen = DrawingBorad.Screen()
        self.current_turtle = DrawingBorad.Turtle()
        if not self.visulize:
            self.current_turtle.hideturtle()
        self.current_turtle.speed(self.speed)
        x,y = -100,50
        for i in self.gridlayout:
            self.current_turtle.up()
            self.current_turtle.goto(i[0],i[1])
            self.current_turtle.down()
            if len(i) >= 3:
                 self.current_turtle.left(90)
            self.current_turtle.forward(200)   
            if len(i) >= 3:
                 self.current_turtle.right(90)
        self.current_turtle.up()
        
        self.current_turtle.goto(-75,75)
    def DrawLine(self,start,pos2,playerw):
        start1 = start.split(',')
        pos21 = pos2.split(',')
        d = [int(pos21[0])-int(start1[0]),int(pos21[1])-int(start1[1])]
        on = start
        for i in range(5):
            stuff = self.CheckCoordForNear(on,d)
            if len(stuff) >0:
                for i,v in stuff.items():
                    on = i
        new = start.split(",")
        self.GoToPosition(str(float(new[0])-float(d[0])/2)+','+str(float(new[1])-float(d[1])/2))
        if playerw ==1:
            self.current_turtle.color("green")
        else:
            self.current_turtle.color("red")  
        self.current_turtle.down()
        new = on.split(",")
        self.GoToPosition(str(float(new[0])+float(d[0])/2)+','+str(float(new[1])+float(d[1])/2))   
        self.current_turtle.up()
    def CheckCoordForNear(self,text,direaction):
        text2 = text.split(",")
        x,y = int(text2[0]),int(text2[1])
        player = self.placed[text]
        found = {}
        if direaction:
            newx,newy = x+direaction[0],y+direaction[1]
            if str(newx)+","+str(newy) != text and str(newx)+","+str(newy) in self.placed:
                if self.placed[str(newx)+","+str(newy)] == player:
                    found[str(newx)+","+str(newy)] = direaction
        else:
             for zx in range(x-1,x+2):
                for zy in range(y-1,y+2):  
                    if str(zx)+","+str(zy) in self.placed:
                        if str(zx)+","+str(zy) in self.placed and self.placed[str(zx)+","+str(zy)] == player:
                            found[str(zx)+","+str(zy)] = [zx-x,zy-y]
        return found
        
            
                
    def CheckForWinner(self):
        point1,point2 = False,False
        playerw = 0
        for coord,player in self.placed.items():
            text = coord.split(",")
            x,y = text[0],text[1]
            point1 = coord
            playerw = player
            close = self.CheckCoordForNear(coord,False)
            if len(close) > 0:       
                for c,d in close.items():
                    can = True
                    for i in range(4):
                        new = self.CheckCoordForNear(c,d)
                        if len(new) == 0:
                            can = False
                            break
                        point2 = c                         
                    if can:                       
                        break
            if point2:
                break
        if point2:
            self.DrawLine(point1,point2,playerw)
            self.winner = playerw
            self.EndGame()
            return False
        if len(self.placed) == 9:
            self.EndGame()
        return True
    def UpdateTime(self):
        self.timetext.up()
        self.timetext.clear()
        if self.current_turn == 1:
            self.timetext.color("red")
        else:
            self.timetext.color("green")
        self.timetext.goto(150,0)
        self.timetext.write(str(24-(int(task.time()) - self.StartTime)) +" s" , font=('Arial',20))
    def Loop(self):
        self.UpdateTime()
        coord = self.AskForPos(1)
        if coord ==False :
            return
        self.GoToPosition(coord)
        if self.current_turn == 1:
            self.DrawCircle()
        else:
            self.DrawX()
        loopa = self.CheckForWinner()
        if loopa:
            self.Loop()
        return
    def StartGame(self):
        self.timetext = DrawingBorad.Turtle()
        self.timetext.hideturtle()
        self.timetext.speed(10)
        self.StartTime= int(task.time())
        self.GameEnded = False
        self.CreateGrid()
        for x in range(1,4):
            x1 = str(x)+',1'
            x2=str(x)+',2'
            x3=str(x)+',3'
            for i in range(1,4):
                f = str(i)
                e = str(x)
                a = e+","+f
                self.GoToPosition(a)
                style = ('Arial', 15, 'italic')
                self.current_turtle.write(e+","+f,font=style,align='center')
           # print("[",x1,"]","[",x2,"]","[",x3,"]")
        task.sleep(.3)
        self.Loop()
    def EndGame(self):
        self.GameEnded = True
        text,color = "","Black"
        if self.winner == "None":
            text ="Stalemate"
        else:
            text = "Player "+ str(self.winner) +" Won"
            color = "Green" if self.winner == 1 else "Red"
        self.current_turtle.goto(0,150)
        style = ('timesnewroman', 50,)
        self.current_turtle.color(color)
        self.current_turtle.write(text,font=style,align='center')
        self.placed = {}
        self.screen = ""
        self.current_turtle = ""
        self.current_turn = 1
        self.winner = "None"
        
newgame = CreateGame()
newgame.StartGame()
exitout = False
def endexit():
    exitout= True
    exit()
turtle.onkey(endexit,"Escape")
for i in range(99999):
    if exitout:
        break
    time.sleep(1)


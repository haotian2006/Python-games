import turtle
import math
import random  
import time
print("Made By Hao")
print("It Is also reccomended to use an ide for this")
#How to play
#You can change Mines var in the MineSweeper Class to increase/decreese the amount of mines spawnned
#you can click on the grid thats not fully made to start
#to win you need to cover all mines with a flag
#to place/remove a flag first switch to flag mode (f or FlagModeKey) and left click 
#if your not placing any flags then you might have ran out, you can check the ammount you have left in the bottem right corner
#If you have used all flags and you didn't win then you most likly have a flag on a tile thats not a bomb
#also mines only spawn in full Squars
#also if you are using a ide thats not runestone you can change length to a number divisable by 50
#Have Fun - hao
class createtext():
    #Simple text Module Created by hao
    def __init__(self):
        self.style = "" 
        self.align = ""
        self.turtlea = turtle.Turtle()
        self.turtlea.speed(200)
        self.turtlea.up()
    def set(self,style,align,color):
        self.style,self.align,self.color = style,align,color
        
    def goto(self,x,y):
        self.turtlea.goto(x,y)
        self.turtlea.hideturtle()
    def clear(self):
        self.turtlea.clear()
    def setext(self,text):
        self.turtlea.color(self.color)
        self.clear()
        self.turtlea.write(text,font=self.style,align=self.align)
        
class MineSweeper():
    #Settings
    gridsize = 50
    length = 200
    startend = [int(-length+gridsize/2),int(length-gridsize/2)]
    ShowTurtles = False
    BgColor = "Lime"
    indexcolor = ["White","Black","Blue","Yellow","Red"]
    FlagModeKey = "f"
    #minessettings
    MineColor = "Black"
    Mines = 10 #Max Mines
    ShowMines = False
    #attributes
    flagmodebool = False
    mines = {}
    flags = {}
    MineText = createtext()
    MineText.set(('Arial', 12),"right","Red")
    flagmodetext = createtext()
    flagmodetext.set(('Arial', 12),"right","Black")
    Screen = turtle.Screen()
    Screen.bgcolor(BgColor)
    MainTurtle = turtle.Turtle()
    GameEnded = False
    def combinevector2(self,x,y):
        return str(x)+","+str(y)
    def roundtogrid(self,x,y):
        return round(x/self.gridsize)*self.gridsize,round(y/self.gridsize)*self.gridsize
    def getrandmine(self):
        x,y = random.randrange(self.startend[0]+self.gridsize/2,self.startend[1]-self.gridsize/2),random.randrange(self.startend[0]+self.gridsize/2,self.startend[1]-self.gridsize/2)
        x,y = self.roundtogrid(x,y)
        if not self.checkmine(x,y):
            x,y= self.getrandmine()
        return x,y
    def checknearby(self,x,y):
        minecount = 0
        for cx in range(x-50,x+50+1,50):
            for cy in range(y-50,y+50+1,50):
                if not self.checkmine(cx,cy):
                    minecount+= 1
        return minecount
    def checkmine(self,x,y):
        if self.combinevector2(x,y) in self.mines:
            return False
        return True
    
    def GenMines(self):
        for i in range(self.Mines):
            x,y = self.getrandmine()
            self.mines[self.combinevector2(x,y)] = [x,y]
            if self.ShowMines:
                self.DrawMine(x,y)
    def DrawMine(self,x,y):
        self.MainTurtle.up()
        self.MainTurtle.goto(x,y)
        self.MainTurtle.begin_fill()
        self.MainTurtle.color(self.MineColor)
        self.MainTurtle.circle(8)
        self.MainTurtle.end_fill()
    def CheckIfFlags(self):
        win = True
        if len(self.flags) == self.Mines:
            for index,value in self.mines.items():
                if not self.flags[index]:
                    win = False
                    break
        else:
            win = False 
        if win:
            self.endgame(True)
        return win
    def DrawFlag(self,x,y):
        if self.combinevector2(x,y) in self.flags:
            self.flags[self.combinevector2(x,y)].setext("")
            self.flags.pop(self.combinevector2(x,y),None)
        else:
            if len(self.flags) != self.Mines:
                self.flags[self.combinevector2(x,y)] = createtext()
                self.flags[self.combinevector2(x,y)].goto(x,y)
                self.flags[self.combinevector2(x,y)].set(('Arial', 12),"center","Red")
                self.flags[self.combinevector2(x,y)].setext("Flag")
    def FlagMode(self):
        self.flagmodebool = not self.flagmodebool
        self.flagmodetext.setext("Flag Mode: "+str(self.flagmodebool))
    def OnClick(self,x,y):
        if self.GameEnded:
            return
        x,y = self.roundtogrid(x,y)
        self.MainTurtle.up()
        nearmines = self.checknearby(x,y)
        colora = self.indexcolor[nearmines] if nearmines<len(self.indexcolor) else "Purple"
        self.MainTurtle.color(colora)
        style = ('Arial', 15)
        self.MainTurtle.goto(x,y)
        if self.flagmodebool:          
            self.DrawFlag(x,y)
            self.MineText.setext(str(self.Mines- len(self.flags))+" flags left")
            self.CheckIfFlags()
            return
        if self.combinevector2(x,y) in self.flags:
            return
        if self.combinevector2(x,y) in self.mines:
            self.endgame(False)
        self.MainTurtle.write(str(nearmines),font=style,align='center')
    def Grid(self):
        self.MainTurtle.color("grey")
        for x in range(self.startend[0],self.startend[1]+1,self.gridsize):
            self.MainTurtle.up()
            self.MainTurtle.goto(x,self.length)
            self.MainTurtle.down()
            self.MainTurtle.goto(x,-self.length)
        for y in range(self.startend[0],self.startend[1]+1,self.gridsize):
            self.MainTurtle.up()
            self.MainTurtle.goto(self.length,y)
            self.MainTurtle.down()
            self.MainTurtle.goto(-self.length,y)
    def Start(self):
        self.MainTurtle.speed(200)
        if not self.ShowTurtles:
            self.MainTurtle.hideturtle()
        self.Grid()
        self.MineText.goto(self.length,-self.length)
        self.flagmodetext.goto(self.length,self.length-15)
        stras = str(self.flagmodebool)
        self.flagmodetext.setext("Flag Mode: "+ stras)
        self.MineText.setext(str(self.Mines- len(self.flags))+" flags left")
        self.GenMines()
        #print(self.mines)
        self.Screen.listen()
        self.Screen.onclick(self.OnClick)
        self.Screen.onkey(self.FlagMode, self.FlagModeKey)
    def endgame(self,Won):
        self.GameEnded = True
        texta = createtext()
        colour = "Red"
        texa = "You Lost"
        texta.goto(0,0)
        if Won:
            texa = "You Won"
            colour = "Green"
        for index,value in self.mines.items():
            self.DrawMine(value[0],value[1])
        texta.set(('Arial', 30),"center",colour)
        texta.setext(texa)
MineSweeper().Start()
exitout = False
def endexit():
    global exitout
    exitout = True
    exit()
turtle.onkey(endexit,"Escape")
turtle.mainloop()
for i in range(99999):
    if exitout:
        break
    time.sleep(1)

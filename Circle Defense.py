from tkinter.tix import Tree
import turtle as t 
import math
import time

screen = t.Screen()
ScreenSize = 400
backgroundcolor = "lime"
HideTurtles = True
DrawYourOwnPath = True
MakeWayPoints = False
screen.setup(ScreenSize,ScreenSize)
screen.bgcolor(backgroundcolor)
if MakeWayPoints:
    def printpos(x,y):
        print('['+str(x)+','+str(y)+'],',end = "")
    screen.onclick(printpos)
    exit()
class CircleDefense():
    Path = [[191,23],[18,21],[16,132],[-84,149],[-201,139]]
    
    def OnClick(self,x,y):
        mode = self.Mode
        if mode == "DrawPath":
            if abs(x) >= (ScreenSize/2)-5 and x <0:
                self.Path.append([-ScreenSize/2,y])
                self.Mode = None
            else:
                self.Path.append([x,y])
            self.lineturtle.down()
            self.lineturtle.goto(self.Path[len(self.Path)-1][0],self.Path[len(self.Path)-1][1])
            self.lineturtle.up()
    def DrawPath(self):
        for v in self.Path:
            self.lineturtle.goto(v[0],v[1])
            self.lineturtle.down()
    def loop(self,varible,value):
        if self.__dict__[varible] == value:
            return True
        else:
            time.sleep(.1)
            self.loop(varible,value)
    def __init__ (self):
        self.lineturtle = t.Turtle()
        self.lineturtle.speed(0)
        if HideTurtles:
            self.lineturtle.hideturtle()
        self.lineturtle.up()
        self.Mode = None
        if DrawYourOwnPath:
            self.Path = [[ScreenSize/2,0]]
            self.lineturtle.goto(self.Path[0][0],self.Path[0][1])
            self.Mode = "DrawPath"
        else:
            self.DrawPath()
        self.loop("Mode",None)
        print("c")
CircleDefense()
exitout = False
def endexit():
    global exitout
    exitout = True
    exit()
screen.onkey(endexit,"Escape")
t.mainloop()
for i in range(99999):
    if exitout:
        break
    time.sleep(1)
from datetime import datetime
import random
import turtle
import math
import time
#Work In Progress
screen = turtle.Screen()
screen.register_shape("triangle", ((5,-3), (0,5), (-5,-3)))
ScreenSize = 400
backgroundcolor = "lime"
HideTurtles = True
DrawYourOwnPath = False or ScreenSize != 400
MakeWayPoints = False
screen.setup(ScreenSize,ScreenSize)
bordert = turtle.Turtle()
bordert.hideturtle()
bordert.speed(0)
bordert.up()
bordert.goto((-ScreenSize/2),(-ScreenSize/2))
bordert.down()
bordert.fillcolor(backgroundcolor)
bordert.pensize(10)
bordert.begin_fill()
for i in range(4):
    bordert.forward(ScreenSize)
    bordert.left(90)
bordert.end_fill()
#screen.bgcolor(backgroundcolor)
if MakeWayPoints:
    def printpos(x,y):
        print('['+str(x)+','+str(y)+'],',end = "")
    screen.onclick(printpos)
    exitout = False
    def endexit():
        global exitout
        exitout = True
        exit()
    screen.onkey(endexit,"Escape")
    turtle.mainloop()
class CircleDefense():
    Prebuilt = [[[191,23],[18,21],[16,132],[-84,149],[-201,139]],[[191,23],[58,15],[-49,-75],[-119,5],[-118,113],[-200,117]]]
    class Enemy():
        EnemyInfo = {
            "arrow" : {
                'Shape' : 'arrow',
                'Health' : 10,
                'Color' : 'Yellow',
                'Speed' : 2,
                'HealthToSizeOffset' : 1/20,
                'SizeChangeWithHp' : True, 
            } 
        }
        def  GetDirec(self,p):
            a = self.Position
            x,y = (p[0]-a[0]),(p[1]-a[1])
            mag = self.GetMag(p)
            return [x/mag,y/mag]
        def GetMag(self,p):
            a = self.Position
            return math.sqrt((p[0]-a[0])**2+(p[1]-a[1])**2)
        def LookAt(self,p):
            self.Turtle.left(self.Turtle.towards(p[0], p[1]) - self.Turtle.heading())
        def update(self):
            if self.ReachedEnd: return
            if self.SizeChangeWithHp:
                self.Turtle.shapesize(self.Health*self.offset<0.25 and 0.25 or self.Health*self.offset)
            speed = self.Speed
            self.Turtle.color(self.Color)
            currentwayp = self.GameInfo.Path[self.CurrentWayPoint]
            self.LookAt(currentwayp)
            self.Turtle.clear()
            if self.GetMag(currentwayp) <=speed:
                speed = self.GetMag(currentwayp)
            self.Turtle.forward(speed)
            self.Position = list(self.Turtle.pos())
            if self.GetMag(currentwayp) <=0.5:
                if self.CurrentWayPoint+1 == len(self.GameInfo.Path):
                    self.ReachedEnd = True
                    print("ReachedEnd")
                else:
                    self.CurrentWayPoint += 1
            if not self.ReachedEnd:
                screen.ontimer(self.update,1)
        def __init__ (self,GameInfo,Enemy):
            if not(Enemy in self.EnemyInfo): return
            self.type = Enemy
            self.Position = GameInfo.Path[0]
            self.ReachedEnd = False
            self.GameInfo = GameInfo
            self.Health = self.EnemyInfo[Enemy]["Health"] 
            self.Speed = self.EnemyInfo[Enemy]["Speed"] 
            self.Color = self.EnemyInfo[Enemy]["Color"]
            self.Turtle = turtle.Turtle(self.EnemyInfo[Enemy]["Shape"])
            self.offset = self.EnemyInfo[Enemy]["HealthToSizeOffset"] 
            self.SizeChangeWithHp = self.EnemyInfo[Enemy]["SizeChangeWithHp"] 
            self.Turtle.hideturtle()
            self.Turtle.up()
            self.Turtle.speed(0)
            self.Turtle.color(self.Color)
            self.Turtle.shapesize(self.Health*self.offset)
            self.Turtle.goto(GameInfo.Path[0])
            self.Turtle.showturtle()
            self.CurrentWayPoint = 1
            self.update()
    def OnClick(self,x,y):
        mode = self.Mode
        if mode == "DrawPath":
            if abs(x) >= (ScreenSize/2)-15 and x <0:
                self.Path.append([-ScreenSize/2,y])
                self.Mode = None
            else:
                self.Path.append([x,y])
            self.lineturtle.down()
            self.lineturtle.goto(self.Path[len(self.Path)-1][0],self.Path[len(self.Path)-1][1])
            self.lineturtle.up()
    def Loop(self):
        for enemy in self.Enemys:
            enemy.update()
        screen.ontimer(self.Loop,10)
    def NextPart(self):
        self.Enemys = [self.Enemy(self,"arrow")]
        time.sleep(1)
        self.Enemys.append(self.Enemy(self,"arrow"))
        #self.Loop()
    def DrawPath(self):
        for v in self.Path:
            self.lineturtle.goto(v[0],v[1])
            self.lineturtle.down()
    def __init__ (self):
        self.Path = []
        self.lineturtle = turtle.Turtle()
        self.lineturtle.speed(0)
        self.lineturtle.color("Brown")
        self.lineturtle.pensize(10)
        if HideTurtles:
            self.lineturtle.hideturtle()
        self.lineturtle.up()
        self.Mode = None
        screen.onclick(self.OnClick)
        if DrawYourOwnPath:
            self.Path = [[ScreenSize/2,0]]
            self.lineturtle.goto(self.Path[0][0],self.Path[0][1])
            self.Mode = "DrawPath"
        else:
            self.Path = self.Prebuilt[random.randint(0,len(self.Prebuilt)-1)]
            self.DrawPath()
        once = False
        def loop():
            if self.Mode == None:
                return self.NextPart() 
            return screen.ontimer(loop,1)
        loop()
CircleDefense()
exitout = False
def endexit():
    global exitout
    exitout = True
    exit()
screen.onkey(endexit,"Escape")
turtle.mainloop()
for i in range(99999):
    if exitout:
        break
    time.sleep(1)

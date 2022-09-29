import turtle 
import time as task
import random
import math
def clamp(num, min_value, max_value):
    return max(min(num, max_value), min_value)
class HitTheCircle():
    Rate = 1 #How much circles will spawn per second
    RadiusSize = 20 #circle radius
    Color = "red" #circle color
    GridRangex = [-150,150] # x range
    GridRangey = [-50,100] # y range
    MaxTime = 24 #how much time
    MaxTime = clamp(MaxTime,1,9999)
    #Not Reccomened to edit these
    Speed = 10
    Score = 0
    Turtle = None
    Screen = None
    CurrentPos = [0,0]
    GameEnd = False
    Clicked = False
    HitTurtle = None
    ScoreTurtle = None
    TimerTurtle = None
    StartTime = None
    def AABB(self,x,y):
        circlex = self.CurrentPos[0] +self.RadiusSize/(self.RadiusSize/5)
        circley = self.CurrentPos[1]+self.RadiusSize
        distance = math.sqrt((x-circlex )*(x-circlex)+(y-circley)*(y-circley))
        return distance < self.RadiusSize
    def CreateCircle(self):
        self.Turtle.goto(self.CurrentPos[0],self.CurrentPos[1])
        self.Turtle.clear()
        self.Turtle.begin_fill()
        self.Turtle.circle(self.RadiusSize)
        self.Turtle.end_fill()  
    def UpdateScore(self):
        self.ScoreTurtle.clear()
        self.ScoreTurtle.goto(130,170)
        self.ScoreTurtle.color("Black")
        style = ('Arial', 11, 'bold')
        self.ScoreTurtle.write("Score: "+str(self.Score),font=style,align='Right')
    def UpdateTime(self):
        self.TimerTurtle.clear()
        self.TimerTurtle.goto(-200,170)
        self.TimerTurtle.color("Black")
        style = ('Arial', 11, 'bold')
        self.TimerTurtle.write("Time Left: "+str(self.MaxTime-math.floor(task.time()-self.StartTime+0.5))+" Seconds",font=style,align='Left')
        if self.MaxTime-math.floor(task.time()-self.StartTime+0.5) <= 0:
            self.EndGame()
    def OnCLick(self,x,y):
        if self.GameEnd:
            return
        self.HitTurtle.clear()
        self.HitTurtle.goto(x,y)
        self.HitTurtle.color("Black")
        style = ('Arial', 10, 'bold')
        self.Clicked = True
        text = "Miss"
        if self.AABB(x,y):
            self.HitTurtle.color("Green")
            self.Score +=1
            self.UpdateScore()
            text = "Hit"
        self.HitTurtle.write(text,font=style,align='center')
        self.Loop(True)
    def GeneratePosition(self):
        x = random.randrange(self.GridRangex[0],self.GridRangex[1])
        y = random.randrange(self.GridRangey[0],self.GridRangey[1])
        self.CurrentPos = [x,y]
    def Loop(self):
        self.UpdateTime()
        if not self.GameEnd:
            self.GeneratePosition()
            self.CreateCircle()
            for i in range(0,int(self.Rate*100),1):
                task.sleep(0.01)
                if self.Clicked:
                    self.Clicked = False
                    break
            self.Loop()
    def StartGame(self):
        self.StartTime = task.time()
        self.Screen = turtle.Screen()
        self.Turtle = turtle.Turtle()
        self.TimerTurtle = turtle.Turtle()
        self.TimerTurtle.up()
        self.TimerTurtle.hideturtle()
        self.HitTurtle = turtle.Turtle()
        self.ScoreTurtle = turtle.Turtle()
        self.ScoreTurtle.hideturtle()
        self.Turtle.hideturtle()
        self.HitTurtle.hideturtle()
        self.ScoreTurtle.speed(10)
        self.HitTurtle.speed(10)
        self.HitTurtle.up()
        self.ScoreTurtle.up()
        self.Turtle.up()
        self.Turtle.speed(10)
        self.Turtle.fillcolor(self.Color)
        self.Screen.onclick(self.OnCLick)
        turtle.onkey(self.EndGame,"Escape")
        self.UpdateScore()
        self.Screen.listen()
        self.Loop()
    def EndGame(self):
        self.GameEnd = True
        TimeUp = turtle.Turtle()
        TimeUp.up()
        TimeUp.speed(10)
        TimeUp.hideturtle()
        style = ('Arial', 25, 'bold')
        TimeUp.goto(0,0)
        TimeUp.write("Times Up!",font=style,align='center')   
        TimeUp.goto(0,-50)
        style = ('Arial', 20, 'bold')
        TimeUp.write(str(self.Score)+" Score",font=style,align='center')   
        exit()
    
HitTheCircle().StartGame()
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
    task.sleep(1)

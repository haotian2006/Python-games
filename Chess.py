from copy import copy
import turtle
import time
cc = turtle.Turtle()
cc.up()
#there is currently no warning to tell that you are in check or checkmate
class Chess:
    #<--Classes-->
    class CreatePeice:
        def __init__ (self,Team,classtype):
            self.Icon = createtext()
            self.Team = Team # 0 for none 1 for white -1 for black
            self.Position =[0,0]
            self.Moves = 0
            self.ClassType = classtype
            self.Icon.text(classtype)
        def GetPosAsString(self):
            return str(self.Position[0])+","+str(self.Position[1])
        def combinevector2(self,x,y):
            return str(x)+","+str(y)
        def GetPos(self):
            return self.Position[0],self.Position[1]
        def GetMoves(self):
            return self.Moves
        def GetClass(self):
            return self.ClassType    
        def GetUnit(self,p1,p2):
            return [p1[0]-p2[0],p1[1]-p2[1]]
        def GoTo(self,x,z):
            self.Moves +=1
            self.Position[0] = x
            self.Position[1] = z
            self.Icon.goto(x,z)
            self.Icon.updatetp()
        def OnDeath(self):
            self.Icon.clear()
            self.Position = None
        def GetTeam(self):
            return self.Team    
        def CheckIfCanMove(self,x,y,LandingOn,AllPeicesTable):
            if LandingOn and LandingOn != True and LandingOn.GetClass() == "King": return False 
            AllPossibleMoves = {} #["1,3"] = False,False,False -- CanBeBlocked?,GoAsFarAsPossible?,CanEat?
            moves = self.moves
            for data in moves:
                if data == None: continue
                if self.Moves > data[1][4] and data[1][4] !=0: continue
                row,on = 1,1
                ori = None
                point = None
                direaction = [0,0]
                for num in data[0]:#finds ori and gotopoint
                    if num == 0:
                        ori = [on,row]
                    elif num == 2:
                        point = [on,row]
                    if point != None and ori != None:
                        break
                    if on%3 ==0:
                        on = 0
                        row+=1
                    on += 1
                if ori == None or point == None:
                    print(self.ClassType,"Has a Bugged Movement")
                direaction = self.GetUnit(ori,point)
                if data[1][0]:
                    rx,ry = direaction[0], direaction[1]
                    AllPossibleMoves[self.combinevector2(rx,ry)] =[ data[1][1],data[1][2],data[1][3],data[1][5]]
                    rx,ry = -direaction[0], direaction[1]
                    AllPossibleMoves[self.combinevector2(rx,ry)] =[ data[1][1],data[1][2],data[1][3],data[1][5]]
                    rx,ry = direaction[0], -direaction[1]
                    AllPossibleMoves[self.combinevector2(rx,ry)] = [data[1][1],data[1][2],data[1][3],data[1][5]]
                    rx,ry = -direaction[0], -direaction[1]
                    AllPossibleMoves[self.combinevector2(rx,ry)] = [data[1][1],data[1][2],data[1][3],data[1][5]]
                    rx,ry = direaction[1], direaction[0]
                    AllPossibleMoves[self.combinevector2(rx,ry)] =[ data[1][1],data[1][2],data[1][3],data[1][5]]
                    rx,ry = -direaction[1], direaction[0]
                    AllPossibleMoves[self.combinevector2(rx,ry)] = [data[1][1],data[1][2],data[1][3],data[1][5]]
                    rx,ry = direaction[1], -direaction[0]
                    AllPossibleMoves[self.combinevector2(rx,ry)] = [data[1][1],data[1][2],data[1][3],data[1][5]]
                    rx,ry = -direaction[1], -direaction[0]
                    AllPossibleMoves[self.combinevector2(rx,ry)] = [data[1][1],data[1][2],data[1][3],data[1][5]]
                elif self.Team == -1:
                    direaction[0],direaction[1] = -direaction[0], -direaction[1]
                    AllPossibleMoves[self.combinevector2(direaction[0],direaction[1])] = [data[1][1],data[1][2],data[1][3],data[1][5]]
                else:
                    AllPossibleMoves[self.combinevector2(direaction[0],direaction[1])] = [data[1][1],data[1][2],data[1][3],data[1][5]]
            team = self.Team
            cx,cy = self.GetPos()
            unit = self.GetUnit([x,y],[cx,cy])
            unit[0] = unit[0]//50
            unit[1] = unit[1]//50
            cmpunit = self.combinevector2(unit[0],unit[1])
            biggerthan1 = False
            same = False
            Yes = False
            unit1 = copy(unit)
            xsing = int(unit[0]/abs(unit[0]) if unit[0] !=0 else 1)
            ysing = int(unit[1]/abs(unit[1]) if unit[1] !=0 else 1)
            L = True
            for d,info in AllPossibleMoves.items():
                if cmpunit == d and not info[1]:
                    L = False
                    break
            if abs(unit[0]) == abs(unit[1]):
                same = True
            if L:
                #print((abs(unit[0]) != 2 or abs(unit[1]) == 0) , (abs(unit[1]) != 2 or abs(unit[0]) == 0),abs(unit[0])>abs(unit[1]))
                if abs(unit[0]) > 1 or abs(unit[1]) > 1:
                    biggerthan1 = True
                    if abs(unit[0]) == abs(unit[1]):
                        unit1 = [1,1]
                    elif abs(unit[0])>abs(unit[1]) and ((abs(unit[0]) != 2 or abs(unit[1]) == 0) and (abs(unit[1]) != 2 or abs(unit[0]) == 0) or  same):
                        unit1 = [xsing*(abs(unit[0])-abs(unit[1])),0]
                        unit2 = copy(unit1)
                        if abs(unit[0]) -1 == abs(unit[1]):
                            if abs(unit[0]) >2:
                                unit2 = [2,1]
                        #print(unit2)
                        if unit[1] == 0 and ((abs(unit2[0]) != 2 or abs(unit2[1]) == 0) and (abs(unit2[1]) != 2 or abs(unit2[0]) == 0) or  same) :
                            unit1 = [xsing*1,0]
                    elif (abs(unit[0]) != 2 or abs(unit[1]) == 0) and (abs(unit[1]) != 2 or abs(unit[0]) == 0) or  same :
                        if unit[0] == 0:
                            unit1 = [0,ysing*1]
            old = cmpunit
            cmpunit = self.combinevector2(int(unit1[0]),int(unit1[1])) 
            for d,info in AllPossibleMoves.items():
                if cmpunit == d or old == d :
                    can = None
                    if same and info[1]:#checks if its diagonal and can go forever
                        Yes = True
                        #print("d")
                        can = [unit,info[0],info[1],info[2]]
                    elif not info[1] and not biggerthan1 and same: #checks if its dia but cannot goforver
                        Yes = True
                        #print("c")
                        can = [unit,info[0],info[1],info[2]]
                    elif not info[1] and not same and not biggerthan1: # cannot goforever and is foward
                        Yes = True
                        #print("b")
                        can = [unit,info[0],info[1],info[2]]
                    elif not same and info[1]: #checks if it can go foward but  forever
                        #print("a")
                        Yes = True
                        can = [unit,info[0],info[1],info[2]]
                    if  LandingOn != None and info[3]:
                        if LandingOn == True and old != cmpunit:
                            continue
                        Yes = True
                        break
                    if (can != None and( LandingOn and not info[2])or info[3]):
                        Yes = False
                        continue
                    if can != None and info[0]:
                        ax,ay = 0,0
                        splited = old.split(",")
                        ccx = abs(int(splited[0]))
                        ccy = abs(int(splited[1]))
                        for i in range(10):
                            ax += int(xsing*1) if ccx != 0 else 0
                            ay += int(ysing*1) if ccy != 0 else 0
                            ccx -= 1
                            ccy -=1
                            if ccx <0:
                                ccx = 0
                            if ccy <0:
                                ccy = 0
                            nx = cx+ax*50
                            ny = cy+ay*50
                            string2 = str(nx)+','+str(ny)   
                            if (ccy == 0 and ccx ==0) :
                                break                  
                            #self.HighLightClear()   
                            if string2 in AllPeicesTable :
                                 global cc
                                 #print(ax,ay,old)
                                 cc.goto(nx,ny)
                                 Yes = False
                                 break
            return  Yes                                  
    class Pawn(CreatePeice):
        moves = [None,None,None,None,None,None,None,None]
        moves[0] = [ #1(any) = surrounding 2 = path 0 = origin
            [
            1,2,1,
            1,0,1,
            1,1,1
            ],
            [False,True,False,False,0,False], #Rotate?, CanBeBlocked?,GoAsFarAsPossible?,CanEat?,HowMuchMoves?      
        ]
        moves[1] = [ #1(any) = surrounding 2 = path 0 = origin
            [
            1,1,2,
            1,0,1,
            1,1,1
            ],
            [False,False,False,True,0,True], #Rotate?, CanBeBlocked?,GoAsFarAsPossible?,CanEat?,HowMuchMoves?,Special?      
        ]
        moves[2] = [ #1(any) = surrounding 2 = path 0 = origin
            [
            2,1,1,
            1,0,1,
            1,1,1
            ],
            [False,False,False,True,0,True], #Rotate?, CanBeBlocked?,GoAsFarAsPossible?,CanEat?,HowMuchMoves?,Special?        
        ]
        moves[3] = [ #1(any) = surrounding 2 = path 0 = origin
            [
            1,2,1,
            1,1,1,
            1,0,1
            ],
            [False,True,False,False,1,False], #Rotate?, CanBeBlocked?,GoAsFarAsPossible?,CanEat?,HowMuchMoves?      
        ]
        def __init__ (self,Team,Type):
            self.Icon = createtext()
            self.Team = Team
            self.Position =[0,0]
            super().__init__(Team, Type)
    class King(CreatePeice):
        moves = [None,None,None,None,None,None,None,None]
        moves[0] = [ #1(any) = surrounding 2 = path 0 = origin
            [
            1,2,1,
            1,0,1,
            1,1,1
            ],
            [True,True,False,True,0,False], #Rotate?, CanBeBlocked?,GoAsFarAsPossible?,CanEat?,HowMuchMoves?      
        ]
        moves[1] = [ #1(any) = surrounding 2 = path 0 = origin
            [
            1,1,2,
            1,0,1,
            1,1,1
            ],
            [True,True,False,True,0,False], #Rotate?, CanBeBlocked?,GoAsFarAsPossible?,CanEat?,HowMuchMoves?      
        ]
        def __init__ (self,Team,Type):
            self.Icon = createtext()
            self.Team = Team
            self.Position =[0,0]
            super().__init__(Team, Type)
    class Queen(CreatePeice):
        moves = [None,None,None,None,None,None,None,None]
        moves[0] = [ #1(any) = surrounding 2 = path 0 = origin
            [
            1,2,1,
            1,0,1,
            1,1,1
            ],
            [True,True,True,True,0,False], #Rotate?, CanBeBlocked?,GoAsFarAsPossible?,CanEat?,HowMuchMoves?      
        ]
        moves[1] = [ #1(any) = surrounding 2 = path 0 = origin
            [
            1,1,2,
            1,0,1,
            1,1,1
            ],
            [True,True,True,True,0,False], #Rotate?, CanBeBlocked?,GoAsFarAsPossible?,CanEat?,HowMuchMoves?      
        ]
        def __init__ (self,Team,Type):
            self.Icon = createtext()
            self.Team = Team
            self.Position =[0,0]
            super().__init__(Team, Type)   
    class Rook(CreatePeice):
        moves = [None,None,None,None,None,None,None,None]
        moves[0] = [ #1(any) = surrounding 2 = path 0 = origin
            [
            1,2,1,
            1,0,1,
            1,1,1
            ],
            [True,True,True,True,0,False], #Rotate?, CanBeBlocked?,GoAsFarAsPossible?,CanEat?,HowMuchMoves?      
        ]
        moves[1] = [ #1(any) = surrounding 2 = path 0 = origin
            [
            1,1,1,
            1,0,2,
            1,1,1
            ],
            [True,True,True,True,0,False], #Rotate?, CanBeBlocked?,GoAsFarAsPossible?,CanEat?,HowMuchMoves?      
        ]
        def __init__ (self,Team,Type):
            self.Icon = createtext()
            self.Team = Team
            self.Position =[0,0]
            super().__init__(Team, Type) 
    class Bishop(CreatePeice):
        moves = [None,None,None,None,None,None,None,None]
        moves[0] = [ #1(any) = surrounding 2 = path 0 = origin
            [
            1,1,2,
            1,0,1,
            1,1,1
            ],
            [True,True,True,True,0,False], #Rotate?, CanBeBlocked?,GoAsFarAsPossible?,CanEat?,HowMuchMoves?      
        ]
        def __init__ (self,Team,Type):
            self.Icon = createtext()
            self.Team = Team
            self.Position =[0,0]
            super().__init__(Team, Type)
    class Knight(CreatePeice):
        moves = [None,None,None,None,None,None,None,None]
        moves[0] = [ #1(any) = surrounding 2 = path 0 = origin
            [
            1,1,2,
            1,1,1,
            1,0,1
            ],
            [True,False,False,True,0,False], #Rotate?, CanBeBlocked?,GoAsFarAsPossible?,CanEat?,HowMuchMoves?      
        ]
        def __init__ (self,Team,Type):
            self.Icon = createtext()
            self.Team = Team
            self.Position =[0,0]
            super().__init__(Team, Type)  
   
 
               
    #<--Settings-->
    TeamColor = ["dark olive green","black"]
    colors = ["old lace","peru"]
    ShowTurtles = False
    HighLightColor = "indigo"
    abbreviation = {
    'P':['Pawn',Pawn],
    'H':['Knight',Knight],
    'R':['Rook',Rook],
    'B':['Bishop',Bishop],
    'Q':['Queen',Queen],
    'K':['King',King]
    }
    SetUpW = list("PPPPPPPPRHBQKBHR")
    SetUpB = list("RHBQKBHRPPPPPPPP")
    #<--Other-->
    gridlength = 200
    gridsize = 50
    start = [gridlength,-gridlength]
    def combinevector2(self,x,y):
        return str(x)+","+str(y)
    def CheckInCheckMate(self,team):
        KingP = [0,0]
        for pos,data in self.Peices.items():
            if data.GetClass() == "King" and data.GetTeam() == team:
                a = pos.split(",")
                KingP = [int(a[0]),int(a[1])]
        timesincheck = 0
        kingincheck = False        
        for x in range(KingP[0]-50,KingP[0]+51,50):
            for y in range(KingP[1]-50,KingP[1]+51,50):
                combinedsl = self.combinevector2(KingP[0],KingP[1])                            
                obj = self.Peices[combinedsl]
                clonedpeices = dict(self.Peices)
                clonedpeices.pop(combinedsl)
                clonedpeices[self.combinevector2(x,y)] = obj 
                if self.combinevector2(x,y) in self.Peices and self.Peices[self.combinevector2(x,y)].GetTeam() == team and not (x == KingP[0] and y == KingP[1]):
                    timesincheck +=1
                    continue
                if self.CheckInCheck(team,clonedpeices) or abs(x) >200 or abs(y) >200 :
                    if x == KingP[0] and y == KingP[1]:
                        kingincheck = True
                    timesincheck +=1
                del clonedpeices
        return timesincheck == 9
    def CheckInCheck(self,team,Peices):
        KingP = [0,0]
        InCheck = False
        placeholder = self.Pawn(team,"Pawn")
        for pos,data in Peices.items():
            if data.GetClass() == "King" and data.GetTeam() == team:
                a = pos.split(",")
                KingP = [int(a[0]),int(a[1])]
        for pos,data in Peices.items():
            if data.GetTeam() ==  -team:
                if data.CheckIfCanMove(KingP[0],KingP[1],True,Peices):  
                    InCheck = True 
                    #print(data.GetClass())
                    break
        placeholder = None
        return InCheck
    def roundtogrid(self,x,y):
        x -= 25
        y -= 25
        x,y = round(x/self.gridsize)*self.gridsize,round(y/self.gridsize)*self.gridsize
        x += 25
        y += 25
        self.MainTurtle.goto(x,y)
        return x,y
    def CreatePeices(self):
        currentyindex = -125
        currentx = -175
        for classtype in self.SetUpW:
            Peice = self.abbreviation[classtype][1](1,self.abbreviation[classtype][0])
            Peice.Icon.setcolor(self.TeamColor[0])
            Peice.GoTo(currentx,currentyindex)
            self.Peices[self.combinevector2(currentx,currentyindex)] = Peice
            currentx+=50
            if currentx >175:
                currentx = -175
                currentyindex -= 50
        currentyindex = 175
        currentx = -175
        for classtype in self.SetUpB:
            Peice = self.abbreviation[classtype][1](-1,self.abbreviation[classtype][0])
            Peice.Icon.setcolor(self.TeamColor[1])
            Peice.GoTo(currentx,currentyindex)
            self.Peices[self.combinevector2(currentx,currentyindex)] = Peice
            currentx+=50
            if currentx >175:
                currentx = -175
                currentyindex -= 50                
        currentyindex = 175
    def HighLight(self,x,y):
        self.SelectedCoord = [x,y]
        x -= 25
        y -=25
        self.THighLight.up()
        self.THighLight.clear()
        self.THighLight.goto(x,y)
        self.THighLight.color(self.HighLightColor)
        self.THighLight.setheading(0)
        self.THighLight.down()
        for i in range(4):
            self.THighLight.right(90)
            self.THighLight.forward(-self.gridsize)
            self.BreakHH = False
            if self.BreakHH:
                self.BreakHH = False
                break
        self.THighLight.up()
    def HighLightClear(self):
        self.BreakHH = True
        self.SelectedCoord = None
        self.THighLight.clear()        
    def DrawTile(self,x,y):
        self.MainTurtle.up()
        self.MainTurtle.goto(x,y)
        self.MainTurtle.begin_fill()
        self.currentgridcolor = 1 if self.currentgridcolor == 0 else 0
        self.MainTurtle.color(self.colors[self.currentgridcolor])
        self.MainTurtle.setheading(0)
        for i in range(4):
            self.MainTurtle.right(90)
            self.MainTurtle.forward(-self.gridsize)
        self.MainTurtle.end_fill()
    def OnClick(self,x,y):
        x,y = self.roundtogrid(x,y)
        combined = self.combinevector2(x,y)
        if  abs(x)>200 or abs(y)>200:
             self.HighLightClear()
             return
        if not self.SelectedCoord and combined in self.Peices and self.Peices[combined].GetTeam() == self.Turn and abs(x) <= self.start[0] and abs(y) <= self.start[0] :
            self.SelectedCoord = [x,y]
            self.HighLight(x,y)
            return
        elif self.SelectedCoord != None  :
            xc,yc = self.SelectedCoord[0],self.SelectedCoord[1]
            combinedsl = self.combinevector2(xc,yc)
            if not (combinedsl in self.Peices):
                self.HighLightClear()
                return
            obj = self.Peices[combinedsl]
            landingon = self.Peices[combined] if combined in self.Peices else None
            clonedpeices = dict(self.Peices)
            clonedpeices.pop(combinedsl)
            clonedpeices[combined] = obj       
            if not obj.CheckIfCanMove(x,y,landingon,self.Peices) or ((combined in self.Peices and self.Peices[combined].GetTeam() == self.Turn)) or (self.CheckInCheck(self.Turn,clonedpeices)and obj.GetClass() != "King" ):
                self.HighLightClear()
                return
            if obj.GetClass() == "King" and  self.CheckInCheck(self.Turn,clonedpeices):
                #print(self.CheckInCheck(self.Turn,clonedpeices),self.Turn)
                self.HighLightClear()
                return 
            if combined in self.Peices:
                landingon.OnDeath()
            self.Peices[combinedsl].GoTo(x,y)
            self.Peices[combined] = self.Peices[combinedsl]
            del self.Peices[combinedsl] 
            self.InCheck = 0
            if y == 175*self.Turn and obj.GetClass() == "Pawn":
                self.Peices[combined].OnDeath()
                self.Peices[combined] = None
                self.Peices[combined] = self.Queen(self.Turn,"Queen")
                c = 0 if self.Turn == 1 else 1
                self.Peices[combined].Icon.setcolor(self.TeamColor[c])
                self.Peices[combined].GoTo(x,y)
            self.Turn = -self.Turn
            if self.CheckInCheck(self.Turn,clonedpeices):
                self.InCheck = self.Turn
            del clonedpeices
        self.HighLightClear()
    def __init__ (self):
        self.BreakHH = False
        self.THighLight = turtle.Turtle()
        self.SelectedCoord = None
        self.Turn = 1
        self.InCheck = 0
        self.THighLight.speed(0)
        self.THighLight.pensize(4)
        self.MainTurtle = turtle.Turtle()
        self.MainTurtle.speed(0)
        if not self.ShowTurtles:
            self.MainTurtle.hideturtle()
            self.THighLight.hideturtle()
            global ccc
            cc.hideturtle()
        self.Screen = turtle.Screen()
        self.currentgridcolor = 1
        self.Screen.bgcolor("white")
        self.CurrentlyDone = [self.start[1],self.start[0]]
        self.CreateGrid()
        self.Peices = {}
        self.MainTurtle.color("Black")
        self.CreatePeices()
        self.Screen.onclick(self.OnClick)       
    def CreateGrid(self):
        self.MainTurtle.up()
        for x in range(self.CurrentlyDone[0],self.CurrentlyDone[1],self.gridsize):
            self.currentgridcolor = 1 if self.currentgridcolor == 0 else 0
            for y in range(self.CurrentlyDone[0],self.CurrentlyDone[1],self.gridsize):
                self.DrawTile(x,y)
class createtext:
    #Simple text Module Created by hao
    def __init__(self):
        self.style = "" 
        self.align = ""
        self.Text = ""
        self.color = "Black"
        self.style = ('Arial', 10,"bold")
        self.align = "center"
        self.turtlea = turtle.Turtle()
        self.turtlea.hideturtle()
        self.turtlea.speed(0)
        self.turtlea.up()
    def set(self,style,align,color):
        self.style,self.align,self.color = style,align,color
    def setcolor(self,color):
        self.color = color
    def setalign(self,align):
        self.align = align
    def setstyle(self,style):
        self.align = style
    def getturtle(self):
        return self.turtlea
    def goto(self,x,y):
        self.turtlea.goto(x,y)
    def clear(self):
        self.turtlea.clear()
    def updatetp(self):
        self.setext(self.Text)
    def text(self,Text):
        self.Text = Text
    def setext(self,text):
        self.Text = text
        self.turtlea.color(self.color)
        self.clear()
        self.turtlea.write(text,font=self.style,align=self.align)            
Chess()
turtle.mainloop()
time.sleep(9999)

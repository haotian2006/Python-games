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

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

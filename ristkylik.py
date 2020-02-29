import turtle

def ristkylik_vasak():    
    global ristkylikVasak 
    ristkylikVasak = turtle.Turtle()
    ristkylikVasak.color ('white')    #turtle alustab keskelt
    ristkylikVasak.shape('square')    #pisike kastike väljaku keskel, sellest kuj välja ristkülik
    ristkylikVasak.shapesize(stretch_len=1, stretch_wid=5) #ruudust sai ristkülik
    ristkylikVasak.penup()            #ristküliku viimisega keskelt vasakule tekkiva joone varjamine
    ristkylikVasak.goto(-450,0)       #viisime ristküliku väljaku keskelt vasakule

def ristkylik_parem():  
    global ristkylikParem  
    ristkylikParem = turtle.Turtle()
    ristkylikParem.color ('white')
    ristkylikParem.shape('square')
    ristkylikParem.shapesize(stretch_len=1, stretch_wid=5)
    ristkylikParem.penup()
    ristkylikParem.goto(450,0)

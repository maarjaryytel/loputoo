def aken():    
    import turtle
    global aken
    aken = turtle.Screen()
    aken.title("PING-PONG")
    aken.setup(width=1.0, height=1.0)
    aken.bgcolor("black")
    aken.tracer(1)                    #kiirendab palli liikumist
    aken.mainloop() 

def valjak():
    import turtle
    border = turtle.Turtle()          
    border.speed(0)                   #väljaku äärte joonistamise kiirus
    border.color('dark blue')
    border.begin_fill()               #alustab väljaku täitmist
    border.goto(-500,300)             #väljaku keskelt ülesse vasakusse nurka
    border.goto(500,300)              #ülemisest vasakust nurgast ülemisse paremasse nurka
    border.goto(500,-300)             #ülemisest paremast nurgast alla paremasse nurka
    border.goto(-500,-300)            #alt paremast nurgast alla vasakusse nurka
    border.goto(-500,300)             #alt vasakust nurgast ülesse vasakusse nurka
    border.end_fill()                 #lõpetab väljaku täitmise
    
    border.goto(0,300)                #väljaku keskele joone joonistamine
    border.color('white')
    border.setheading(270)            #ülevalt keskelt läheb alla keskele
    for i in range(25):               #väljaku keskel asuvate valgete kriipsukeste saamiseks
        if i%2 ==0:
            border.forward(24)
        else:
            border.up()
            border.forward(24)
            border.down()

    
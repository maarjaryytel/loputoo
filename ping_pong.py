#mängija nimed, edetabel skooridest
#vahetab värvi


import turtle                      
from random import choice, randint  #1- võimaldab pallil liikuda suvalises suunas
                                    #2- et pall ei liiguks alati keskele tagasi, vaid ka mujale- randint


aken = turtle.Screen()
aken.title("PING-PONG")
aken.setup(width=1.0, height=1.0)
aken.bgcolor("black")
aken.tracer(1)                    #kiirendab palli liikumist

border = turtle.Turtle()          #
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
for i in range(25):               #??????????miks ta seda tegi, valgete kriipsukeste saamiseks
    if i%2 ==0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()
border.hideturtle()               #kaotab noolekese ehk turtle ära

ristkylikVasak = turtle.Turtle()
ristkylikVasak.color ('white')    #turtle alustab keskelt
ristkylikVasak.shape('square')    #pisike kastike väljaku keskel, sellest kuj välja ristkülik
ristkylikVasak.shapesize(stretch_len=1, stretch_wid=5) #ruudust sai ristkülik
ristkylikVasak.penup()            #ristküliku viimisega keskelt vasakule tekkiva joone varjamine
ristkylikVasak.goto(-450,0)       #viisime ristküliku väljaku keskelt vasakule

ristkylikParem = turtle.Turtle()
ristkylikParem.color ('white')
ristkylikParem.shape('square')
ristkylikParem.shapesize(stretch_len=1, stretch_wid=5)
ristkylikParem.penup()
ristkylikParem.goto(450,0)

FONT = ('Arial', 38)
score_vasak = 0
skooriKast = turtle.Turtle(visible=False) #skoorikasti juures olev nooleke muuta nähtamatuks
skooriKast.color ('white')
skooriKast.penup()
skooriKast.setposition(-200, 300) #skoorikasti asukoht x, y teljel
skooriKast.write(score_vasak, font=FONT)

score_parem = 0
skooriKast2 = turtle.Turtle(visible=False) #skoorikasti juures olev nooleke muuta nähtamatuks
skooriKast2.color ('white')
skooriKast2.penup()
skooriKast2.setposition(200, 300) #skoorikasti asukoht x, y teljel
skooriKast2.write(score_parem, font= FONT)

def liigu_yles_vasak():
    y = ristkylikVasak.ycor() + 10        #y-telg
    if y > 250:                 #seadistused, et ristkülik ei läheks väljaku piiridest välja
        y = 250            
    ristkylikVasak.sety(y)     #set y-telg, 

def liigu_yles_parem():
    y = ristkylikParem.ycor() + 10
    if y >250:
        y = 250
    ristkylikParem.sety(y)

def liigu_alla_vasak():
    y = ristkylikVasak.ycor() -10
    if y < -250:
        y = -250
    ristkylikVasak.sety(y)     

def liigu_alla_parem():
    y = ristkylikParem.ycor() -10
    if y < -250:
        y = -250
    ristkylikParem.sety(y)

pall = turtle.Turtle()
pall.shape('circle')
pall.speed (0)
pall.color('red')
pall.dx = 3                       #palli kiirus
pall.dy = -3
pall.penup()                      #kaotab palli liikumise joone

aken.listen()  #see meetod paneb erinevad liigutused tööle, st ristküliku liikumise
aken.onkeypress(liigu_yles_vasak, "w")  #nupuvajutus- üles- w
aken.onkeypress(liigu_alla_vasak, "s")
aken.onkeypress(liigu_yles_parem, "p")
aken.onkeypress(liigu_alla_parem, "l")

while True:
    aken.update()
    pall.setx(pall.xcor() + pall.dx)  #pall.xcor on hetke koordinaat
                                          #hetke koordinaadile lisame kiiruse
                                          #saadud tulemusest kujuneb uus koordin setx
    pall.sety(pall.ycor() + pall.dy) 

    if pall.ycor() >= 290:            #ülemine serv
        pall.dy = -pall.dy            #pall muudab suunda

    if pall.ycor() <= -290:           #alumine serv
        pall.dy = -pall.dy

    if pall.xcor() >= 490: 
        score_parem += 1         #kui pall möödub ristkülikust, siis saab vastane punkti
                   #kui pall jõuab parema ääreni, st ristkülikust mööda
        skooriKast2.clear()
        skooriKast2.write(score_parem, font= FONT)
        pall.goto(0, randint(-150, 150))    # siis läheb pall väljaku keskjoone juurde tagasi
         #selleks, et pall ei liiguks kogu aeg ühes suunas
        pall.dx = choice ([-4, -3, -2, 2, 3, 4])                
        pall.dy = choice ([-4, -3, -2, 2, 3, 4]) 
    
    if pall.xcor() <= -490:
        score_vasak += 1
        skooriKast.clear()
        skooriKast.write(score_vasak, font=FONT)
        pall.goto(0,randint(-150, 150)) 
        #selleks, et pall ei liiguks kogu aeg ühes suunas 
        pall.dx = choice ([-4, -3, -2, 2, 3, 4])        #selleks, et pall liiguks suvalises suunas            
        pall.dy = choice ([-4, -3, -2, 2, 3, 4]) 

#kontrollime, kas pall kattub ristkülikuga
#kattub siis, kui ta on ristküliku ülemise ja alumise serva vahel ja
#kui ta on kasvõi osaliselt püstiste külgede vahel 
    if pall.ycor ()>= ristkylikParem.ycor ()-50 and pall.ycor () <= ristkylikParem.ycor () +50 \
    and pall.xcor () >= ristkylikParem.xcor () -5 and pall.xcor () <=ristkylikParem.xcor () +5:
        pall.dx = -pall.dx  #muudan palli suunda

    if pall.ycor ()>= ristkylikVasak.ycor ()-50 and pall.ycor () <= ristkylikVasak.ycor () +50 \
    and pall.xcor () >= ristkylikVasak.xcor () -5 and pall.xcor () <=ristkylikVasak.xcor () +5:
        pall.dx = -pall.dx  #muudan palli suunda

aken.mainloop()                   #selleks, et konsooli aken ei sulguks kohe

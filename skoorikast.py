import turtle

def skoorikastid():
    global FONT
    global skooriKast
    global score_vasak
    global skooriKast2
    global score_parem
    
    FONT = ('Arial', 38)
    score_vasak = 0
    skooriKast = turtle.Turtle(visible=False) #skoorikasti juures olev nooleke muuta nähtamatuks
    skooriKast.color ('white')
    skooriKast.penup()
    skooriKast.setposition(-200, 300)        #skoorikasti asukoht x, y teljel
    skooriKast.write(score_vasak, font=FONT)

    score_parem = 0    
    skooriKast2 = turtle.Turtle(visible=False) #skoorikasti juures olev nooleke muuta nähtamatuks
    skooriKast2.color ('white')
    skooriKast2.penup()
    skooriKast2.setposition(200, 300) #skoorikasti asukoht x, y teljel
    skooriKast2.write(score_parem, font=FONT)
from random import randint

def koordinaadid(aken,pall,score_parem,skooriKast2,FONT,choice,score_vasak,skooriKast):

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

   
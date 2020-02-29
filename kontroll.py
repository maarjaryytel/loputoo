def kontroll(pall,ristkylikParem, ristkylikVasak):
#kontrollime, kas pall kattub ristkülikuga
#kattub siis, kui ta on ristküliku ülemise ja alumise serva vahel ja
#kui ta on kasvõi osaliselt püstiste külgede vahel 
    if pall.ycor ()>= ristkylikParem.ycor ()-50 and pall.ycor () <= ristkylikParem.ycor () +50 \
    and pall.xcor () >= ristkylikParem.xcor () -5 and pall.xcor () <=ristkylikParem.xcor () +5:
        pall.dx = -pall.dx  #muudan palli suunda

    if pall.ycor ()>= ristkylikVasak.ycor ()-50 and pall.ycor () <= ristkylikVasak.ycor () +50 \
    and pall.xcor () >= ristkylikVasak.xcor () -5 and pall.xcor () <=ristkylikVasak.xcor () +5:
        pall.dx = -pall.dx  #muudan palli suunda

        
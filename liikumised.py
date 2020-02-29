
def liigu_yles_vasak(ristkylikVasak):         
    y = ristkylikVasak.ycor() + 10        #y-telg
    if y > 250:                 #seadistused, et ristkülik ei läheks väljaku piiridest välja
        y = 250            
    ristkylikVasak.sety(y)     #set y-telg, 
    #return ristkylikVasak
    
def liigu_yles_parem(ristkylikParem):
    y = ristkylikParem.ycor() + 10
    if y > 250:
        y = 250
    ristkylikParem.sety(y)
    

def liigu_alla_vasak(ristkylikVasak):
    y = ristkylikVasak.ycor() -10
    if y < -250:
        y = -250
    ristkylikVasak.sety(y)     

def liigu_alla_parem(ristkylikParem):
    y = ristkylikParem.ycor() -10
    if y < -250:
        y = -250
    ristkylikParem.sety(y)



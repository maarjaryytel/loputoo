import turtle
#from turtle import * #annab selle rea peale 36 errorit
from random import choice, randint  
from valjak import *  
from ristkylik import *  
from skoorikast import *   
from liikumised import * 
from mangupall import * 
from nupuvajutused import * 
from koordinaadid import *  
from kontroll import *   

aken()
valjak()

ristkylik_vasak()
ristkylik_parem()

skoorikastid()

liigu_yles_vasak(ristkylikVasak)
liigu_yles_parem(ristkylikParem)
liigu_alla_vasak(ristkylikVasak)
liigu_alla_parem(ristkylikParem)

pall()

nupuvajutused(aken,liigu_yles_vasak,liigu_alla_vasak,liigu_yles_parem,liigu_alla_parem)

koordinaadid(aken,pall,score_parem,skooriKast2,FONT,choice,score_vasak,skooriKast)

kontroll(pall,ristkylikParem, ristkylikVasak)

               

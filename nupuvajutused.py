def nupuvajutused(aken,liigu_yles_vasak,liigu_alla_vasak,liigu_yles_parem,liigu_alla_parem):
    aken.listen()  #see meetod paneb erinevad liigutused tööle, st ristküliku liikumise
    aken.onkeypress(liigu_yles_vasak, "w")  #nupuvajutus- üles- w
    aken.onkeypress(liigu_alla_vasak, "s")
    aken.onkeypress(liigu_yles_parem, "p")
    aken.onkeypress(liigu_alla_parem, "l")
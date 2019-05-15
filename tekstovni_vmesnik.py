import model

lojtrice = '####################################\n'

def izpis_zmage(igra):
    tekst = lojtrice + 'Uganili ste geslo {0}\n'.format(igra.geslo) + lojtrice
    return tekst

def izpis_poraza(igra):
    tekst = lojtrice + 'Obešeni ste! Pravilno geslo je bilo {0}.\n'.format(igra.geslo) + lojtrice
    return tekst

def izpis_igre(igra):
    tekst = lojtrice + 'Zaenkrat ste uganili: {0}.\n'.format(igra.pravilni_del_gesla()) + 'Število preostalih poizkusov: {0}. \n'.format(model.STEVILO_DOVOLJENIH_NAPAK + 1 - igra.stevilo_napak()) + 'Napačni ugibi: {0}. \n'.format(igra.nepravilni_ugibi()) + lojtrice
    return tekst

def zahtevaj_vnos():
    return input('Ugibaj črko: ')

def pozeni_vmesnik():
    igra = model.nova_igra()

    while True:
        #Izpišemo stanje igre
        print(izpis_igre(igra))
        #zahtevamo vnos uporabnika
        poskus = zahtevaj_vnos()
        igra.ugibaj(poskus)
        if igra.poraz():
            print(izpis_poraza(igra))
            break
        elif igra.zmaga():
            print(izpis_zmage(igra))
            break
        else:
            pass
    return None

igra = model.nova_igra()
print(izpis_zmage(igra))
print(izpis_poraza(igra))
print(izpis_igre(igra))
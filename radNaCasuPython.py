brl = [30, 55, 16, 60, 68, 7, -23, 39, -69, -3, -65, -17, 41, 6]
brojpojavljivanja = 0
maks = brl[0]  # promenljivi maks dajemo vrednost prvog elementa u nizu
for i in brl:  # petlja pomoću koje prolazimo kroz svaki element niza
    if i > maks: # proveravamo da li je element niza veći od maks-a
        maks = i # ako element niza jeste veći od maks-a, promenljiva maks dobija vrednost tog elementa
        brojpojavljivanja += 1
print (" najveći broj u nizu je", maks) # ispisujemo vrednost promenljive maks, tj. najveći element niza
#1
print(brojpojavljivanja)

#2
prosek = 0
zbir = 0
brojelemenata = 0
for k in brl:
    zbir += k

for m in brl:
    if m in brl:
       brojelemenata += 1

prosek = zbir / brojelemenata
print(prosek)

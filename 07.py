# print("tere maailm")
# “jaanuar”,-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3
# Kuva mõõdetava kuu nimetus
# Kuva viimase mõõtmise tulemus
# Kuva ainult temperatuurid
# Leia kuu maksimaalne ja minimaalne temperatuur
# Leia kuu keskmine temperatuur
# Mitu korda esines -20 kraadi
# Eemalda element nr 5
# Lisa 5. elemendi kohale temperatuur, mis on sinu vanus
# Sorteeri temperatuurid nimekirjas kasvavas järjekorras

jtemp = ["jaanuar",-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3]

print(f"Mõõdetav temperatuur {jtemp[0]}")
print(f"Viimane mõõtmise tulemus {jtemp[-1]}kraadi")
maks = 0
mini = 100
summa = 0
kokku = 0
kordused = 0


for t in range(1,len(jtemp)):
    print(jtemp[t], end=" ")
    if jtemp[t]>maks:
        maks = jtemp [t]
    if jtemp[t]<mini:
        mini = jtemp[t]
        print()
    summa+=jtemp[t] 
    kokku+=1
    if jtemp[t]== -20:
        kordused+=1

jtemp.pop(5)
jtemp.insert(5,41)

print()
print(f"Maksimum temp on: {maks}")
print(f"Miinimum temp on: {mini}")
print(f"keskmine temp on: {summa/kokku:0.2f}")
print(f"Temp - 20 esineb: {kordused} korda")
print(jtemp)




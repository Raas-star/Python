import requests
import json



url = "https://metshein.com/kordamine/json/arved.json"  
response = requests.get(url)  
arved = response.json()["arved"]
if response.status_code==200:


    maksmata=0
    makstud=0
    makstud_kokku=0
    kogu_summa=0
    kokku_arveid=0


    for arve in arved:
        kogu_summa+= arve["summa"]
        kokku_arveid+=1

        if arve["makstud"]== True:
            makstud+=1
            makstud_kokku+= arve["summa"]
        else:
            maksmata+=1


    keskmine= kogu_summa/kokku_arveid
    print(f"Makstud arveid on: {makstud}")
    print(f"Maksmata arveid on: {maksmata}")
    print(f"Makstud arveid kokku: {makstud_kokku}")
    print(f"keskminen: {makstud}")

            
else:
    print(f"Viga!Ei suutnud andmeid laadida. Staatuskood: {response.status_code}") 





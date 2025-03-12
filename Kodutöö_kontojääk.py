
def pangakonto(algne_saldo, toiming, summa):
    if toiming == "deposiit":
        algne_saldo += summa
    elif toiming == "valjavote":
        algne_saldo -= summa
    return algne_saldo 


saldo = float(input("Sisesta algne saldo: "))  
toiming = input("Sisesta toiming (deposiit/valjavote): ") 
summa = float(input("Sisesta summa: "))


uus_saldo = pangakonto(saldo, toiming, summa)
print("Konto jääk:", uus_saldo) 


  
   

        

        


 
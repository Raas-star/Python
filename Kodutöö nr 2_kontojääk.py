

def pangakonto(algne_saldo, toiming, summa):
    if toiming == "deposiit": 
        algne_saldo += summa
    elif toiming == "valjavote":
        algne_saldo -= summa
    print("Konto jääk:", algne_saldo)
        
           
 
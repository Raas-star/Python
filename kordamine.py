#Ülesanne 

# fail = open("rebased.txt", encoding="UTF-8")

# vastuvõetud = []

# for rida in fail:
#     #print(rida, end="")
#     vastuvõetud.append(int(rida))

# fail.close()

# aasta = 9
# print(vastuvõetud[aasta-1])
# aasta = input("Lisa aasta 2011-2019: ")
# print(vastuvõetud[int(aasta[3])-1])
      
# fail = open("rebased.txt", encoding="UTF-8")

# vastuvõetud = []

# for rida in fail:
#     #print(rida, end="")
#     vastuvõetud.append(int(rida))

# fail.close()

# fail = open("konto.txt", encoding="UTF-8")
# for kirje in fail:
#     if float(kirje) > 0:
#      print(float(kirje), end="\n")

# fail.close()

musa = "edm.txt"
fail = open(musa, encoding="UTF-8")

nr = 1
for pala in fail:
    print(str(nr)+". "+pala, end="")
    nr+=1
  
print()  
valik = int(input("Vali lugu: "))
fail = open(musa, encoding="UTF-8")
mangin = 1
for pala in fail:
    if valik == mangin:
        print(pala, end="")
    mangin+=1

fail.close()


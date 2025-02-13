import os
from datetime import date

print(f"Tere{os.getlogin()}")
print(f"Sinu rada {os.getcwd()}")

kataloogidearv = 10
kp = str(date.today())

try:
    os.mkdir(kp)
    print(f"{kp} Kataloog loodud")
    for i in range(1,kataloogidearv):
        kaust = kp+"/"+str(i)
        os.makdeirs(kaust)

except:
    print("kataloog juba olemas")

#Kustutab kausta
if os.path.exsists(kp+"/"+str(kustuta)):
    os.rmdir(kp+"/"+str(kustuta))
    print(f"{kustuta} kataloog kustutatud")
else: 
    print(f"{kustuta}")

    
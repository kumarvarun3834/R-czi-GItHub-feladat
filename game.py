import sqlite3
import random
import hashlib


def véletlen():
    vél=random.Random()
    return vél.randrange (len(datas))

def rekord(list,x):
    return list[x]

def adat(list,x,y):
    return list[x][y]


base=sqlite3.connect("szavak.db")
t=base.cursor()
adatok=t.execute("Select szó,mondat1,mondat2,mondat3,mondat4 from szavmon")

datas=[list(adat) for adat in adatok]
szám=[]
szám.append(véletlen())
#***************************************************************************
pontok=0
def game(szám,pontok):
    élet=4
    if adat(datas,szám[0],0)==adat(datas,szám[0],0):
        print(adat(datas,szám[0],1))
        kiv=input("Ön melyik szóra gondol?: ")
        if kiv==adat(datas,szám[0],0):
            pontok+=1
            print("Gratulálok ez a helyes válasz! \nSzeretne új játékot kezdeni? Y/N")
            uj=input("")
            if uj.lower()=="y":
                véletlen()
                szám.clear()
                szám.append(véletlen())
                game(szám,pontok)
            else:
                print("Köszönjük a játékot!","Ennyi pontot gyűjtött:",pontok)
        else:
            print("Ez sajnos helytelen. Ennyi élete van:",élet-1,"Itt a következő mondat: ",adat(datas,szám[0],2))
            kiv=input("Az előző szó helytelen volt. Kérem a szót!: ")
            if kiv==adat(datas,szám[0],0):
                pontok+=1
                print("Gratulálok ez a helyes válasz! \nSzeretne új játékot kezdeni? Y/N")
                uj=input("")
                if uj.lower()=="y":
                    véletlen()
                    szám.clear()
                    szám.append(véletlen())
                    game(szám,pontok)
                else:
                    print("Köszönjük a játékot!","Ennyi pontot gyűjtött:",pontok)
            else:
                print("Ez sajnos helytelen. Ennyi élete van:",élet-2,"Itt a következő mondat:",adat(datas,szám[0],3))
                kiv=input("Az előző szó helytelen volt. Kérem a szót!: ")
                if kiv==adat(datas,szám[0],0):
                    pontok+=1
                    print("Gratulálok ez a helyes válasz! \nSzeretne új játékot kezdeni? Y/N")
                    uj=input("")
                    if uj.lower()=="y":
                        véletlen()
                        szám.clear()
                        szám.append(véletlen())
                        game(szám,pontok)
                    else:
                        print("Köszönjük a játékot!","Ennyi pontot gyűjtött:",pontok)
                else:
                    print("Ez sajnos helytelen. Ennyi élete van:",élet-3," Itt a következő mondat:",adat(datas,szám[0],4))
                    kiv=input("Az előző szó helytelen volt. Kérem a szót!: ")
                    if kiv==adat(datas,szám[0],0):
                        pontok+=1
                        print("Gratulálok ez a helyes válasz! \nSzeretne új játékot kezdeni? Y/N")
                        uj=input("")
                        if uj.lower()=="y":
                            véletlen()
                            szám.clear()
                            szám.append(véletlen())
                            game(szám,pontok)
                        else:
                            print("Köszönjük a játékot!","Ennyi pontot gyűjtött:",pontok)
                    else:
                        print("Ön sajnos vesztett! A szó nem más, mint",adat(datas,szám[0],0),"Ennyi pontot gyűjtött:",pontok,"\nSzeretne új játékot kezdeni? Y/N")
                        uj=input("")
                        if uj.lower()=="y":
                            véletlen()
                            szám.clear()
                            szám.append(véletlen())
                            game(szám,pontok)
                        else:
                            print("Köszönjük a játékot!","Ennyi pontot gyűjtött:",pontok)

#***************************************************************************
def regisztráció():
    email = input("Írja be az email címét: ")
    jelszó = input("Adjon meg egy jelszót: ")
    biztjelszó = input("Újra a jelszót: ")
    
    if biztjelszó == jelszó:
        enc = biztjelszó.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        
        with open("beléptetőadatok.txt", "a") as f:
            f.write(email + "|" + hash1 + "\n")
        print("Sikeresen regisztrált!")
    else:
        print("A jelszó nem egyezik!\n")

def bejelentkezés():
    email = input("Írja be az email címét: ")
    jelszó = input("Írja be a jelszavát: ")
    auth = jelszó.encode()
    auth_hash = hashlib.md5(auth).hexdigest()

    with open("beléptetőadatok.txt", "r") as f:
        adatok = f.readlines()

    for sor in adatok:
        tárolt_email, tárolt_jelszó = sor.strip().split("|")
        if email == tárolt_email and auth_hash == tárolt_jelszó:
            print("Sikeresen bejelentkezett!")
            game(szám,pontok)
            break
        else:
            print("Sikertelen bejelentkezés!\n")

while 1:
    print("********** Login System **********")
    print("1.Regisztráció")
    print("2.Bejelentkezés")
    print("3.Kilépés")
    
    választás = int(input("Válasszon a lehetőségek közül: "))
    
    if választás == 1:
        regisztráció()
    elif választás == 2:
        bejelentkezés()
    elif választás == 3:
        break
    else:
        print("Rossz válasz!")

#*******************************************************************************

##print(adat(datas,szám[0],0))#szó#
##print(adat(datas,szám[0],1))#mondat1#
##print(adat(datas,szám[0],2))#mondat2#
##print(adat(datas,szám[0],3))#mondat3#
##print(adat(datas,szám[0],4))#mondat4#

#********************************************************************************




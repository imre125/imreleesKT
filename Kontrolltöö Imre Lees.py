##
##'''Variant 1 '''
#### Esimene ülesanne
##def list_sum(n): #Defineerime sum_listi
##    n=sum(n)     #Summeerib 
##    return(n) #Tagastab tulemuse
####
#######JÄRGNEVAT KOODI POLE VAJA SEST SEE KÜSIB KASUTAJALT NUMBREID JA TAGASTAB LISTI
#######sisestus=str(input("sisesta numbrid listi: "))    #palume kasutajal sisestada numbrid listi
#######listi_pikkus=len(sisestus)    #Mõõdame ära listi pikkuse
######list=[]    #Kõigepealt on list tühi
#######for i in range(listi_pikkus): # Teeme sisestatud numbrist listi
#######   c=int(sisestus[i])
#######   list.append(c) 
#######   
#######print("Sisestatud numbrite summa on:", (list_sum(list)))   #Kutsume välja funktsiooni, mis summeerib listis olevad numbrid ja prindime tulemuse
####
##print(list_sum([1,5,8,3,6]))





####Teine ülesanne

def liblikas(tekst):
    words=tekst.split() #teeme kõigepealt stringi juppideks
    pikkus=len(words) #Mõõdame ära mitu sõna on
    list=[] #kõigepealt on list tühi
    for i in range (0,pikkus): #otsime sõnade hulgast neid sõnu, mis algavad a tähega
        if words[i].startswith("a"):
            words[i]= "liblikas" #Kui leiame a tähega algava sõna siis asendame sõna liblikaga 
            list.append(words[i]) #Lisame sõna listi
        else: list.append(words[i]) #Kui pole a tähega sõna siis lisame lihtsalt listi
    ühendatud_list=" ".join(list)
    return(ühendatud_list) #Tagastame listi


print(liblikas("Kui arno isaga koolimajja autoga"))

              
#muudetud


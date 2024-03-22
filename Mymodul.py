def töönumber():
    nimi=input("Mis su nimi on?: ")
    päev=input("Mis päevl sa sündisid?: ")
    kuu=input("Mis kuul sa sündisid?: ")
    aastal=input("Mis aastal sa sündisis: ")
    sünnipäev=(päev+ '.' +kuu+ '.' +aastal)
    summa_päev=0
    summa_kuu=0
    for i in range(len(päev)):
        summa_päev+=int(päev[i])
    for i in range(len(kuu)):
        summa_kuu+=int(kuu[i])
    numbrite_summa=summa_päev + summa_kuu 
    print("Päeva ja kuu summa: "+str(numbrite_summa))
    summa_aastal=0
    for i in range(len(aastal)):
        summa_aastal+=int(aastal[i])
    print("Aasta numbrite summa: "+str(summa_aastal))
    saadud_arv=numbrite_summa + summa_aastal 
    print(saadud_arv, "see on 1 töönumber!")
    summa_arv_2=0 
    for i in range(len(str(saadud_arv))):  
        summa_arv_2+=int(str(saadud_arv)[i]) 
    print(summa_arv_2, "see on 2 töönumber!")   
    saadud_arv_3=saadud_arv-2*int(päev[0]) 
    print(saadud_arv_3, "see on 3 töönumber!") 
    saadud_arv_4=0
    for i in range(len(str(saadud_arv_3))): 
        saadud_arv_4+=int(str(saadud_arv_3)[i]) 
    print(saadud_arv_4, "see on 4 töönumber!")
    date="".join(sünnipäev.split("."))
    print("Arvude esimene rida: "+str(date))
    date1=str(saadud_arv)+str(summa_arv_2)+str(saadud_arv_3)+str(saadud_arv_4)
    print("Teine ruut numbriga: "+str(date1)) 
    print("------------------------------------------------------")
    numbrid=[]
    nlist=''
    for digit in range(1,10):
        date_kogus=date.count(str(digit))+date1.count(str(digit))
        n=str(digit)*date_kogus
        if n=='': 
            n='  ...  '
        numbrid.append(n)
        if digit%3==0:
            print(f"|    {numbrid[0]}   |    {numbrid[1]}    |     {numbrid[2]}     | ")
            print("------------------------------------------------------")
            nlist+=",".join(numbrid)+","
            numbrid.clear()
    failname = "andmeid.txt"
    f = open(failname,'a',encoding="utf-8")
    f.write(f"\nNimi: {nimi}, Sünnipäev: {sünnipäev}, Numbrid:  {nlist} ")   
    print("Salvestatud failis")
    f.close() 

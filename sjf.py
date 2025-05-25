#SaberAzizi
#4021133092
#Algoritm Shortest Job First (SJF)

def main():
    # ورودی
    num = int(input("Enter the number of processes: "))

    time_vorood = []
    time_ejra = []
    index = []
    aya_takmilshd = [] 

    for i in range(num):
        print(f"\nVorood va Ejra baraye Process shomare[{i + 1}]")
        x = int(input("zaman vorood: "))
        time_vorood.append(x)
        y = int(input("zaman ejra: "))
        time_ejra.append(y)
        index.append(f"P{i + 1}")
    
    tedad_takmilshd = 0
    aya_takmilshd = [] 
    for i in range(num):
        aya_takmilshd.append(False)
    
    time = 0 
    gant = []

    # حلقه اصلی
    while tedad_takmilshd < num:
        index_amade_ejra = []
        for item in range(num): 
            if aya_takmilshd[item] == False and time_vorood[item] <= time:
                index_amade_ejra.append(item)
        
        if len(index_amade_ejra) == 0: 
            aya_baghimandeh_yaft = False 
            for item in range(num): 
                if aya_takmilshd[item] == False:
                    aya_baghimandeh_yaft = True
                    break 
            if aya_baghimandeh_yaft == False: 
                break 
            continue 

        tedad_amade = len(index_amade_ejra)
        if tedad_amade > 1: 
            for i in range(tedad_amade - 1):
                aya_jabeja_shod = False
                for j in range(0, tedad_amade - i - 1):
                    andis_aval = index_amade_ejra[j]
                    andis_dovom = index_amade_ejra[j + 1]
                    bayad_jabeja_shavad = False
                    if time_ejra[andis_aval] > time_ejra[andis_dovom]:
                        bayad_jabeja_shavad = True
                    elif time_ejra[andis_aval] == time_ejra[andis_dovom] and \
                         time_vorood[andis_aval] > time_vorood[andis_dovom]:
                        bayad_jabeja_shavad = True
    
                    if bayad_jabeja_shavad == True: 
                        movaghat = index_amade_ejra[j]
                        index_amade_ejra[j] = index_amade_ejra[j + 1]
                        index_amade_ejra[j + 1] = movaghat
                        aya_jabeja_shod = True
                
                if aya_jabeja_shod == False: 
                    break 
        
        if len(index_amade_ejra) == 0: 
            continue

        andis_process_entekhabi = index_amade_ejra[0]
        zaman_shoroo_process = time
        zaman_payan_entekhabi = time + time_ejra[andis_process_entekhabi]
        
        gant.append((index[andis_process_entekhabi], zaman_shoroo_process, zaman_payan_entekhabi))
        
        aya_takmilshd[andis_process_entekhabi] = True
        time = zaman_payan_entekhabi 
        tedad_takmilshd += 1 
        
    # خروجی
    print("\n--------------------------SJF-------------------------\n")

    if len(gant) > 0:
        tartib = [] 
        for item in gant: 
            tartib.append(item[0])
        print("tartib:", ", ".join(tartib))
         
        print("\nGant :")
        gant_process, currenttime, payan_proces = gant[0] 
        print(f"{gant_process} --- {currenttime} : {payan_proces}")
        
        for item in range(1, len(gant)): 
            gant_process, currenttime, payan_proces = gant[item] 
            print(f"{gant_process} --- {currenttime} : {payan_proces}")

if __name__ == "__main__":
    main()
#SaberAzizi
#4021133092
#Algoritm Round Robin 

def main():
    #ورودی ها
    num = int(input("Enter the number of processes: "))
    quantom = int(input("Enter Quantom zaman: "))

    time_vorood = [] 
    time_ejra = []  
    index = []

    for i in range(num):
        print(f"\nVorood va Ejra baraye Process shomare[{i+1}]")
        x = int(input("Zaman vorood: ")) 
        time_vorood.append(x)
        y = int(input("Zaman ejra: ")) 
        time_ejra.append(y)
        index.append(f"P{i+1}")

    baghimande = []
    for item in time_ejra:
        baghimande.append(item)
    anjamshd = [] 
    for item in range(num): 
        anjamshd.append(False)
    ezafeshode_yebar = []
    for item in range(num): 
        ezafeshode_yebar.append(False)
    
    time = 0   
    tedad_anjamshd = 0  
    saf_amade_ejra = []   
    gant = []   
    
    # حلقه اصلی
    while tedad_anjamshd < num:
        
        voroodijadid = []
        for item in range(num):
            if time_vorood[item] <= time:
                if anjamshd[item] == False: 
                    if ezafeshode_yebar[item] == False: 
                        if item not in saf_amade_ejra: 
                            voroodijadid.append(item)
        for item in voroodijadid:
            saf_amade_ejra.append(item)
            ezafeshode_yebar[item] = True
        if len(saf_amade_ejra) == 0: 
            if tedad_anjamshd < num: 
                time_voroodbadi = 0      
                voroodbadi_hast = False  
                for item in range(num):
                    if anjamshd[item] == False:
                        if ezafeshode_yebar[item] == False: 
                            if voroodbadi_hast == False: 
                                time_voroodbadi = time_vorood[item]
                                voroodbadi_hast = True
                            else: 
                                if time_vorood[item] < time_voroodbadi:
                                    time_voroodbadi = time_vorood[item]
                if voroodbadi_hast == True and time_voroodbadi > time: 
                    time = time_voroodbadi 
                else: 
                    time += 1
                continue 
            else:
                break 

        pid_feli = saf_amade_ejra.pop(0) 
        ejra_inbar = 0 
        
        if baghimande[pid_feli] > quantom:
            ejra_inbar = quantom
        else:
            ejra_inbar = baghimande[pid_feli]

        gant_shoroo = time 
        
        baghimande[pid_feli] = baghimande[pid_feli] - ejra_inbar
        time += ejra_inbar                     
        gant.append( (index[pid_feli], gant_shoroo, time) ) 

        if baghimande[pid_feli] == 0:
            anjamshd[pid_feli] = True
            tedad_anjamshd = tedad_anjamshd + 1
        
        tazevared_bad_az_ejra = [] 

        for item in range(num):
            if item == pid_feli: 
                continue
            if time_vorood[item] <= time:
                if anjamshd[item] == False:
                    if ezafeshode_yebar[item] == False:
                        if item not in saf_amade_ejra: 
                             tazevared_bad_az_ejra.append(item)
                             
        if anjamshd[pid_feli] == False: 
            saf_amade_ejra.append(pid_feli)

        for pid_jadid in tazevared_bad_az_ejra: 
            saf_amade_ejra.append(pid_jadid)
            ezafeshode_yebar[pid_jadid] = True 

    # خروجی
    print("\n--------------------------RR-------------------------\n")
    if len(gant) > 0:
        tartib = []
        for item in gant:
            tartib.append(item[0])
        print("tartib:", ", ".join(tartib))
        print("\nGant :") 
        if len(gant) > 0: 
            currenttime = gant[0][1]
            print(f"{gant[0][0]} --- {currenttime} : {gant[0][2]}")
            currenttime = gant[0][2]
            for item in range(1, len(gant)):
                gant_process = gant[item][0]
                payan_proces = gant[item][2]
                
                print(f"{gant_process} --- {currenttime} : {payan_proces}")
                currenttime = payan_proces


if __name__ == "__main__":
    main()
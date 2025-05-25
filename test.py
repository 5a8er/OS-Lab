#SaberAzizi
#4021133092
#Algoritm Shortest Remaining Time (SRT)

def main():
    # ورودی
    num = int(input("Enter the number of processes: "))

    time_vorood = []    
    time_ejra = []      
    index = []
    time_baghimandeh = []

    for i in range(num):
        print(f"\nVorood va Ejra baraye Process shomare[{i + 1}]")
        x = int(input("zaman vorood: ")) 
        time_vorood.append(x)
        y = int(input("zaman ejra: ")) 
        time_ejra.append(y)
        time_baghimandeh.append(y) 
        index.append(f"P{i + 1}")

    tedad_takmilshd = 0       
    aya_takmilshd = []
    for item in range(num): 
        aya_takmilshd.append(False)
    
    pid_ejra_feli = ""  
    time = 0 
    time_shoro = 0     
    gant = [] 
    
    # حلقه اصلی  
    while tedad_takmilshd < num:
        index_amade_ejra = [] 
        for item in range(num): 
            if aya_takmilshd[item] == False and time_vorood[item] <= time: 
                index_amade_ejra.append(item)

        if len(index_amade_ejra) == 0: 
            if pid_ejra_feli != "" and time_shoro != time: 
                gant.append((pid_ejra_feli,  time_shoro, time)) 
            
            pid_ejra_feli = "" 

            all_processes_completed = True
            for i_check in range(num):
                if not aya_takmilshd[i_check]:
                    all_processes_completed = False
                    break
            
            if all_processes_completed: 
                break 
            continue

        index_process_entekhabi = -1 
        kamtarin_baghi_srt = -1 
        aya_baghi_yaft = False 
        
        vorood_baraye_tasavi_srt = -1 
        index_baraye_tasavi_kamel_srt = -1 

        if len(index_amade_ejra) > 0: 
            for idx_amade in index_amade_ejra: 
                bayad_entekhab_shavad = False 
                
                if aya_baghi_yaft == False: 
                    bayad_entekhab_shavad = True
                    aya_baghi_yaft = True  
                elif time_baghimandeh[idx_amade] < kamtarin_baghi_srt: 
                    bayad_entekhab_shavad = True
                elif time_baghimandeh[idx_amade] == kamtarin_baghi_srt: 
                    if time_vorood[idx_amade] < vorood_baraye_tasavi_srt: 
                        bayad_entekhab_shavad = True
                    elif time_vorood[idx_amade] == vorood_baraye_tasavi_srt:
                        if index_baraye_tasavi_kamel_srt == -1 or idx_amade < index_baraye_tasavi_kamel_srt: 
                             bayad_entekhab_shavad = True
                
                if bayad_entekhab_shavad == True:
                    kamtarin_baghi_srt = time_baghimandeh[idx_amade]
                    vorood_baraye_tasavi_srt = time_vorood[idx_amade] 
                    index_baraye_tasavi_kamel_srt = idx_amade
                    index_process_entekhabi = idx_amade 
        
        if index_process_entekhabi == -1 and len(index_amade_ejra) > 0 :
             index_process_entekhabi = index_amade_ejra[0] 

        pid_entekhabi_nam = index[index_process_entekhabi] 

        if pid_ejra_feli != pid_entekhabi_nam:
            if pid_ejra_feli != "" and  time_shoro != time: 
                gant.append((pid_ejra_feli,  time_shoro, time)) 
            time_shoro = time 
            pid_ejra_feli = pid_entekhabi_nam
        
        time_baghimandeh[index_process_entekhabi] = time_baghimandeh[index_process_entekhabi] - 1
        time = time + 1 

        if time_baghimandeh[index_process_entekhabi] == 0: 
            aya_takmilshd[index_process_entekhabi] = True 
            tedad_takmilshd = tedad_takmilshd + 1 
            gant.append((pid_ejra_feli,  time_shoro, time)) 
            pid_ejra_feli = "" 

    if pid_ejra_feli != "" and  time_shoro != time: 
        gant.append((pid_ejra_feli,  time_shoro, time)) 

    # خروجی
    print("\n--------------------------SRT-------------------------\n") 
    if len(gant) > 0:
        tartib = [] 
        for item in gant: 
            tartib.append(item[0])
        print("tartib:", ", ".join(tartib))
        print("\nGant :")
        gant_process, currenttime, payan_process = gant[0] 
        print(f"{gant_process} --- {currenttime} : {payan_process}")
        for item in range(1, len(gant)): 
            gant_process, currenttime, payan_process = gant[item] 
            print(f"{gant_process} --- {currenttime} : {payan_process}")
        
if __name__ == "__main__":
    main()
def main():
    try:
        num = int(input("How many process you want to enter : "))
        if num <= 0:
            raise ValueError("Number of processes must be positive")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    input_list = []
    p_time = []
    index = []

    for i in range(num):
        print(f"Process {i + 1}:")
        arrival_time = int(input("  Enter arrival time: "))
        input_list.append(arrival_time)
        
        processing_time = int(input("  Enter processing time: "))
        p_time.append(processing_time)

        index.append(f"P{i + 1}")

    # Sort processes by arrival time
    processes = list(zip(input_list, p_time, index))
    processes.sort(key=lambda x: x[0])  # Sort by arrival time
    input_list, p_time, index = zip(*processes)
    input_list, p_time, index = list(input_list), list(p_time), list(index)

    print("\n---------------------FCFS-------------------------\n")
    
    # Show the actual execution order after sorting
    print("Final Process order:", ", ".join(index))
 print("\nGantt Chart:")
 currenttime = max(input_list[0], 0)  # Start at arrival time or 0
 print(f"{index[0]} --- {currenttime} : {currenttime + p_time[0]}")
 currenttime += p_time[0]

 for i in range(1, len(index)):
     # Check if there's idle time before next process
     if input_list[i] > currenttime:
         print(f"IDLE --- {currenttime} : {input_list[i]}")
         currenttime = input_list[i]
     print(f"{index[i]} --- {currenttime} : {currenttime + p_time[i]}")
     currenttime += p_time[i]
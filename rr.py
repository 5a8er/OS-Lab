# Algorithm: Round Robin (RR)

def main():
    # Input validation
    try:
        num = int(input("Enter the number of processes: "))
        if num <= 0:
            raise ValueError("Number of processes must be positive")
        quantum = int(input("Enter quantum time: "))
        if quantum <= 0:
            raise ValueError("Quantum time must be positive")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    arrival_time = []
    burst_time = []
    process_ids = []

    for i in range(num):
        print(f"\nArrival and Burst time for Process [{i+1}]")
        x = int(input("Arrival time: "))
        arrival_time.append(x)
        y = int(input("Burst time: "))
        burst_time.append(y)
        process_ids.append(f"P{i+1}")

    remaining_time = burst_time.copy()  # Remaining execution time
    completed = [False] * num          # Completion status
    added_to_queue = [False] * num     # Queue membership tracking
    
    current_time = 0
    completed_count = 0
    ready_queue = []
    gantt_chart = []
    
    # Main scheduling loop
    while completed_count < num:
        # Add newly arrived processes to ready queue
        newly_arrived = []
        for i in range(num):
            if (arrival_time[i] <= current_time and 
                not completed[i] and 
                not added_to_queue[i] and 
                i not in ready_queue):
                newly_arrived.append(i)
                
        for process in newly_arrived:
            ready_queue.append(process)
            added_to_queue[process] = True
            
        if len(ready_queue) == 0:
            if completed_count < num:
                next_arrival_time = float('inf')
                has_next_arrival = False
                for i in range(num):
                    if not completed[i] and not added_to_queue[i]:
                        if not has_next_arrival:
                            next_arrival_time = arrival_time[i]
                            has_next_arrival = True
                        else:
                            next_arrival_time = min(next_arrival_time, arrival_time[i])
                if has_next_arrival and next_arrival_time > current_time:
                    current_time = next_arrival_time
                else:
                    current_time += 1
                continue
            else:
                break

        current_process = ready_queue.pop(0)
        execution_time = min(quantum, remaining_time[current_process])
        
        gantt_start = current_time
        current_time += execution_time
        remaining_time[current_process] -= execution_time
        gantt_chart.append((process_ids[current_process], gantt_start, current_time))

        if remaining_time[current_process] == 0:
            completed[current_process] = True
            completed_count += 1
        
        new_arrivals = []
        for i in range(num):
            if i == current_process:
                continue
            if (arrival_time[i] <= current_time and 
                not completed[i] and 
                not added_to_queue[i] and 
                i not in ready_queue):
                new_arrivals.append(i)
                
        if not completed[current_process]:
            ready_queue.append(current_process)

        for new_process in new_arrivals:
            ready_queue.append(new_process)
            added_to_queue[new_process] = True

    # Output
    print("\n--------------------------RR-------------------------\n")
    if len(gantt_chart) > 0:
        process_order = []
        for entry in gantt_chart:
            process_order.append(entry[0])
        print("Final Process order:", ", ".join(process_order))
        print("\nGantt Chart:") 
        if len(gantt_chart) > 0:
            current_time = gantt_chart[0][1]
            print(f"{gantt_chart[0][0]} --- {current_time} : {gantt_chart[0][2]}")
            current_time = gantt_chart[0][2]
            for i in range(1, len(gantt_chart)):
                process = gantt_chart[i][0]
                end_time = gantt_chart[i][2]
                print(f"{process} --- {current_time} : {end_time}")
                current_time = end_time

if __name__ == "__main__":
    main()
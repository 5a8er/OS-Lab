# Algorithm: Shortest Job First (SJF)

def main():
    # Input
    num = int(input("Enter the number of processes: "))

    arrival_times = []
    execution_times = []
    process_ids = []
    is_completed = [False] * num
    completed_count = 0

    # Get process details from user
    for i in range(num):
        print(f"\nInput for Process {i + 1}:")
        try:
            arrival_time = int(input("Arrival time: "))
            execution_time = int(input("Execution time: "))
            if arrival_time < 0 or execution_time <= 0:
                raise ValueError("Invalid time values")
            arrival_times.append(arrival_time)
            execution_times.append(execution_time)
            process_ids.append(f"P{i + 1}")
        except ValueError as e:
            print(f"Error: {e}")
            return
    current_time = 0
    gantt_chart = []

    # Main scheduling loop
    while completed_count < num:
        ready_processes = []
        for i in range(num):
            if not is_completed[i] and arrival_times[i] <= current_time:
                ready_processes.append(i)

        if not ready_processes:
            # Check if there are any remaining processes
            remaining_processes = False
            for i in range(num):
                if not is_completed[i]:
                    remaining_processes = True
                    break
            if not remaining_processes:
                break
            current_time += 1
            continue

        # Sort ready processes by execution time, then by arrival time as tiebreaker
        ready_processes.sort(key=lambda i: (execution_times[i], arrival_times[i]))

        selected_process = ready_processes[0]
        start_time = current_time
        end_time = current_time + execution_times[selected_process]

        gantt_chart.append((process_ids[selected_process], start_time, end_time))

        is_completed[selected_process] = True
        current_time = end_time
        completed_count += 1

    # Output results
    print("\n--------------------------SJF-------------------------\n")

    if gantt_chart:
        process_order = [entry[0] for entry in gantt_chart]
        print("Final Process order:", ", ".join(process_order))

        print("\nGantt Chart:")
        for process_id, start, end in gantt_chart:
            print(f"{process_id} --- {start} : {end}")

if __name__ == "__main__":
    main()
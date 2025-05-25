# Algorithm: Shortest Remaining Time (SRT)

def main():
    """Main function to get user input and run the SRT scheduler."""
    try:
        num_processes = int(input("Enter the number of processes: "))
        if num_processes <= 0:
            raise ValueError("Number of processes must be positive")

        arrival_times = []
        burst_times = []

        for i in range(num_processes):
            print(f"\nProcess {i + 1}:")
            arrival_time = int(input("  Enter arrival time: "))
            if arrival_time < 0:
                raise ValueError("Arrival time cannot be negative")
            arrival_times.append(arrival_time)
            
            burst_time = int(input("  Enter burst time: "))
            if burst_time <= 0:
                raise ValueError("Burst time must be positive")
            burst_times.append(burst_time)

        gantt_chart, process_order = run_srt_scheduler(num_processes, arrival_times, burst_times)
        print_schedule(gantt_chart, process_order)

    except ValueError as e:
        print(f"Invalid input: {e}")


def run_srt_scheduler(num_processes, arrival_times, burst_times):
    """
    Run the SRT (Shortest Remaining Time) scheduling algorithm.
    
    Args:
        num_processes (int): Number of processes
        arrival_times (list): List of process arrival times
        burst_times (list): List of process burst times
        
    Returns:
        tuple: A tuple containing (gantt_chart, process_order)
    """
    # Create copies to avoid modifying original lists
    remaining_times = burst_times.copy()
    completed = [False] * num_processes
    completed_count = 0
    process_ids = [f"P{i+1}" for i in range(num_processes)]
    
    current_process = ""
    current_time = min(arrival_times)  # Start at earliest arrival
    start_time = current_time
    gantt_chart = []
    
    while completed_count < num_processes:
        # Find ready processes
        ready_processes = [
            i for i in range(num_processes) 
            if not completed[i] and arrival_times[i] <= current_time
        ]

        if not ready_processes:
            # No process is ready, advance time to next arrival
            if current_process:
                gantt_chart.append((current_process, start_time, current_time))
            
            current_process = ""
            next_arrival = float('inf')
            for i in range(num_processes):
                if not completed[i] and arrival_times[i] > current_time:
                    next_arrival = min(next_arrival, arrival_times[i])
            
            if next_arrival == float('inf'):
                break
            current_time = next_arrival
            continue

        # Find process with shortest remaining time
        selected_process = -1
        shortest_time = float('inf')
        for proc in ready_processes:
            if remaining_times[proc] < shortest_time:
                shortest_time = remaining_times[proc]
                selected_process = proc
            elif remaining_times[proc] == shortest_time and arrival_times[proc] < arrival_times[selected_process]:
                # Break tie using arrival time
                selected_process = proc

        # Process context switch
        if current_process != process_ids[selected_process]:
            if current_process:
                gantt_chart.append((current_process, start_time, current_time))
            current_process = process_ids[selected_process]
            start_time = current_time

        # Execute for 1 time unit
        remaining_times[selected_process] -= 1
        current_time += 1

        # Check if process completed
        if remaining_times[selected_process] == 0:
            completed[selected_process] = True
            completed_count += 1
            gantt_chart.append((current_process, start_time, current_time))
            current_process = ""

    # Add final process if any
    if current_process and start_time != current_time:
        gantt_chart.append((current_process, start_time, current_time))

    # Generate process order from gantt chart
    process_order = [entry[0] for entry in gantt_chart]
    
    return gantt_chart, process_order


def print_schedule(gantt_chart, process_order):
    """
    Print the scheduling results.
    
    Args:
        gantt_chart (list): List of tuples (process_id, start_time, end_time)
        process_order (list): List of process IDs in order of execution
    """
    print("\n--------------------------SRT-------------------------\n")
    
    print("Final Process order:", ", ".join(process_order))
    
    print("\nGantt Chart:")
    for process, start, end in gantt_chart:
        print(f"{process} --- {start} : {end}")


if __name__ == "__main__":
    main()

import importlib

def menu():
    while True:
        print("Select the scheduling algorithm to run:")
        print("1. FCFS (First-Come, First-Served)")
        print("2. RR (Round Robin)")
        print("3. SJF (Shortest Job First)")
        print("4. SRT (Shortest Remaining Time)")
        print("5. Exit")

        choice = input("Enter the number of your choice: ").strip()

        match choice:
            case "1":
                run_algorithm("fcfs")
                break
            case "2":
                run_algorithm("rr")
                break
            case "3":
                run_algorithm("sjf")
                break
            case "4":
                run_srt()
                break
            case "5":
                print("Exiting program.")
                return
            case _:
                print("Invalid choice. Please try again.\n")

def run_algorithm(module_name):
    try:
        # Dynamically import the selected algorithm module using importlib
        module = importlib.import_module(module_name)
        print(f"Running {module_name.upper()} scheduling algorithm...")
        
        # Assuming each algorithm file has a `main` function, we call it
        if hasattr(module, "main"):
            module.main()  # Execute the main function of the algorithm
        else:
            print(f"{module_name.upper()} does not have a main function.")
    
    except ModuleNotFoundError:
        print(f"{module_name.upper()} module not found.")
    except ValueError as e:
        print(f"Error executing {module_name.upper()}: {e}")

def run_srt():
    from srt import run_srt_scheduler, print_schedule
    try:
        # Get input from user
        num = int(input("Enter the number of processes: "))
        if num <= 0:
            raise ValueError("Number of processes must be positive")
        
        arrival_times = []
        burst_times = []
 
        for i in range(num):
            print(f"\nArrival and Burst time for Process [{i + 1}]")
            arrival_time = int(input("Arrival time: "))
            if arrival_time < 0:
                raise ValueError("Arrival time cannot be negative")
            arrival_times.append(arrival_time)
            
            burst_time = int(input("Burst time: "))
            if burst_time <= 0:
                raise ValueError("Burst time must be positive")
            burst_times.append(burst_time)

        # Run the SRT scheduler
        gantt_chart, process_order = run_srt_scheduler(num, arrival_times, burst_times)
        print_schedule(gantt_chart, process_order)

    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    menu()

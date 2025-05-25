import importlib

def menu():
    print("Select the scheduling algorithm to run:")
    print("1. FCFS (First-Come, First-Served)")
    print("2. RR (Round Robin)")
    print("3. SJF (Shortest Job First)")
    print("4. SRT (Shortest Remaining Time)")
    print("5. Exit")

    choice = input("Enter the number of your choice: ")

    match choice:
        case "1":
            run_algorithm("fcfs")
        case "2":
            run_algorithm("rr")
        case "3":
            run_algorithm("sjf")
        case "4":
            run_algorithm("srt")
        case "5":
            print("Exiting program.")
            exit()
        case _:
            print("Invalid choice. Please try again.")
            menu()

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
    except Exception as e:
        print(f"Error executing {module_name.upper()}: {e}")

if __name__ == "__main__":
    menu()

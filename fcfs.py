def main():
    num = int(input("How many process you want to enter : "))

    input_list = []
    p_time = []
    index = []

    for i in range(num):
        print(f"Enter Process Number : {i + 1}")
        in_process = int(input())
        input_list.append(in_process)

        out_process = int(input())
        p_time.append(out_process)

        index.append(f"P{i + 1}")

    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if input_list[i] > input_list[j]:
                input_list[i], input_list[j] = input_list[j], input_list[i]
                p_time[i], p_time[j] = p_time[j], p_time[i]
                index[i], index[j] = index[j], index[i]

    print("\n---------------------------------------------------\n")
    currenttime = input_list[0] + p_time[0]
    print(f"{index[0]} --- {input_list[0]} : {currenttime}")

    for i in range(1, len(index)):
        print(f"{index[i]} --- {currenttime} : {currenttime + p_time[i]}")
        currenttime += p_time[i]

if __name__ == "__main__":
    main()

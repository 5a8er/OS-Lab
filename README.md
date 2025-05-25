# Operating System Scheduling Algorithms

This project implements various CPU scheduling algorithms in Python to demonstrate how different scheduling strategies work in operating systems.

## Overview

This project includes implementations of four fundamental CPU scheduling algorithms:

1. **First-Come, First-Served (FCFS)**
   - Non-preemptive scheduling algorithm
   - Processes are executed in the order they arrive
   - Simple to implement but may lead to the convoy effect
   - Implementation: `fcfs.py`

2. **Round Robin (RR)**
   - Preemptive scheduling algorithm
   - Each process gets a fixed time quantum
   - Provides fair CPU sharing and good response time
   - Implementation: `rr.py`

3. **Shortest Job First (SJF)**
   - Non-preemptive scheduling algorithm
   - Selects the process with the shortest burst time
   - Optimal average waiting time but may lead to starvation
   - Implementation: `sjf.py`

4. **Shortest Remaining Time (SRT)**
   - Preemptive version of SJF
   - Switches to shorter processes when they arrive
   - Optimal average response time but may lead to starvation
   - Implementation: `srt.py`

## How to Run

1. Make sure you have Python 3.x installed
2. Run the main program:
   ```bash
   python OS-algorthms.py
   ```
3. Select the scheduling algorithm you want to test
4. Follow the prompts to input:
   - Number of processes
   - Arrival times
   - Burst/Processing times
   - Time quantum (for Round Robin only)

## File Structure

- `OS-algorthms.py`: Main program that lets you choose which algorithm to run
- `fcfs.py`: First-Come, First-Served implementation
- `rr.py`: Round Robin implementation
- `sjf.py`: Shortest Job First implementation
- `srt.py`: Shortest Remaining Time implementation
- `OS-lab-reports/`: Contains detailed reports and documentation

## Output Format

Each algorithm displays:
1. Process execution order
2. Gantt chart showing:
   - Process ID
   - Start time
   - End time

Example output:
```
--------------------------ALGORITHM-------------------------

Process order: P1, P2, P3, P4

Gantt Chart:
P1 --- 0 : 3
P2 --- 3 : 7
P3 --- 7 : 12
P4 --- 12 : 15
```

## Algorithm Characteristics

### FCFS (First-Come, First-Served)
- Simple and fair for equal-length processes
- May cause long average waiting times
- No process prioritization

### Round Robin (RR)
- Fair CPU sharing
- Better response time
- Higher context switching overhead
- Time quantum affects performance

### Shortest Job First (SJF)
- Optimal average waiting time
- Requires knowing/estimating burst times
- May cause starvation of longer processes

### Shortest Remaining Time (SRT)
- Preemptive version of SJF
- Optimal average response time
- Higher context switching overhead
- May cause starvation of longer processes



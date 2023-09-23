import queue

# Define the process data
processes = [
    {"name": "P1", "arrival_time": 0, "burst_time": 24, "priority": 3},
    {"name": "P2", "arrival_time": 4, "burst_time": 3, "priority": 1},
    {"name": "P3", "arrival_time": 5, "burst_time": 3, "priority": 4},
    {"name": "P4", "arrival_time": 6, "burst_time": 12, "priority": 2},
]

# Define the time quantum for RR scheduling
time_quantum = 4

# Initialize variables for each scheduling algorithm
fcfs_queue = queue.Queue()
sjf_queue = queue.PriorityQueue()
ps_queue = queue.PriorityQueue()
rr_queue = queue.Queue()

# Populate queues with processes
for process in processes:
    fcfs_queue.put(process.copy())
    sjf_queue.put((process["burst_time"], process["name"], process.copy()))
    ps_queue.put((process["priority"], process["name"], process.copy()))
    rr_queue.put(process.copy())

# Initialize variables to store waiting time and turnaround time
waiting_time_fcfs = {}
waiting_time_sjf = {}
waiting_time_ps = {}
waiting_time_rr = {}

turnaround_time_fcfs = {}
turnaround_time_sjf = {}
turnaround_time_ps = {}
turnaround_time_rr = {}

# FCFS Scheduling
current_time_fcfs = 0
while not fcfs_queue.empty():
    process = fcfs_queue.get()
    current_time_fcfs = max(current_time_fcfs, process["arrival_time"])
    waiting_time_fcfs[process["name"]] = current_time_fcfs - process["arrival_time"]
    current_time_fcfs += process["burst_time"]
    turnaround_time_fcfs[process["name"]] = current_time_fcfs - process["arrival_time"]

# SJF Scheduling
current_time_sjf = 0
while not sjf_queue.empty():
    burst_time, name, process = sjf_queue.get()
    current_time_sjf = max(current_time_sjf, process["arrival_time"])
    waiting_time_sjf[name] = current_time_sjf - process["arrival_time"]
    current_time_sjf += process["burst_time"]
    turnaround_time_sjf[name] = current_time_sjf - process["arrival_time"]

# PS Scheduling
current_time_ps = 0
while not ps_queue.empty():
    priority, name, process = ps_queue.get()
    current_time_ps = max(current_time_ps, process["arrival_time"])
    waiting_time_ps[name] = current_time_ps - process["arrival_time"]
    current_time_ps += process["burst_time"]
    turnaround_time_ps[name] = current_time_ps - process["arrival_time"]

# RR Scheduling
current_time_rr = 0
while not rr_queue.empty():
    process = rr_queue.get()
    current_time_rr = max(current_time_rr, process["arrival_time"])
    if process["burst_time"] <= time_quantum:
        waiting_time_rr[process["name"]] = current_time_rr - process["arrival_time"]
        current_time_rr += process["burst_time"]
        turnaround_time_rr[process["name"]] = current_time_rr - process["arrival_time"]
    else:
        waiting_time_rr[process["name"]] = current_time_rr - process["arrival_time"]
        current_time_rr += time_quantum
        process["burst_time"] -= time_quantum
        rr_queue.put(process.copy())

# Calculate average waiting time and average turnaround time for each algorithm
avg_waiting_time_fcfs = sum(waiting_time_fcfs.values()) / len(processes)
avg_turnaround_time_fcfs = sum(turnaround_time_fcfs.values()) / len(processes)

avg_waiting_time_sjf = sum(waiting_time_sjf.values()) / len(processes)
avg_turnaround_time_sjf = sum(turnaround_time_sjf.values()) / len(processes)

avg_waiting_time_ps = sum(waiting_time_ps.values()) / len(processes)
avg_turnaround_time_ps = sum(turnaround_time_ps.values()) / len(processes)

avg_waiting_time_rr = sum(waiting_time_rr.values()) / len(processes)
avg_turnaround_time_rr = sum(turnaround_time_rr.values()) / len(processes)

# Print results
print("FCFS Scheduling:")
print("Average Waiting Time:", avg_waiting_time_fcfs)
print("Average Turnaround Time:", avg_turnaround_time_fcfs)
print()

print("SJF Scheduling:")
print("Average Waiting Time:", avg_waiting_time_sjf)
print("Average Turnaround Time:", avg_turnaround_time_sjf)
print()

print("Priority Scheduling:")
print("Average Waiting Time:", avg_waiting_time_ps)
print("Average Turnaround Time:", avg_turnaround_time_ps)
print()

print("Round Robin (RR) Scheduling:")
print("Average Waiting Time:", avg_waiting_time_rr)
print("Average Turnaround Time:", avg_turnaround_time_rr)

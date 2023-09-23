import queue

# Define patient data
patients = [
    {"name": "A", "arrival_time": 0, "treatment_time": 30, "urgency": 3},
    {"name": "B", "arrival_time": 10, "treatment_time": 20, "urgency": 5},
    {"name": "C", "arrival_time": 15, "treatment_time": 40, "urgency": 2},
    {"name": "D", "arrival_time": 20, "treatment_time": 15, "urgency": 4},
]

# Initialize variables
fcfs_queue = queue.Queue()
sjf_queue = queue.PriorityQueue()
ps_queue = queue.PriorityQueue()
rr_queue = queue.Queue()

# Populate queues with patients
for patient in patients:
    fcfs_queue.put(patient.copy())
    sjf_queue.put((patient["treatment_time"], patient.copy()))
    ps_queue.put((-patient["urgency"], patient.copy()))
    rr_queue.put(patient.copy())

# Initialize variables to store scheduling results
fcfs_order = []
sjf_order = []
ps_order = []
rr_order = []

# FCFS Scheduling
current_time_fcfs = 0
while not fcfs_queue.empty():
    patient = fcfs_queue.get()
    current_time_fcfs = max(current_time_fcfs, patient["arrival_time"])
    fcfs_order.append(patient["name"])
    current_time_fcfs += patient["treatment_time"]

# SJF Scheduling
current_time_sjf = 0
while not sjf_queue.empty():
    treatment_time, patient = sjf_queue.get()
    current_time_sjf = max(current_time_sjf, patient["arrival_time"])
    sjf_order.append(patient["name"])
    current_time_sjf += patient["treatment_time"]

# PS Scheduling
current_time_ps = 0
while not ps_queue.empty():
    urgency, patient = ps_queue.get()
    current_time_ps = max(current_time_ps, patient["arrival_time"])
    ps_order.append(patient["name"])
    current_time_ps += patient["treatment_time"]

# RR Scheduling (with a time quantum of 15 minutes)
time_quantum = 15
rr_order = []
current_time_rr = 0
while rr_queue.qsize() > 0:
    patient = rr_queue.get()
    current_time_rr = max(current_time_rr, patient["arrival_time"])
    rr_order.append(patient["name"])
    if patient["treatment_time"] <= time_quantum:
        current_time_rr += patient["treatment_time"]
    else:
        current_time_rr += time_quantum
        patient["treatment_time"] -= time_quantum
        rr_queue.put(patient.copy())

# Calculate average waiting time and average turnaround time for each algorithm
def calculate_waiting_turnaround_time(order, patients):
    waiting_times = {}
    turnaround_times = {}
    current_time = 0
    for name in order:
        patient = next(p for p in patients if p["name"] == name)
        current_time = max(current_time, patient["arrival_time"])
        waiting_times[name] = max(0, current_time - patient["arrival_time"])
        current_time += patient["treatment_time"]
        turnaround_times[name] = current_time - patient["arrival_time"]
    return waiting_times, turnaround_times

fcfs_waiting, fcfs_turnaround = calculate_waiting_turnaround_time(fcfs_order, patients)
sjf_waiting, sjf_turnaround = calculate_waiting_turnaround_time(sjf_order, patients)
ps_waiting, ps_turnaround = calculate_waiting_turnaround_time(ps_order, patients)
rr_waiting, rr_turnaround = calculate_waiting_turnaround_time(rr_order, patients)

# Calculate average waiting time and average turnaround time
def calculate_average(values):
    return sum(values.values()) / len(values)

avg_waiting_fcfs = calculate_average(fcfs_waiting)
avg_turnaround_fcfs = calculate_average(fcfs_turnaround)

avg_waiting_sjf = calculate_average(sjf_waiting)
avg_turnaround_sjf = calculate_average(sjf_turnaround)

avg_waiting_ps = calculate_average(ps_waiting)
avg_turnaround_ps = calculate_average(ps_turnaround)

avg_waiting_rr = calculate_average(rr_waiting)
avg_turnaround_rr = calculate_average(rr_turnaround)

# Print scheduling results
print("FCFS Order:", fcfs_order)
print("Average Waiting Time (FCFS):", avg_waiting_fcfs)
print("Average Turnaround Time (FCFS):", avg_turnaround_fcfs)
print()

print("SJF Order:", sjf_order)
print("Average Waiting Time (SJF):", avg_waiting_sjf)
print("Average Turnaround Time (SJF):", avg_turnaround_sjf)
print()

print("Priority Scheduling Order:", ps_order)
print("Average Waiting Time (PS):", avg_waiting_ps)
print("Average Turnaround Time (PS):", avg_turnaround_ps)
print()

print("Round Robin (RR) Order:", rr_order)
print("Average Waiting Time (RR):", avg_waiting_rr)
print("Average Turnaround Time (RR):", avg_turnaround_rr)

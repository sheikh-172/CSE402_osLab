class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.rt = bt
        self.ct = self.tat = self.wt = 0

n = int(input("enter number of process: "))
procs = []
#input
for i in range(n):
    pid = f"p{i+1}"
    at = int(input(f"enter AT for {pid}: "))
    bt = int(input(f"enter BT for {pid}: "))
    procs.append(Process(pid, at, bt))

#round robin
time_quantum = 5
time = 0
done = 0
queue = []


#sort procs AT
procs.sort(key=lambda p: p.at)
i = 0

while done < n:

#add arrive procss to queue
    while i < n and procs[i].at <= time:
        queue.append(procs[i])
        i += 1

    #if queue is empt, cpu idle
    if not queue:
        if i < n: # Check if there are still processes to arrive
            time = procs[i].at
        continue

    curr = queue.pop(0)
#execute for 5
    exec_time = min(time_quantum, curr.rt)
    curr.rt -= exec_time
    time += exec_time
#add new arive procs
    while i < n and procs[i].at <= time:
        queue.append(procs[i])
        i += 1
#procs cmplt
    if curr.rt == 0:
        curr.ct = time
        curr.tat = curr.ct -curr.at
        curr.wt = curr.tat - curr.bt
        done += 1 # Corrected operator
    else:
        queue.append(curr)




#output
print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for p in sorted(procs, key=lambda x: x.pid):
    print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")


# average
avg_tat = sum(p.tat for p in procs) / n
avg_wt = sum(p.wt for p in procs) / n

print(f"\nAverage TAT: {avg_tat:.2f}")
print(f"Average WT:  {avg_wt:.2f}")

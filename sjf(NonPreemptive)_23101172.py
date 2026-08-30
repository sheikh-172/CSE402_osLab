class Process:
  def __init__(self, pid, at, bt):
    self.pid, self.at, self.bt = pid, at, bt
    self.ct = self.tat = self.wt = 0
    self.done = False

n = int(input("enter number of process: "))
procs = []

# Input
for i in range(n):
  pid = f"p{i+1}"
  at = int(input(f"enter AT for {pid}: "))
  bt = int(input(f"enter BT for {pid}: "))
  procs.append(Process(pid, at, bt))

# SJF NonPreemptive
time, count = 0, 0
while count < n:
  ready = [p for p in procs if p.at <= time and not p.done]
  if not ready:
    time += 1
    continue
  curr = min(ready, key=lambda p: p.bt)
  time += curr.bt
  curr.ct = time
  curr.tat = curr.ct - curr.at
  curr.wt = curr.tat - curr.bt
  curr.done = True
  count += 1

# Output
print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for p in sorted(procs, key=lambda x: x.pid):
  print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")

# Average
avg_tat = sum(p.tat for p in procs) / n
avg_wt = sum(p.wt for p in procs) / n

print(f"\nAverage TAT: {avg_tat:.2f}")
print(f"Average WT:    {avg_wt:.2f}")

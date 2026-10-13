#SSTF

head = int(input("enter head: "))

n = int(input("enter number of request: "))

requests = []

for i in range(n):
    x = int(input(f"enter request {i+1}: "))
    requests.append(x)

total = 0
current = head

while requests:

    nearest = min(requests, key=lambda x: abs(current - x))
    distance = abs(current - nearest)

    print(f"{current} -> {nearest} ")
    total += distance
    current = nearest
    requests.remove(nearest)

print("
total seek =", total)

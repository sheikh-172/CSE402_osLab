#FIFO(page replacement algo)

frames = int(input("enter frame size: "))

ref_input = input("enter reference string: ")
pages = [int(x) for x in ref_input.split()]

frame = []
page_faults = 0

print("
page	frames		status")
for page in pages:
    if page not in frame:
        page_faults += 1

        if len(frame) < frames:
            frame.append(page)
        else:
            frame.pop(0)
            frame.append(page)

        status = "page fault"
    else:
        status = "hit"

    print(page, "	", frame, "	", status)

print("
total page faults =", page_faults)

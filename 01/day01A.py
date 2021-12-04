with open("./input.txt") as input_file:
    input = input_file.read()

probes = input.split("\n")
probes.remove("") # Lol

prev = None
increments = 0

for probe in [int(probe) for probe in probes]:
    if prev is not None and prev < probe: 
        increments += 1
    prev = probe

print(f"The measurements have increased {increments} times.")
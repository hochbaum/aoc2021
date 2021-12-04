with open("./input.txt") as input_file:
    input = input_file.read()

probes = input.split("\n")
probes.remove("") # Lol
probes = list(map(int, probes))

prev = None
increments = 0
n_probes = len(probes)

for i in range(n_probes):
    if i > n_probes - 3: 
        continue
    sum = probes[i] + probes[i + 1] + probes[i + 2]
    if prev is not None and prev < sum: 
        increments += 1
    prev = sum

print(f"The measurements have increased {increments} times.")
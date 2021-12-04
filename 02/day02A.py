with open("./input.txt") as input_file:
    input = input_file.read()

input = input.split("\n")
input.remove("") # Lol

horizontal = 0
depth = 0

for line in input:
    split = line.split(" ")
    op = split[0]
    n = int(split[1])
    
    match op:
        case "forward":
            horizontal += n
        case "up":
            depth -= n
        case "down":
            depth += n

print(f"The result is {horizontal * depth}.")       
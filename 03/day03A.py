with open("./input.txt") as input_file:
    input = input_file.read()

diagnostic = input.split("\n")
diagnostic.remove("") # Lol
diagnostic = [int(str, 2) for str in diagnostic]

gamma = 0

for i in reversed(range(12)):
    set = 0
    unset = 0

    for n in diagnostic:
        if n >> i & 1 == 1:
            set += 1
        else:
            unset += 1
    if set > unset:
        gamma = gamma | (1 << i)

epsilon = ~(gamma) & 0xFFF # Only 12 digits
print(gamma * epsilon)
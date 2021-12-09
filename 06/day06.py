def simulate_fish(fish, days):
    """
    Simulates the fish reproduction and returns the total amount of fish.
    """
    for _ in range(days):
        produced = fish[0]
        for age in range(1, 9):
            fish[age - 1] = fish[age]
        fish[6] += produced
        fish[8] = produced
    return sum(fish.values())       

def main():
    with open("./input.txt") as input_file:
        input = input_file.read()    

    fish = {}
    for i in range(9): fish[i] = 0
    for age in [int(str) for str in input.split(",")]: fish[age] = fish[age] + 1

    print(f"Fish after 80 days: {simulate_fish(fish.copy(), 80)}")
    print(f"Fish after 256 days: {simulate_fish(fish.copy(), 256)}")

if __name__ == "__main__":
    main()
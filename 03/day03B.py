def main():
    with open("./input.txt") as input_file:
        input = input_file.read()

    diagnostic = input.split("\n")
    diagnostic.remove("") # Lol
    diagnostic = [int(str, 2) for str in diagnostic]

    # If mode is set to <0, we look for the least common bit. If set to >0, we look for the most common bit.
    def get_common_bit(list, pos, mode):
        set = 0
        unset = 0
        for n in list:
            if n >> pos & 1 == 1:
                set = set + 1
            else:
                unset = unset + 1 
        if mode < 0: 
            return set < unset
        else: 
            return set >= unset

    def get_number(list, mode):
        tmp = list.copy()
        for i in reversed(range(12)):
            set = get_common_bit(tmp, i, mode)
            for n in tmp.copy():
                if len(tmp) == 1:
                    break
                if (set and (n >> i) & 1 != 1) or (not set and (n >> i) & 1 == 1):
                    tmp.remove(n)
        return tmp[0]            

    oxygen_rating = get_number(diagnostic, 1)
    co2_scrubber = get_number(diagnostic, -1)

    print(oxygen_rating * co2_scrubber)

if __name__ == "__main__":
    main()
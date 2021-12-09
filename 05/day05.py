from vent import Point, Line, Field    

def fill_field(field, lines):
    for line in lines:
        start, end = Point(line[0][0], line[0][1]), Point(line[1][0], line[1][1])
        field.add_line(Line(start, end))

def main():
    with open("./input.txt") as input_file:
        input = input_file.read()
    input = [[[int(z) for z in y.split(',')] for y in raw_line.strip().split(' -> ')] for raw_line in input.split("\n") if raw_line.strip() != '']

    field = Field(do_diagonal=False)
    fill_field(field, input)
    print(f"Overlaps without diagonal lines: {field.find_overlaps()}")

    field = Field(do_diagonal=True)
    fill_field(field, input)
    print(f"Overlaps with diagonal lines: {field.find_overlaps()}")

if __name__ == "__main__":
    main()
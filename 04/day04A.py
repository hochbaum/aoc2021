from bingo import BingoBoard

BOARD_SIZE = 5

def main():
    with open("./input.txt") as input_file:
        input = input_file.read()

    parts = input.split("\n\n")
    draws = [int(str) for str in parts[0].split(",")]
    raw_boards = parts[1:]

    boards = []
    for raw_board in raw_boards:
        numbers = [int(str) for str in raw_board.split()]
        board = BingoBoard(BOARD_SIZE)
        board.fill(numbers)
        boards.append(board)

    winner = None
    for draw in draws:
        if winner != None: 
            break
        for board in boards.copy():
            board.draw_number(draw)
            if board.has_won():
                winner = board
                break

    final_score = winner.get_score()          
    print(f"The score of the final winner is {final_score}.")

if __name__ == "__main__":
    main()
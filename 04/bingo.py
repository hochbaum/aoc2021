class BingoBoard:
    def __init__(self, size):
        """
        Creates an empty instance of a BingoBoard.
        """
        self.size = size
        self.numbers = [[0 for _ in range(size)] for _ in range(size)]
        self.marked = [[0 for _ in range(size)] for _ in range(size)]
        self.current_draw = 0

    def fill(self, numbers):
        """
        Populates the numbers on the BingoBoard using the provided number list.
        """
        row = 0
        column = 0
        for number in numbers:
            if column % self.size == 0 and column != 0:
                column = 0
                row += 1
            self.numbers[row][column] = number
            column += 1

    def mark_column(self, row, column):
        """ 
        Sets a specific column marked. 
        """
        self.marked[row][column] = 1

    def is_marked(self, row, column):
        """ 
        Returns whether or not the specified column is marked.
        """
        return self.marked[row][column]

    def get_number(self, row, column):
        """
        Returns the number at the specified column.
        """
        return self.numbers[row][column]     

    def draw_number(self, number):
        """
        Draws the specified number and marks it on the BingoBoard.
        """
        self.current_draw = number
        for row in range(self.size):
            for column in range(self.size):
                if self.get_number(row, column) == number:
                    self.mark_column(row, column)

    def has_won(self):
        """
        Checks whether the board has won by counting horizontal and vertical
        matches.
        """
        for row in range(self.size):
            horizontal_matches = 0
            for column in range(self.size):
                if self.is_marked(row, column):
                    horizontal_matches += 1
            if horizontal_matches >= self.size:
                return True
        for column in range(self.size):
            vertical_matches = 0
            for row in range(self.size):
                if self.is_marked(row, column):
                    vertical_matches += 1
            if vertical_matches >= self.size:
                return True
        return False

    def get_score(self):
        """
        Returns the final score of the BingoBoard by multiplying the sum of
        all unmarked numbers by the current draw.
        """
        sum = 0
        for row in range(self.size):
            for column in range(self.size):
                if not self.is_marked(row, column):
                    sum += self.get_number(row, column)
        return sum * self.current_draw    
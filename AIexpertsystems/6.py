class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.moves = []

    def clean(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == 'dirty':
                    self.clean_cell(row, col)

    def clean_cell(self, row, col):
        while row > 0:
            self.move('up')
            row -= 1
        while col > 0:
            self.move('left')
            col -= 1
        self.grid[row][col] = 'clean'
        self.moves.append((row, col))
        print(f"Cleaned cell at ({row}, {col})")

    def move(self, direction):
        if direction == 'up':
            self.moves.append('up')
            print("Moving up")
        elif direction == 'down':
            self.moves.append('down')
            print("Moving down")
        elif direction == 'left':
            self.moves.append('left')
            print("Moving left")
        elif direction == 'right':
            self.moves.append('right')
            print("Moving right")

    def print_moves(self):
        print("Sequence of movements:")
        for move in self.moves:
            print(move)

# Example grid (dirty cells represented by 'dirty')
grid = [
    ['clean', 'dirty', 'clean', 'dirty'],
    ['clean', 'clean', 'dirty', 'clean'],
    ['dirty', 'clean', 'clean', 'dirty'],
    ['dirty', 'dirty', 'clean', 'clean']
]

# Initialize and run the vacuum cleaner
cleaner = VacuumCleaner(grid)
cleaner.clean()
cleaner.print_moves()

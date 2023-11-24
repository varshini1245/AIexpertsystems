class MonkeyBananaProblem:
    def __init__(self):
        self.room = [
            "#####",
            "# M  #",
            "#    #",
            "# B  #",
            "#####"
        ]
        self.monkey_pos = (1, 2)  # Monkey's initial position (row, column)
        self.box_pos = (3, 2)  # Box's initial position (row, column)
        self.banana_pos = (3, 2)  # Banana's position (row, column)
        self.has_box = False

    def print_room(self):
        for row in self.room:
            print(row)

    def move_monkey(self, direction):
        directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }

        move = directions.get(direction)
        if move:
            new_pos = (self.monkey_pos[0] + move[0], self.monkey_pos[1] + move[1])
            if self.is_valid_move(new_pos):
                if new_pos == self.box_pos:
                    self.move_box(direction)
                self.monkey_pos = new_pos
                self.check_for_banana()

    def move_box(self, direction):
        box_move = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }

        box_new_pos = (self.box_pos[0] + box_move[direction][0], self.box_pos[1] + box_move[direction][1])
        if self.is_valid_move(box_new_pos):
            self.box_pos = box_new_pos

    def is_valid_move(self, pos):
        row, col = pos
        return 0 <= row < len(self.room) and 0 <= col < len(self.room[0]) and self.room[row][col] != '#'

    def check_for_banana(self):
        if self.monkey_pos == self.banana_pos and self.has_box:
            print("Monkey got the banana! 🍌")
        else:
            print("Keep trying!")

    def play(self):
        self.print_room()
        print("Help the monkey get the banana by moving around the room and pushing the box.")
        while self.monkey_pos != self.banana_pos or not self.has_box:
            move = input("Enter direction (up/down/left/right): ")
            self.move_monkey(move)
            self.print_room()

# Initialize and play the game
game = MonkeyBananaProblem()
game.play()

#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.flags = [[False for _ in range(width)] for _ in range(height)]
        self.game_over = False

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    if self.revealed[y][x]:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                    elif self.flags[y][x]:
                        print('F', end=' ')
                    else:
                        print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            print("Coordinates are out of bounds!")
            return True  # Don't end the game, just retry.

        if self.revealed[y][x] or self.flags[y][x]:
            print("This cell is already revealed or flagged.")
            return True

        if (y * self.width + x) in self.mines:
            self.game_over = True
            return False

        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def toggle_flag(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            print("Coordinates are out of bounds!")
            return

        if self.revealed[y][x]:
            print("Cannot flag a revealed cell.")
            return

        self.flags[y][x] = not self.flags[y][x]

    def play(self):
        while not self.game_over:
            self.print_board()
            try:
                action = input("Enter action (r x y for reveal, f x y for flag): ").split()
                if len(action) != 3:
                    print("Invalid input. Format: r x y or f x y")
                    continue

                command, x, y = action[0], int(action[1]), int(action[2])
                if command == 'r':
                    if not self.reveal(x, y):
                        self.print_board(reveal=True)
                        print("Game Over! You hit a mine.")
                        break
                elif command == 'f':
                    self.toggle_flag(x, y)
                else:
                    print("Invalid command. Use 'r' to reveal or 'f' to flag.")
            except ValueError:
                print("Invalid input. Please enter valid coordinates.")
            except IndexError:
                print("Coordinates are out of bounds!")

        if not self.game_over:
            print("Congratulations! You cleared the minefield.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()

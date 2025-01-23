def print_grid(grid):
    for row in grid:
        print("".join(row))

def is_valid_horizontal(grid, word, row, col):
    if col + len(word) > 10:
        return False
    for i in range(len(word)):
        if grid[row][col + i] != '-' and grid[row][col + i] != word[i]:
            return False
    return True

def is_valid_vertical(grid, word, row, col):
    if row + len(word) > 10:
        return False
    for i in range(len(word)):
        if grid[row + i][col] != '-' and grid[row + i][col] != word[i]:
            return False
    return True

def place_horizontal(grid, word, row, col):
    original = []
    for i in range(len(word)):
        original.append(grid[row][col + i])
        grid[row][col + i] = word[i]
    return original

def place_vertical(grid, word, row, col):
    original = []
    for i in range(len(word)):
        original.append(grid[row + i][col])
        grid[row + i][col] = word[i]
    return original

def remove_horizontal(grid, original, row, col):
    for i in range(len(original)):
        grid[row][col + i] = original[i]

def remove_vertical(grid, original, row, col):
    for i in range(len(original)):
        grid[row + i][col] = original[i]

def solve(grid, words, index):
    if index == len(words):
        return True

    word = words[index]

    for row in range(10):
        for col in range(10):
            if is_valid_horizontal(grid, word, row, col):
                original = place_horizontal(grid, word, row, col)
                if solve(grid, words, index + 1):
                    return True
                remove_horizontal(grid, original, row, col)

            if is_valid_vertical(grid, word, row, col):
                original = place_vertical(grid, word, row, col)
                if solve(grid, words, index + 1):
                    return True
                remove_vertical(grid, original, row, col)

    return False

def crossword_puzzle():
    grid = [list(input().strip()) for _ in range(10)]
    words = input().strip().split(";")
    if solve(grid, words, 0):
        print_grid(grid)
    else:
        print("No solution found.")

crossword_puzzle()

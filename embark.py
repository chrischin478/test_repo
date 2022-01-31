
width = 4
height = 4
grid = [
    ['W','T','R','M'],
    ['B','C','U','A'],
    ['A','K','C','R'],
    ['G','I','S','T'],
]

words = [
    'TRUCK',
    'MAP',
    'GIST',
    'ART',
    'CRATE'
]

words = [
    'TRUCK'
]

def adjacent_search(grid, grid_width, grid_height, word, word_len, row, col, word_idx):
    next_letter = word[word_idx]
    dirs = ['u','d','l','r']

    match = None
    for dir in dirs:
        if dir == 'u':
            adj_row = row - 1
            if adj_row >= 0:
                adj_letter = grid[adj_row][col]
                if adj_letter == next_letter:
                    match = 1
                    row = adj_row
                    break
        elif dir == 'd':
            adj_row = row + 1
            if adj_row <= grid_height - 1:
                adj_letter = grid[adj_row][col]
                if adj_letter == next_letter:
                    match = 1
                    row = adj_row
                    break
        elif dir == 'l':
            adj_col = col - 1
            if adj_col >= 0:
                adj_letter = grid[row][adj_col]
                if adj_letter == next_letter:
                    match = 1
                    col = adj_col
                    break
        else:
            adj_col = col + 1
            if adj_col <= grid_width - 1:
                adj_letter = grid[row][adj_col]
                if adj_letter == next_letter:
                    match = 1
                    col = adj_col
                    break
    if match:
        max_word_idx = word_len - 1
        if word_idx == max_word_idx:
            return word
        else:
            return adjacent_search(grid, grid_width, grid_height, word, word_len, row, col, word_idx + 1)
    else:
        return None

def valid_words_in_grid(grid, words, grid_width, grid_height):
    valid_words = []
    for word in words:
        valid_word = None
        word_len = len(word)
        current_letter = word[0]
        for row_idx, row in enumerate(grid):
            for col_idx, letter in enumerate(row):
                if current_letter == letter:
                    valid_word = adjacent_search(grid, grid_width, grid_height, word, word_len, row_idx, col_idx, 1)
                    if valid_word:
                        break
            if valid_word:
                valid_words.append(valid_word)
                break
                    

    return(valid_words)


valid_words_in_grid(grid, words, height, width)

def adjacent_search(grid, grid_width, grid_height, word, word_len, row, col, word_idx):
    next_letter = word[word_idx]
    print(next_letter)
    
    adj_letters = []
    for rc in ['row','col']:
        if rc == 'row':            
            for i in [-1,1]:
                adj_letter = []
                adj_row = row + i
                if i == 1:
                    if adj_row <= grid_height:
                        adj_letter = grid[adj_row][col]
                        print(adj_row, col)
                else:
                    if adj_row >= 0:
                        adj_letter = grid[adj_row][col]
                        print(adj_row, col)
                if adj_letter:
                    if adj_letter == next_letter:
                        row = adj_row
                    adj_letters.append(adj_letter)
        if rc == 'col':            
            for i in [-1,1]:
                adj_letter = []
                adj_col = col + i
                if i == 1:
                    if adj_col <= grid_width:
                        adj_letter = grid[row][adj_col]
                        print(row,adj_col)
                else:
                    if adj_col >= 0:
                        adj_letter = grid[row][adj_col]
                        print(row,adj_col)
                if adj_letter:
                    if adj_letter == next_letter:
                        col = adj_col
                    adj_letters.append(adj_letter)
    
    # print(adj_letters)
    if next_letter in adj_letters:
        if word_idx == word_len:
            return word
        else:
            return adjacent_search(grid, grid_width, grid_height, word, word_len, row, col, word_idx + 1)
    else:
        return None

    # # up
    # adj_row = row - 1
    # if adj_row >= 0:
    #     adj_letter = grid[adj_row][col]
    #     adj_letters.append(adj_letter)
    # # down
    # adj_row = row + 1
    # if adj_row <= grid_height:
    #     adj_letter = grid[adj_row][col]
    # # left
    # adj_col = col - 1
    # if adj_col >= 0:
    #     adj_letter = grid[row][adj_col]
    # # right
    # adj_col = col + 1
    # if adj_col <= grid_width:
    #     adj_letter = grid[row][adj_col]

    # if match:
    #     max_word_idx = word_len - 1
    #     if word_idx == max_word_idx:
    #         return word
    #     else:
    #         return adjacent_search(grid, grid_width, grid_height, word, word_len, row, col, word_idx + 1)
    # else:
    #     return None

def valid_words_in_grid(grid, words, grid_width, grid_height):
    max_row_idx = grid_height - 1
    max_col_idx = grid_width - 1
    valid_words = []
    for word in words:
        max_word_idx = len(word) - 1
        valid_word = None
        word_len = len(word)
        current_letter = word[0]
        for row_idx, row in enumerate(grid):
            for col_idx, letter in enumerate(row):
                if current_letter == letter:
                    valid_word = adjacent_search(grid, max_col_idx, max_row_idx, word, max_word_idx, row_idx, col_idx, 1)
                    if valid_word:
                        break
            if valid_word:
                valid_words.append(valid_word)
                break
                    

    # return(valid_words)


valid_words_in_grid(grid, words, height, width)

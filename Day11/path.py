#!python3

NUM_PATHS = 0
STARTX = 2
STARTY = 2

def find_num_paths(right_path, left_path):
    if right_path == 0 or left_path == 0:
        return 1
    return find_num_paths(right_path - 1, left_path) + find_num_paths(right_path, left_path - 1)


NUM_PATHS = find_num_paths(STARTX, STARTY)
print(NUM_PATHS)

# NUM_PATHS = 6...
if (NUM_PATHS == 8):
    print('line shouldn\'t be executed')

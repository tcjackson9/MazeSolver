### Author: Tanner Jackson
### Description: This program is a maze solver. Which gets an input from
### the user and solves a maze printing out each step at a time. When
### a location is passed there is a period left to show that, the path
### that can be followed is signified with hashtags. The program prints
### 'Solution Found!' when the solution is found, and then ends
### the program.
###

def main():
    maze_file = input('Please give the maze file:\n')
    maze_open = open(maze_file)
    maze_open2 = open(maze_file)
    maze_open3 = open(maze_file)
    two_d_array = two_d_maze(maze_open, maze_open2, maze_open3)
    two_d_array, which_one = print_first_one(two_d_array)
    checker = False
    if which_one == '^':
        checker = True
    check_pos, direction, two_d_array, end_maze = \
        check_array(two_d_array, checker)
    back_track = False
    print_coords_direction(check_pos, direction, two_d_array, back_track)
    move_maze(two_d_array, check_pos, direction, back_track, end_maze)


def two_d_maze(maze_open, maze_open2, maze_open3):
    '''
    This function creates a two dimensional array which
    stores the data that will be used in the program. This
    array's information is given by a .txt file that the
    user inputs.
    maze_open: File in read mode.
    maze_open2: File in read mode.
    maze_open3: File in read mode.
    '''
    two_d_array = []
    two_d_array = add_line_before(maze_open2, two_d_array)
    longest = 0
    for line in maze_open:
        line_array = []
        line_array.append(' ')
        for each in line:
            if len(line) - 1 > longest:
                longest = len(line) - 1
            if each != '\n':
                line_array.append(each)
        line_array.append(' ')
        two_d_array.append(line_array)
    # Makes sure each line is the same length.
    for i in range(len(two_d_array)):
        while len(two_d_array[i]) <= longest:
            two_d_array[i].append(' ')
    two_d_array = add_line_after(maze_open3, two_d_array)
    return two_d_array


def add_line_before(maze_open2, two_d_array):
    '''
    This function adds a line before in the two dimensional
    array so that the program does not create an error in
    the future, the error that would occur is about
    indexing out of the array.
    maze_open2: File in read mode.
    two_d_array: Array.
    '''
    count = 0
    for line_before in maze_open2:
        if count == 0:
            one_before = []
            for one in line_before:
                one_before.append(' ')
        count += 1
    two_d_array.append(one_before)
    return two_d_array


def add_line_after(maze_open3, two_d_array):
    '''
    This function adds a line after in the two dimensional
    array so that the program does not create an error in
    the future, the error that would occur is about
    indexing out of the array.
    maze_open3: File in read mode.
    two_d_array: Array.
    '''
    count2 = 0
    for line_after in maze_open3:
        if count2 == 0:
            one_after = []
            for one in line_after:
                one_after.append(' ')
        count2 += 1
    two_d_array.append(one_after)
    return two_d_array


def print_first_one(two_d_array):
    '''
    This function prints out the first print for the maze.
    It does this by searching through the two dimensional
    array and printing out each piece.
    two_d_array: 2-d array.
    '''
    for line in range(1, len(two_d_array) - 1):
        for each in range(1, len(two_d_array[line]) - 2):
            # Changes the start location to a pointer.
            if two_d_array[line][each] == 'S':
                if two_d_array[line - 1][each] == '#':
                    print('^', end='')
                    two_d_array[line][each] = '^'
                elif two_d_array[line][each - 1] == '#':
                    print('<', end='')
                    two_d_array[line][each] = '<'
                elif two_d_array[line + 1][each] == '#':
                    print('v', end='')
                    two_d_array[line][each] = 'v'
                else:
                    print('>', end='')
                    two_d_array[line][each] = '>'
                which_one = two_d_array[line][each]
            else:
                print(two_d_array[line][each], end='')
        print(two_d_array[line][len(two_d_array[line]) - 2])
    return two_d_array, which_one


def print_maze(two_d_array, back_track, check_pos, direction):
    '''
    This function prints out the maze to the user, this is the
    function that is called when the maze is being traversed
    normally, not in backtrack.
    two_d_array: 2-d array.
    back_track: Boolean.
    check_pos: Tuple.
    direction: String.
    '''
    if back_track is True:
        backtrack_maze(two_d_array, check_pos, direction)
    for line in range(1, len(two_d_array) - 1):
        for each in range(1, len(two_d_array[line]) - 2):
            print(two_d_array[line][each], end='')
        print(two_d_array[line][len(two_d_array[line]) - 2])
    return two_d_array


def backtrack_print_maze(two_d_array, back_track, check_pos, direction):
    '''
    This function prints out the maze to the user. This is the
    function that is called when the maze is being traversed
    in backtrack.
    two_d_array: 2-d array.
    back_track: Boolean.
    check_pos: Tuple.
    direction: String.
    '''
    for line in range(1, len(two_d_array) - 1):
        for each in range(1, len(two_d_array[line]) - 2):
            print(two_d_array[line][each], end='')
        print(two_d_array[line][len(two_d_array[line]) - 2])
    return two_d_array


def check_array(two_d_array, checker):
    '''
    This function sets the direction of the pointer,
    it checks to see which direction it should be facing
    in the user print out.
    two_d_array: 2-d array.
    checker: Boolean.
    '''
    end_maze = False
    for line in range(len(two_d_array)):
        for each in range(len(two_d_array[line])):
            # Case for if the pointer is north the start with
            # hashtags to the left.
            if two_d_array[line][each] == '^' and checker is True:
                direction = 'N'
                two_d_array[line][each] = '^'
                check_pos = (each, line)
            # Case for north pointer.
            elif two_d_array[line][each] == '^':
                two_d_array, end_maze, direction, check_pos = \
                    check_array_north(two_d_array, line, each)
            # Case for east pointer.
            elif two_d_array[line][each] == '>':
                two_d_array, end_maze, direction, check_pos = \
                    check_array_east(two_d_array, line, each)
            # Case for south pointer.
            elif two_d_array[line][each] == 'v':
                two_d_array, end_maze, direction, check_pos = \
                    check_array_south(two_d_array, line, each)
            # Case for west pointer.
            elif two_d_array[line][each] == '<':
                two_d_array, end_maze, direction, check_pos = \
                    check_array_west(two_d_array, line, each)
    return check_pos, direction, two_d_array, end_maze


def check_array_north(two_d_array, line, each):
    '''
    This function is called if the direction of the pointer
    is north. Then it checks for which way the pointer should
    change to or stay the same.
    two_d_array: 2-d array.
    line: Integer.
    each: Integer.
    '''
    end_maze = False
    # Checks if the maze is supposed to end.
    if two_d_array[line - 1][each] == 'E':
        end_maze = True
    if two_d_array[line][each - 1] != ' ' and \
            two_d_array[line][each - 1] != '.':
        two_d_array[line][each] = '<'
        direction = 'W'
    elif two_d_array[line - 1][each] != ' ' and \
            two_d_array[line - 1][each] != '.':
        direction = 'N'
    elif two_d_array[line][each + 1] != ' ' and \
            two_d_array[line][each + 1] != '.':
        two_d_array[line][each] = '>'
        direction = 'E'
    else:
        two_d_array[line][each] = 'v'
        direction = 'S'
    check_pos = (each, line)
    return two_d_array, end_maze, direction, check_pos


def check_array_east(two_d_array, line, each):
    '''
    This function is called if the direction of the pointer
    is east. Then it checks for which way the pointer should
    change to or stay the same.
    two_d_array: 2-d array.
    line: Integer.
    each: Integer.
    '''
    end_maze = False
    # Checks if the maze is supposed to end.
    if two_d_array[line][each + 1] == 'E':
        end_maze = True
    if two_d_array[line - 1][each] != ' ' and \
            two_d_array[line - 1][each] != '.':
        two_d_array[line][each] = '^'
        direction = 'N'
    elif two_d_array[line][each + 1] != ' ' and \
            two_d_array[line][each + 1] != '.':
        direction = 'E'
    elif two_d_array[line + 1][each] != ' ' and \
            two_d_array[line + 1][each] != '.':
        two_d_array[line][each] = 'v'
        direction = 'S'
    else:
        two_d_array[line][each] = '<'
        direction = 'W'
    check_pos = (each, line)
    return two_d_array, end_maze, direction, check_pos


def check_array_south(two_d_array, line, each):
    '''
    This function is called if the direction of the pointer
    is south. Then it checks for which way the pointer should
    change to or stay the same.
    two_d_array: 2-d array.
    line: Integer.
    each: Integer.
    '''
    end_maze = False
    # Checks if the maze is supposed to end.
    if two_d_array[line + 1][each] == 'E':
        end_maze = True
    if two_d_array[line][each + 1] != ' ' and \
            two_d_array[line][each + 1] != '.':
        two_d_array[line][each] = '>'
        direction = 'E'
    elif two_d_array[line + 1][each] != ' ' and \
            two_d_array[line + 1][each] != '.':
        direction = 'S'
    elif two_d_array[line][each - 1] != ' ' and \
            two_d_array[line][each - 1] != '.':
        two_d_array[line][each] = '<'
        direction = 'W'
    else:
        two_d_array[line][each] = '^'
        direction = 'N'
    check_pos = (each, line)
    return two_d_array, end_maze, direction, check_pos


def check_array_west(two_d_array, line, each):
    '''
    This function is called if the direction of the pointer
    is west. Then it checks for which way the pointer should
    change to or stay the same.
    two_d_array: 2-d array.
    line: Integer.
    each: Integer.
    '''
    end_maze = False
    # Checks if the maze is supposed to end.
    if two_d_array[line][each - 1] == 'E':
        end_maze = True
    if two_d_array[line + 1][each] != ' ' and \
            two_d_array[line + 1][each] != '.':
        two_d_array[line][each] = 'v'
        direction = 'S'
    elif two_d_array[line][each - 1] != ' ' and \
            two_d_array[line][each - 1] != '.':
        direction = 'W'
    elif two_d_array[line - 1][each] != ' ' and \
            two_d_array[line - 1][each] != '.':
        two_d_array[line][each] = '^'
        direction = 'N'
    else:
        two_d_array[line][each] = '>'
        direction = 'E'
    check_pos = (each, line)
    return two_d_array, end_maze, direction, check_pos


def backtrack_check_array(two_d_array):
    '''
    This function sets the direction of the pointer,
    it checks to see which direction it should be facing
    in the user print out.
    two_d_array: 2-d array.
    checker: Boolean.
    '''
    for line in range(len(two_d_array)):
        for each in range(len(two_d_array[line])):
            if two_d_array[line][each] == '^':
                two_d_array, direction, check_pos = \
                    back_track_check_array_north(two_d_array, line, each)
            elif two_d_array[line][each] == '>':
                two_d_array, direction, check_pos = \
                    back_track_check_array_east(two_d_array, line, each)
            elif two_d_array[line][each] == 'v':
                two_d_array, direction, check_pos = \
                    back_track_check_array_south(two_d_array, line, each)
            elif two_d_array[line][each] == '<':
                two_d_array, direction, check_pos = \
                    back_track_check_array_west(two_d_array, line, each)
    return check_pos, direction, two_d_array


def back_track_check_array_north(two_d_array, line, each):
    '''
    This function is called if the direction of the pointer
    is north. Then it checks for which way the pointer should
    change to or stay the same.
    two_d_array: 2-d array.
    line: Integer.
    each: Integer.
    '''
    if two_d_array[line][each - 1] != ' ':
        two_d_array[line][each] = '<'
        direction = 'W'
    elif two_d_array[line - 1][each] != ' ':
        direction = 'N'
    elif two_d_array[line][each + 1] != ' ':
        two_d_array[line][each] = '>'
        direction = 'E'
    else:
        two_d_array[line][each] = 'v'
        direction = 'S'
    check_pos = (each, line)
    return two_d_array, direction, check_pos


def back_track_check_array_east(two_d_array, line, each):
    '''
    This function is called if the direction of the pointer
    is east. Then it checks for which way the pointer should
    change to or stay the same.
    two_d_array: 2-d array.
    line: Integer.
    each: Integer.
        '''
    if two_d_array[line - 1][each] != ' ':
        two_d_array[line][each] = '^'
        direction = 'N'
    elif two_d_array[line][each + 1] != ' ':
        direction = 'E'
    elif two_d_array[line + 1][each] != ' ':
        two_d_array[line][each] = 'v'
        direction = 'S'
    else:
        two_d_array[line][each] = '<'
        direction = 'W'
    check_pos = (each, line)
    return two_d_array, direction, check_pos


def back_track_check_array_south(two_d_array, line, each):
    '''
    This function is called if the direction of the pointer
    is south. Then it checks for which way the pointer should
    change to or stay the same.
    two_d_array: 2-d array.
    line: Integer.
    each: Integer.
    '''
    if two_d_array[line][each + 1] != ' ':
        two_d_array[line][each] = '>'
        direction = 'E'
    elif two_d_array[line + 1][each] != ' ':
        direction = 'S'
    elif two_d_array[line][each - 1] != ' ':
        two_d_array[line][each] = '<'
        direction = 'W'
    else:
        two_d_array[line][each] = '^'
        direction = 'N'
    check_pos = (each, line)
    return two_d_array, direction, check_pos


def back_track_check_array_west(two_d_array, line, each):
    '''
    This function is called if the direction of the pointer
    is west. Then it checks for which way the pointer should
    change to or stay the same.
    two_d_array: 2-d array.
    line: Integer.
    each: Integer.
    '''
    if two_d_array[line + 1][each] != ' ':
        two_d_array[line][each] = 'v'
        direction = 'S'
    elif two_d_array[line][each - 1] != ' ':
        direction = 'W'
    elif two_d_array[line - 1][each] != ' ':
        two_d_array[line][each] = '^'
        direction = 'N'
    else:
        two_d_array[line][each] = '>'
        direction = 'E'
    check_pos = (each, line)
    return two_d_array, direction, check_pos


def print_coords_direction(check_pos, direction, two_d_array, back_track):
    '''
    This function prints out the coordinates and the direction to the user
    this is called every time the maze board is printed out.
    check_pos: Tuple.
    direction: String.
    two_d_array: 2-d array.
    back_track: Boolean.
    '''
    position = []
    for one in check_pos:
        position.append(one)
    x_pos = str(int(position[0]) - 1)
    y_pos = str(int(position[1]) - 1)
    print('Current Position:  ' + x_pos + ',' + y_pos)
    print('Current Direction: ' + str(direction))
    print()


def move_maze(two_d_array, check_pos, direction, back_track, end_maze):
    '''
    This function deals with actually changing the maze to end up finding
    the end point. It does this with a bunch of different if statements
    to make sure that the pointer is headed in the correct direction.
    two_d_array: 2-d array.
    check_pos: Tuple.
    direction: String.
    back_track: Boolean.
    end_maze: Boolean.
    '''
    while True:
        pointer, pos_x, pos_y = move_maze_first_part(direction, check_pos)
        if two_d_array[pos_y][pos_x] == pointer[0]:
            if direction == 'N':
                two_d_array, back_track = \
                    move_maze_north(two_d_array, pos_x, pos_y)
            if direction == 'W':
                two_d_array, back_track = \
                    move_maze_west(two_d_array, pos_x, pos_y)
            if direction == 'S':
                two_d_array, back_track = \
                    move_maze_south(two_d_array, pos_x, pos_y)
            if direction == 'E':
                two_d_array, back_track = \
                    move_maze_east(two_d_array, pos_x, pos_y)
        if back_track is False:
            check_pos, direction, two_d_array, end_maze = \
                check_array(two_d_array, False)
        print_maze(two_d_array, back_track, check_pos, direction)
        if back_track is False:
            print_coords_direction(check_pos, direction, two_d_array,
                                   back_track)
        # Case if the maze is supposed to end.
        if end_maze is True:
            print('Solution Found!')
            exit()


def move_maze_first_part(direction, check_pos):
    '''
    This function has some of the first part of the move_maze function.
    It sets a lot of variables that will be later used in the
    move_maze function.
    direction: String.
    check_pos: Tuple.
    '''
    if direction == 'N':
        pointer = ['^', '<', 'v', '>']
    elif direction == 'E':
        pointer = ['>', '^', '<', 'v']
    elif direction == 'S':
        pointer = ['v', '>', '^', '<']
    else:
        pointer = ['<', 'v', '>', '^']
    position = []
    for one in check_pos:
        position.append(one)
    pos_x = position[0]
    pos_y = position[1]
    return pointer, pos_x, pos_y


def move_maze_north(two_d_array, pos_x, pos_y):
    '''
    This function is the test case for if the pointer
    is facing the north direction. It then checks for
    which way it should move next to solve the maze.
    two_d_array: 2-d array.
    pos_x: Integer.
    pos_y: Integer.
    '''
    back_track = False
    if two_d_array[pos_y - 1][pos_x] == '#':
        two_d_array[pos_y - 1][pos_x] = '^'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y][pos_x - 1] == '#':
        two_d_array[pos_y][pos_x - 1] = '<'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y + 1][pos_x] == '#':
        two_d_array[pos_y + 1][pos_x] = 'v'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y][pos_x + 1] == '#':
        two_d_array[pos_y][pos_x + 1] = '>'
        two_d_array[pos_y][pos_x] = '.'
    else:
        # Case if user hits dead end.
        back_track = True
    return two_d_array, back_track


def move_maze_west(two_d_array, pos_x, pos_y):
    '''
    This function is the test case for if the pointer
    is facing the west direction. It then checks for
    which way it should move next to solve the maze.
    two_d_array: 2-d array.
    pos_x: Integer.
    pos_y: Integer.
    '''
    back_track = False
    if two_d_array[pos_y][pos_x - 1] == '#':
        two_d_array[pos_y][pos_x - 1] = '<'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y + 1][pos_x] == '#':
        two_d_array[pos_y + 1][pos_x] = 'v'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y][pos_x + 1] == '#':
        two_d_array[pos_y][pos_x + 1] = '>'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y - 1][pos_x] == '#':
        two_d_array[pos_y - 1][pos_x] = '^'
        two_d_array[pos_y][pos_x] = '.'
    else:
        # Case if user hits dead end.
        back_track = True
    return two_d_array, back_track


def move_maze_south(two_d_array, pos_x, pos_y):
    '''
    This function is the test case for if the pointer
    is facing the south direction. It then checks for
    which way it should move next to solve the maze.
    two_d_array: 2-d array.
    pos_x: Integer.
    pos_y: Integer.
    '''
    back_track = False
    if two_d_array[pos_y + 1][pos_x] == '#':
        two_d_array[pos_y + 1][pos_x] = 'v'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y][pos_x - 1] == '#':
        two_d_array[pos_y][pos_x - 1] = '>'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y - 1][pos_x] == '#':
        two_d_array[pos_y - 1][pos_x] = '^'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y][pos_x - 1] == '#':
        two_d_array[pos_y][pos_x - 1] = '<'
        two_d_array[pos_y][pos_x] = '.'
    else:
        # Case if user hits dead end.
        back_track = True
    return two_d_array, back_track


def move_maze_east(two_d_array, pos_x, pos_y):
    '''
    This function is the test case for if the pointer
    is facing the east direction. It then checks for
    which way it should move next to solve the maze.
    two_d_array: 2-d array.
    pos_x: Integer.
    pos_y: Integer.
    '''
    back_track = False
    if two_d_array[pos_y][pos_x + 1] == '#':
        two_d_array[pos_y][pos_x + 1] = '>'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y - 1][pos_x] == '#':
        two_d_array[pos_y - 1][pos_x] = '^'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y][pos_x - 1] == '#':
        two_d_array[pos_y][pos_x - 1] = '<'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y + 1][pos_x] == '#':
        two_d_array[pos_y + 1][pos_x] = 'v'
        two_d_array[pos_y][pos_x] = '.'
    else:
        # Case if user hits dead end.
        back_track = True
    return two_d_array, back_track


def backtrack_maze(two_d_array, check_pos, direction):
    '''
    This function deals with actually changing the maze to end up finding
    the end point. It does this with a bunch of different if statements
    to make sure that the pointer is headed in the correct direction.
    two_d_array: 2-d array.
    check_pos: Tuple.
    direction: String.
    '''
    while True:
        end_maze, back_track, pos_x, pos_y = \
            back_track_maze_first_part(check_pos)
        # Cases for if pointer is back on normal track.
        if two_d_array[pos_y - 1][pos_x] == '#':
            move_maze(two_d_array, check_pos, direction, False, end_maze)
        elif two_d_array[pos_y + 1][pos_x] == '#':
            move_maze(two_d_array, check_pos, direction, False, end_maze)
        elif two_d_array[pos_y][pos_x - 1] == '#':
            move_maze(two_d_array, check_pos, direction, False, end_maze)
        elif two_d_array[pos_y][pos_x + 1] == '#':
            move_maze(two_d_array, check_pos, direction, False, end_maze)
        else:
            # Case for if pointer is still in backtrack.
            if direction == 'N':
                two_d_array = \
                    back_track_maze_north(two_d_array, pos_x, pos_y)
            elif direction == 'W':
                two_d_array = \
                    back_track_maze_west(two_d_array, pos_x, pos_y)
            elif direction == 'S':
                two_d_array = \
                    back_track_maze_south(two_d_array, pos_x, pos_y)
            elif direction == 'E':
                two_d_array = \
                    back_track_maze_east(two_d_array, pos_x, pos_y)
            check_pos, direction, two_d_array = \
                backtrack_check_array(two_d_array)
            backtrack_print_maze(two_d_array, back_track, check_pos,
                                 direction)
            print_coords_direction(check_pos, direction, two_d_array,
                                   back_track)


def back_track_maze_first_part(check_pos):
    '''
    This function is the first part of the backtrack_maze,
    it sets a lot of variables that will be used in the
    function.
    check_pos: Tuple.
    '''
    end_maze = False
    back_track = True
    position = []
    for one in check_pos:
        position.append(one)
    pos_y = position[1]
    pos_x = position[0]
    return end_maze, back_track, pos_x, pos_y


def back_track_maze_north(two_d_array, pos_x, pos_y):
    '''
    This function is the test case for if the pointer
    is facing the north direction. It then checks for
    which way it should move next to solve the maze.
    two_d_array: 2-d array.
    pos_x: Integer.
    pos_y: Integer.
        '''
    if two_d_array[pos_y - 1][pos_x] == '.':
        two_d_array[pos_y - 1][pos_x] = '^'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y][pos_x - 1] == '.':
        two_d_array[pos_y][pos_x - 1] = '<'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y + 1][pos_x] == '.':
        two_d_array[pos_y + 1][pos_x] = 'v'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y][pos_x + 1] == '.':
        two_d_array[pos_y][pos_x + 1] = '>'
        two_d_array[pos_y][pos_x] = '.'
    return two_d_array


def back_track_maze_west(two_d_array, pos_x, pos_y):
    '''
    This function is the test case for if the pointer
    is facing the west direction. It then checks for
    which way it should move next to solve the maze.
    two_d_array: 2-d array.
    pos_x: Integer.
    pos_y: Integer.
    '''
    if two_d_array[pos_y][pos_x - 1] == '.':
        two_d_array[pos_y][pos_x - 1] = '<'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y + 1][pos_x] == '.':
        two_d_array[pos_y + 1][pos_x] = 'v'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y][pos_x + 1] == '.':
        two_d_array[pos_y][pos_x + 1] = '>'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y - 1][pos_x] == '.':
        two_d_array[pos_y - 1][pos_x] = '^'
        two_d_array[pos_y][pos_x] = '.'
    return two_d_array


def back_track_maze_south(two_d_array, pos_x, pos_y):
    '''
    This function is the test case for if the pointer
    is facing the south direction. It then checks for
    which way it should move next to solve the maze.
    two_d_array: 2-d array.
    pos_x: Integer.
    pos_y: Integer.
    '''
    if two_d_array[pos_y + 1][pos_x] == '.':
        two_d_array[pos_y + 1][pos_x] = 'v'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y][pos_x - 1] == '.':
        two_d_array[pos_y][pos_x - 1] = '<'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y - 1][pos_x] == '.':
        two_d_array[pos_y - 1][pos_x] = '^'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y][pos_x - 1] == '.':
        two_d_array[pos_y][pos_x - 1] = '<'
        two_d_array[pos_y][pos_x] = '.'
    return two_d_array


def back_track_maze_east(two_d_array, pos_x, pos_y):
    '''
    This function is the test case for if the pointer
    is facing the east direction. It then checks for
    which way it should move next to solve the maze.
    two_d_array: 2-d array.
    pos_x: Integer.
    pos_y: Integer.
    '''
    if two_d_array[pos_y][pos_x + 1] == '.':
        two_d_array[pos_y][pos_x + 1] = '>'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y - 1][pos_x] == '.':
        two_d_array[pos_y - 1][pos_x] = '^'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y][pos_x - 1] == '.':
        two_d_array[pos_y][pos_x - 1] = '<'
        two_d_array[pos_y][pos_x] = '.'
    elif two_d_array[pos_y + 1][pos_x] == '.':
        two_d_array[pos_y + 1][pos_x] = 'v'
        two_d_array[pos_y][pos_x] = '.'
    return two_d_array


main()

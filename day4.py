expected = ['X', 'M', 'A', 'S']

with open('day4', 'r') as file:
    lines = file.readlines()
    count_part1 = 0

    matrix = [list(line.strip()) for line in lines]

    for y in range(0, len(matrix)):
        for x in range(0, len(matrix[0])):
            # left -> right
            if x < len(matrix[0]) - 3 and [ matrix[y][x], matrix[y][x+1], matrix[y][x+2], matrix[y][x+3]] == expected:
                count_part1 += 1
            # right -> left
            if x > 2 and [ matrix[y][x], matrix[y][x-1], matrix[y][x-2], matrix[y][x-3]] == expected:
                count_part1 += 1
            # up -> down
            if y < len(matrix) -3 and [matrix[y][x], matrix[y+1][x], matrix[y+2][x], matrix[y+3][x]] == expected:
                count_part1 += 1
            # down -> up
            if y > 2 and [matrix[y][x], matrix[y-1][x], matrix[y-2][x], matrix[y-3][x]] == expected:
                count_part1 += 1
            # -> right down
            if  x < len(matrix[0]) - 3 and y < len(matrix) -3 and [ matrix[y][x], matrix[y+1][x+1], matrix[y+2][x+2], matrix[y+3][x+3]] == expected:
                count_part1 += 1
            # -> left down
            if x > 2 and y < len(matrix[0]) - 3 and [matrix[y][x], matrix[y+1][x-1], matrix[y+2][x-2], matrix[y+3][x-3]] == expected:
                count_part1 += 1
            # -> right up
            if x < len(matrix[0]) - 3 and y > 2 and [matrix[y][x], matrix[y-1][x+1], matrix[y-2][x+2], matrix[y-3][x+3]] == expected:
                count_part1 += 1
            # -> left up
            if x > 2 and y > 2 and [matrix[y][x], matrix[y-1][x-1], matrix[y-2][x-2], matrix[y-3][x-3]] == expected:
                count_part1 += 1

    # part 2
    count_part2 = 0
    for y in range(0, len(matrix)):
        for x in range(0, len(matrix[0])):
            if matrix[y][x] == 'A' and x > 0 and y > 0 and x < len(matrix[0])-1 and y < len(matrix)-1:
                if ((matrix[y-1][x-1] == 'M' and matrix[y+1][x+1] == 'S') or (matrix[y-1][x-1] == 'S' and matrix[y+1][x+1] == 'M')) and ((matrix[y - 1][x + 1] == 'M' and matrix[y + 1][x - 1] == 'S') or ( matrix[y - 1][x + 1] == 'S' and matrix[y + 1][x - 1] == 'M')):
                    count_part2 += 1

    print(f'Part1 {count_part1}')
    print(f'Part2 {count_part2}')
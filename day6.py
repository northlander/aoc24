from collections import namedtuple

Pos = namedtuple('Pos', ['x', 'y'])

def move(p, d, area):
    nextp = Pos(x=0, y=0)
    if d == '>':
        nextp = Pos(x=p.x + 1, y=p.y)
    elif d == 'v':
        nextp = Pos(x=p.x, y=p.y + 1)
    elif d == '<':
        nextp = Pos(x=p.x - 1, y=p.y)
    elif d == '^':
        nextp = Pos(x=p.x, y=p.y - 1)

    # Is outside of map?
    if nextp.x > len(area[0]) - 1 or nextp.x < 0 or nextp.y > len(area) - 1 or nextp.y < 0:
        return nextp, d, True

    nextd = d
    if area[nextp.y][nextp.x] == '#':
        # turn 90 right
        if d == '>':
            nextd = 'v'
        elif d == 'v':
            nextd = '<'
        elif d == '<':
            nextd = '^'
        elif d == '^':
            nextd = '>'
        return p, nextd, False
    else:
        return nextp, d, False

with open('day6', 'r') as file:
    lab = [line.strip() for line in file.readlines()]

    start_direction = '>'
    start = Pos(x = 0, y = 0)

    # Find starting position
    for y in range(0, len(lab)):
        for x in range(0, len(lab[0])):
            c = lab[y][x]
            if c in ['^', 'v', '>', '<']:
                start_direction = c
                start = Pos(x = x, y = y)

    print(f'Starting in direction {start_direction} at position {start}')

    pos = start
    direction = start_direction
    visited_positions = {pos}
    while True:
        next_pos, next_dir, outside = move(pos, direction, lab)
        if outside: break
        visited_positions.add(next_pos)
        pos = next_pos
        direction = next_dir

      #  print(f'{direction} - {pos}')
    print(f'Part1: visited position {len(visited_positions)}')

    loops = 0
    total = len(lab) * len(lab[0])
    for y in range(0, len(lab)):
        for x in range(0, len(lab[0])):
            if lab[y][x] in ['>', '<', '^', 'v', '#']:
                continue
            #print(f'Checking x{x} y{y}')

            current_iteration = y*len(lab[0]) + x
            if current_iteration % 100 == 0:
                print(f'Checking {current_iteration}/{total}')

            pos = start
            direction = start_direction
            visited_positions2 = {(start, direction)}
            lab2 = [x for x in lab]
            lab2[y] = lab2[y][:x] + "#" +  lab2[y][x + 1:] # Insert obstacle
            while True:
                next_pos, next_dir, outside = move(pos, direction, lab2)
                if outside:
                    break
                if (next_pos, next_dir) in visited_positions2:
                   # print(f"loop detected at {x},{y}")
                    loops += 1
                    break
                visited_positions2.add((next_pos, next_dir))
                pos = next_pos
                direction = next_dir
    print(f'Part2 loops {loops}')



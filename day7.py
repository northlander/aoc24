import itertools

operators = ['*', '+']
with open('day7', 'r') as file:
    lines = file.readlines()
    equations = [ [ int(line.strip().split(':')[0].strip()), [int(num.strip()) for num in line.strip().split(':')[1].split()] ] for line in lines]
    sum_part1 = 0
    for equation in equations:
        print(f'Testing equation {equation}')
        combinations = [list(i) for i in itertools.product(operators, repeat=len(equation[1])-1)]
        for combination in combinations:
            result = equation[1][0]
            for i in range(1,len(equation[1])):
                if combination[i-1] == '+':
                    result += equation[1][i]
                else:
                    result *= equation[1][i]
            if result == equation[0]:
                print(f'Result: {result} matches!')
                sum_part1 += result
                break
    print("Part2")
    # Part 2
    sum_part2 = 0
    for equation in equations:
        part2_operators = ['+', '*', '||']
        combinations = [list(i) for i in itertools.product(part2_operators, repeat=len(equation[1]) - 1)]
        for combination in combinations:
            result = equation[1][0]
            for i in range(1,len(equation[1])):
                if combination[i-1] == '+':
                    result += equation[1][i]
                elif combination[i-1] == '*':
                    result *= equation[1][i]
                else:
                    result = int(str(result) + str(equation[1][i]))
            if result == equation[0]:
                print(f'Result: {result} matches!')
                sum_part2 += result
                break
    print(f'Part2 {sum_part2}')
import re

with open('day3', 'r') as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        mul_instructions_text = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", line)
        print(mul_instructions_text)
        instr = [x[4:][:-1].split(",") for x in mul_instructions_text]
        for i in instr:
            total += int(i[0])*int(i[1])
    print(f'part1: {total}')


with open('day3', 'r') as file:
    lines = file.readlines()
    total = 0
    mode = "do"
    for line in lines:
        for i in range(0, len(line)):
            current_text = line[:i]
            match_instr = re.search("mul\(([0-9]{1,3}),([0-9]{1,3})\)$", current_text)
            match_do = re.search("do\(\)$", current_text)
            match_do_not = re.search("don't\(\)$", current_text)
            if match_do is not None:
                mode = "do"
            elif match_do_not is not None:
                mode = "do_not"
            elif match_instr is not None:
                x = int(match_instr.group(1))
                y = int(match_instr.group(2))
                if mode != "do_not":
                    total += y*x
    print(f'part2 {total}')

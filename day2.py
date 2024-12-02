import numpy as np

def is_safe(report):
    diffs = np.diff(report)
    prev_sign = np.sign(diffs[0])
    if abs(diffs[0]) > 3:
        return 0
    for i in range(1, len(diffs)):
        if prev_sign != np.sign(diffs[i]) or abs(diffs[i]) > 3:
            return i
    return -1  #it's safe

with open('day2', 'r') as file:
    lines = file.readlines()
    reports = [ [int(n) for n in x.split()] for x in lines]
    safe_reports_part1 = 0
    safe_reports_part2 = 0
    for report in reports:
        problem_index = is_safe(report)
        if problem_index == -1:
            safe_reports_part1 += 1
            safe_reports_part2 += 1
        else:
            # try removing each level
            for i in range(0, len(report)):
                problem_index = is_safe(report[:i] + report[i+1:])
                if problem_index == -1:
                    safe_reports_part2 += 1
                    break

    print(f'part1 {safe_reports_part1}')
    print(f'part2 {safe_reports_part2}')


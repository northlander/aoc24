from functools import cmp_to_key

with open('day5', 'r') as file:
    lines = file.readlines()
    rules = []
    pages_list = []
    parse_pages = False
    for line in lines:
        if line == '\n':
            parse_pages = True
        elif parse_pages:
            pages_list.append([int(c) for c in  line.strip().split(',')])
        else:
            rules.append([int(c) for c in line.strip().split('|')])

    sorted_pages = []
    def comp(i1, i2):

        if [i1,i2] in rules:
            return -1
        else:
            return 1

    sum1 = 0
    for pages in pages_list:
        rule_violation = False
        for i in range(0, len(pages)):
            at = pages[i]
            at_index = pages.index(at)
            at_before_rules = [x for x in rules if at == x[0] and x[1] in pages]
            at_after_rules = [x for x in rules if at == x[1] and x[0] in pages]
            # check if rules hold
            for rule in at_before_rules:
                check_index = pages.index(rule[1])
                if check_index < at_index:
                    rule_violation = True
                    break
            for rule in at_after_rules:
                check_index = pages.index(rule[0])
                if check_index > at_index:
                    rule_violation = True
                    break

            if rule_violation:
                break

        if rule_violation:
            sortedp = sorted(pages, key=cmp_to_key(comp))
            sorted_pages.append(sortedp)
            print(f'Pages {pages} breaks the rules, but has been sorted {sortedp}')
        else:
            print(f'Pages {pages} is good')
            middle_number = pages[len(pages)//2]
            sum1 += middle_number
    print(f'Part1 {sum1}')

    sum2 = 0
    for sp in sorted_pages:
        middle_number = sp[len(sp) // 2]
        sum2 += middle_number
    print(f'Part2 {sum2}')

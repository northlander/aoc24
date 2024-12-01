print("day1")

with open('day1', 'r') as file:
    lines = file.readlines()
    nums = [ [int(n) for n in x.split()] for x in lines]
    sorted_transposed = [sorted(list(x)) for x in zip(*nums)]
    distance_pairs = [abs(x[0] - x[1]) for x in zip(*sorted_transposed)]
    print(f'part1 {sum(distance_pairs)}')
    similarity_score = [x[0] * sorted_transposed[1].count(x[0]) for x in zip(*sorted_transposed)]
    print(f'part2 {sum(similarity_score)}')

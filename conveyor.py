"""Assumptions:
    Workers always use one hand (say their right) before the other - it would make a difference to the
    outcome if workers randomly selected which hand to use at the end of the production line if some or all workers had
    at least one hand full. Or one could assume that, if a worker has one hand full, they will use their free hand,
    which is equivalent to looping over hands like I have here.
"""


import random
from collections import Counter

choices = ['0', 'A', 'B']

components = [
    random.choice(choices)
    for i in range(100)
]

positions = [
    ['0', '0'] for i in range(3)
]

for component_index in range(len(components)):
    for position_index in range(len(positions)):
        for worker_index in range(len(positions[position_index])):
            if positions[position_index][worker_index] == '0':
                positions[position_index][worker_index] = components[component_index]
                components[component_index] = '0'

            elif ((positions[position_index][worker_index] == 'A' and components[component_index] == 'B')
                  or (positions[position_index][worker_index] == 'B' and components[component_index] == 'A')):
                positions[position_index][worker_index] = 'W'
                components[component_index] = '0'

            elif positions[position_index][worker_index] == 'W':
                positions[position_index][worker_index] = 'P'

            elif components[component_index] == '0' and positions[position_index][worker_index] == 'P':
                components[component_index] = 'P'
                positions[position_index][worker_index] = '0'

            else:
                continue

completed_components = Counter(components)
unprocessed_A = 0
unprocessed_B = 0
unprocessed_P = 0
for workers in positions:
    for worker in workers:
        if worker == 'A':
            unprocessed_A += 1
        elif worker == 'B':
            unprocessed_B += 1
        elif worker == 'W' or worker == 'P':
            unprocessed_P += 1
        else:
            continue

print(components)
print(positions)
unprocessed = unprocessed_A + unprocessed_B + unprocessed_P
print(f"Products assembled: {completed_components['P']}")
print(f"Components left unprocessed {unprocessed + completed_components['A'] + completed_components['B']}")
print(f"A components left unprocessed {completed_components['A'] + unprocessed_A}")
print(f"B components left unprocessed {completed_components['B'] + unprocessed_B}")
print(f"Assembled or part assembled products not placed on production line {completed_components['P'] + unprocessed_P}")

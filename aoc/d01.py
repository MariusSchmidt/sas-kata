import math


def process_data_a(filepath: str) -> int:
    file = open(filepath, 'r')
    lines = file.readlines()
    file.close()

    # init block
    previous_value = math.nan
    increase_count = 0

    # processing
    for line in lines:
        line = line.strip()
        if not line.isnumeric():
            continue
        if math.isnan(previous_value):
            previous_value = int(line)
            continue
        if int(line) > previous_value:
            increase_count += 1
        previous_value = int(line)

    return increase_count


def process_data_b(filepath: str) -> int:
    file = open(filepath, 'r')
    lines = file.read().splitlines()
    slices = sliding_window(lines, 3)
    previous_value = math.nan
    increases = 0
    for my_slice in slices:
        current_value = int(my_slice[0]) + int(my_slice[1]) + int(my_slice[2])
        if math.isnan(previous_value):
            previous_value = current_value
            continue
        if current_value > previous_value:
            increases = increases + 1
        previous_value = current_value
    file.close()
    return increases


def sliding_window(elements, window_size):
    slices = []
    if len(elements) <= window_size:
        return elements
    for i in range(len(elements) - window_size + 1):
        slices.append(elements[i:i + window_size])
    return slices

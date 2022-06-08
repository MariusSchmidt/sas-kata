import math


def process_data_a(filepath: str) -> int:
    file = open(filepath, 'r')
    lines = file.readlines()
    previous_value = math.nan
    increases = 0
    for line in lines:
        line = line.strip()
        if not line.isnumeric():
            continue
        if math.isnan(previous_value):
            previous_value = int(line)
            continue
        if int(line) > previous_value:
            increases = increases + 1
        previous_value = int(line)
    file.close()
    return increases

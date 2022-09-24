from typing import List


def list_avg(sequence: List[int]):
    return sum(sequence) / len(sequence)


v = list_avg([1, 2, 3])
print(v)

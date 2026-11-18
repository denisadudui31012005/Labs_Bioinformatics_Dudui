# Make an artificial DNA seq. of 200 to 400 bases in length, in which to simulate 3 to 4 transposable elements.
# Implement a software App which can detect the positions of these transposible elements(start,end)
# within the created DNA sequence.

import random

COMP = {"A": "T", "T": "A", "G": "C", "C": "G"}

MIN_SPACER = 10
MIN_DISTANCE = 3
K = 10


def take_r():
    return "ATGC"[random.randint(0, 3)]


def random_bases(length):
    return [take_r() for _ in range(length)]


def reverse_complement(bases):
    return [COMP[b] for b in reversed(bases)]


def make_element():
   
    arm = random_bases(random.randint(12, 16))
    loop = random_bases(random.randint(10, 20))
    return arm + loop + reverse_complement(arm)


def make_sequence():
    elements = [make_element() for _ in range(random.randint(3, 4))]
    element_bases = sum(len(te) for te in elements)
    spacer_count = len(elements) + 1

   
    smallest_total = max(200, element_bases + MIN_SPACER * spacer_count)
    total = random.randint(smallest_total, 400)

   
    spacers = [MIN_SPACER] * spacer_count
    for _ in range(total - element_bases - MIN_SPACER * spacer_count):
        spacers[random.randrange(spacer_count)] += 1

    
    chunks = []
    planted = []
    offset = 0
    for gap_size, element in zip(spacers, elements):
        gap = random_bases(gap_size)
        start = offset + len(gap)
        offset = start + len(element)
        planted.append((start, offset - 1))
        chunks.extend([gap, element])
    chunks.append(random_bases(spacers[-1]))
    sequence = [base for chunk in chunks for base in chunk]
    return sequence, planted


def detect_ir(seq, min_distance, k=10):
    s = "".join(seq)
    hits = set()

    for i in range(len(s) - k + 1):
        rc = "".join(COMP[b] for b in reversed(s[i:i + k]))

        for j in range(i + k + min_distance, len(s) - k + 1):
            if s[j:j + k] == rc:
                start, end = i, j + k - 1
                while start > 0 and end < len(s) - 1 and COMP[s[start - 1]] == s[end + 1]:
                    start -= 1
                    end += 1
                hits.add((start, end))

    return sorted(hits)


sequence, planted = make_sequence()

print("Sequence length:", len(sequence))
print("".join(sequence))

print("\nPlanted elements (start, end):")
for start, end in planted:
    print(f"  start={start}, end={end}")

print("\nDetected elements (start, end):")
for start, end in detect_ir(sequence, MIN_DISTANCE, K):
    print(f"  start={start}, end={end}")

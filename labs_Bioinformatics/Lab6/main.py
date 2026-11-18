import random


def random_dna(length):
    return "".join(random.choices("ATGC", k=length))


def reverse_complement(dna):
    pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(pairs[base] for base in reversed(dna))


def create_element():
    left = random_dna(12)
    middle = random_dna(15)
    return left + middle + reverse_complement(left)


dna = ""
positions = []
element_count = random.randint(3, 4)

for _ in range(element_count):
    gap_length = random.randint(15, 25)
    dna += random_dna(gap_length)

    start = len(dna)
    dna += create_element()
    positions.append((start, len(dna) - 1))

total_length = random.randint(max(200, len(dna)), 400)
dna += random_dna(total_length - len(dna))

print("DNA sequence:", dna)
print("Sequence length:", len(dna))

print("\nInserted elements:")
for start, end in positions:
    print(f"Start: {start} End: {end}")

print("\nDetected elements:")
element_length = 12 + 15 + 12

for start in range(len(dna) - element_length + 1):
    window = dna[start:start + element_length]
    left = window[:12]
    right = window[-12:]

    if right == reverse_complement(left):
        end = start + element_length - 1
        print(f"Start: {start} End: {end}")
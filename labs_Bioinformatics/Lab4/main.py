import random
from pathlib import Path


genome = Path(__file__).with_name(
    "sequenceB.txt"
).read_text().strip()


def generate_samples(sequence, count=2000):
    fragments = []

    for _ in range(count):
        size = random.randint(100, 120)
        position = random.randint(
            0, len(sequence) - size
        )

        fragments.append(
            sequence[position:position + size]
        )

    return fragments


def search_overlaps(fragments, minimum):
    index = {}
    overlaps = []
    contained = set()

    for i, fragment in enumerate(fragments):
        for position in range(len(fragment) - minimum + 1):
            key = fragment[position:position + minimum]

            index.setdefault(key, []).append(
                (i, position)
            )

    for j, fragment in enumerate(fragments):
        prefix = fragment[:minimum]

        for i, position in index.get(prefix, []):
            if i == j:
                continue

            suffix = fragments[i][position:]

            if len(suffix) >= len(fragment):
                if suffix.startswith(fragment):
                    contained.add(j)

            elif fragment.startswith(suffix):
                overlaps.append((len(suffix), i, j))

    return overlaps, contained


def reconstruct(fragments, minimum=20):
    fragments = sorted(set(fragments))

    _, contained = search_overlaps(fragments, minimum)

    fragments = [
        fragment
        for i, fragment in enumerate(fragments)
        if i not in contained
    ]

    overlaps, _ = search_overlaps(fragments, minimum)

    next_fragment = {}
    previous_fragment = {}
    parent = list(range(len(fragments)))

    def find_root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]

        return x

    for size, a, b in sorted(overlaps, reverse=True):
        if a in next_fragment or b in previous_fragment:
            continue

        if find_root(a) == find_root(b):
            continue

        next_fragment[a] = (b, size)
        previous_fragment[b] = a
        parent[find_root(a)] = find_root(b)

    results = []

    for i in range(len(fragments)):
        if i in previous_fragment:
            continue

        sequence = fragments[i]
        current = i

        while current in next_fragment:
            current, overlap = next_fragment[current]
            sequence += fragments[current][overlap:]

        results.append(sequence)

    return sorted(results, key=len, reverse=True)


samples = generate_samples(genome)
contigs = reconstruct(samples)

lengths = []
for contig in contigs:
    lengths.append(len(contig))

print("Original genome length:", len(genome))
print("Number of contigs:", len(contigs))
print("Contig lengths:", lengths)

if len(contigs) == 1:
    assembled = contigs[0]
    start = genome.find(assembled)

    if assembled == genome:
        print("Genome successfully reconstructed.")
    elif start == -1:
        print("Reconstruction does not match.")
    else:
        end = start + len(assembled)
        print("Partial reconstruction.")
        print("Missing bases at start:", start)
        print("Missing bases at end:", len(genome) - end)
import math
from pathlib import Path

import matplotlib.pyplot as plt


enzymes = {
    "EcoRI": "gaattc",
    "BamHI": "ggatcc",
    "HindIII": "aagctt",
}

ladder = [10000, 8000, 6000, 5000, 4000, 3000,
          2000, 1500, 1000, 500, 250, 100]


def cut_dna(dna, enzyme):
    cuts = [0]
    site_length = len(enzyme)

    for start in range(len(dna) - site_length + 1):
        if dna[start:start + site_length] == enzyme:
            cuts.append(start + 1)

    cuts.append(len(dna))
    return [end - start for start, end in zip(cuts, cuts[1:])]


def draw_gel(dna, name):
    lanes = {"Ladder": ladder}

    for enzyme_name, site in enzymes.items():
        fragments = cut_dna(dna, site)
        lanes[enzyme_name] = fragments
        print(name, enzyme_name, fragments)

    _, ax = plt.subplots(figsize=(8, 7))
    ax.set_facecolor("black")

    for column, sizes in enumerate(lanes.values()):
        for size in sizes:
            height = math.log10(size)
            ax.hlines(height, column - 0.3, column + 0.3,
                      colors="white", linewidth=4)
            ax.text(column + 0.35, height, str(size),
                    color="cyan", fontsize=8)

    ax.set_xticks(range(len(lanes)), labels=list(lanes))
    ax.set_yticks([])
    ax.set_xlim(-0.6, 4)
    ax.set_title(f"Gel Electrophoresis - {name}")
    plt.show()


folder = Path(__file__).parent

for name in ["sequenceB", "sequenceA"]:
    file_path = folder / f"{name}.txt"
    dna = file_path.read_text().strip().lower()
    draw_gel(dna, name)
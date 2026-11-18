import math
import random
from pathlib import Path

import matplotlib.pyplot as plt


def calculate_position(fragment, a=20, min_h=4):
    return len(fragment) * a / math.log(min_h)


file_path = Path(__file__).with_name("sequence.txt")
genome = file_path.read_text().strip()

fragments = []

for number in range(1, 11):
    start = random.randint(0, 3000)
    size = random.randint(100, 3000)
    end = start + size

    fragment = genome[start:end]
    fragments.append(fragment)
    print(f"Fragment {number} length: {len(fragment)}")

for fragment in fragments:
    position = calculate_position(fragment)
    plt.axhline(y=position, color="blue", linewidth=2)

plt.title("DNA fragment distribution")
plt.ylabel("fragment position")
plt.show()
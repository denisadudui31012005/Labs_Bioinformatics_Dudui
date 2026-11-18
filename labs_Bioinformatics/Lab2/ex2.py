import math
import random
import matplotlib.pyplot as plt


def calculate_temperature(c, g, a, t):
    gc_count = c + g
    length = gc_count + a + t
    gc_percent = (gc_count / length) * 100
    salt_term = 16.6 * math.log10(0.05)

    return 81.5 + salt_term + 0.41 * gc_percent - 600 / length


points = []

for _ in range(9):
    c = random.randint(1, 15)
    g = random.randint(0, 10)
    a = random.randint(1, 10)
    t = random.randint(1, 10)

    average_gc = (c + g) / 2
    temperature = calculate_temperature(c, g, a, t)
    points.append((average_gc, temperature))

gc_values, temperatures = zip(*points)

_, ax = plt.subplots()
ax.plot(gc_values, temperatures, marker="o")
ax.set(
    xlabel="Average G and C count",
    ylabel="Melting temperature",
    title="DNA Melting Temperature",
)
plt.show()
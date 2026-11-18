import matplotlib.pyplot as plt


def compute_t_m(sequence):
    bases = ["C", "G", "A", "T"]
    frequencies = [sequence.count(base) for base in bases]
    c, g, a, t = frequencies

    _, ax = plt.subplots()
    ax.bar(bases, frequencies)
    ax.set(xlabel="Grupare", ylabel="Frecventa")
    plt.show()
    return 4 * (c + g) + 2 * (a + t)


while True:
    sequence = input("Input sequence:\n")
    print(compute_t_m(sequence))
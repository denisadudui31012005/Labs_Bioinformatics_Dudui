import matplotlib.pyplot as plt


def compute_freq(sequence):
    bases = ["C", "G", "A", "T"]
    frequencies = [sequence.count(base) for base in bases]

    _, ax = plt.subplots()
    ax.bar(bases, frequencies)
    ax.set(xlabel="Grupare", ylabel="Frecventa")
    plt.show()


while True:
    sequence = input("Input sequence:\n")
    print(compute_freq(sequence))
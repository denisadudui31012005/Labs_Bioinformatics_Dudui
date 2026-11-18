from collections import Counter
from pathlib import Path
import matplotlib.pyplot as plt
import os
from google import genai
from dotenv import load_dotenv


genetic_code = {
    "uuu": "Phe", "uuc": "Phe",
    "uua": "Leu", "uug": "Leu",
    "cuu": "Leu", "cuc": "Leu",
    "cua": "Leu", "cug": "Leu",
    "auu": "Ile", "auc": "Ile",
    "aua": "Ile", "aug": "Met",
    "guu": "Val", "guc": "Val",
    "gua": "Val", "gug": "Val",
    "ucu": "Ser", "ucc": "Ser",
    "uca": "Ser", "ucg": "Ser",
    "ccu": "Pro", "ccc": "Pro",
    "cca": "Pro", "ccg": "Pro",
    "acu": "Thr", "acc": "Thr",
    "aca": "Thr", "acg": "Thr",
    "gcu": "Ala", "gcc": "Ala",
    "gca": "Ala", "gcg": "Ala",
    "uau": "Tyr", "uac": "Tyr",
    "uaa": "Stop", "uag": "Stop",
    "cau": "His", "cac": "His",
    "caa": "Gln", "cag": "Gln",
    "aau": "Asn", "aac": "Asn",
    "aaa": "Lys", "aag": "Lys",
    "gau": "Asp", "gac": "Asp",
    "gaa": "Glu", "gag": "Glu",
    "ugu": "Cys", "ugc": "Cys",
    "uga": "Stop", "ugg": "Trp",
    "cgu": "Arg", "cgc": "Arg",
    "cga": "Arg", "cgg": "Arg",
    "agu": "Ser", "agc": "Ser",
    "aga": "Arg", "agg": "Arg",
    "ggu": "Gly", "ggc": "Gly",
    "gga": "Gly", "ggg": "Gly"
}


def most_frequent_amino_acids(sequence):
    rna = sequence.lower().replace("t", "u")
    counts = Counter()

    for start in range(len(rna) - 2):
        triplet = rna[start:start + 3]
        if triplet in genetic_code:
            amino_acid = genetic_code[triplet]
            counts[amino_acid] += 1

    return dict(counts.most_common(10))


sequence_path = Path(__file__).with_name("sequenceB.txt")
sequence = sequence_path.read_text().strip()
ranking = most_frequent_amino_acids(sequence)

print("Most frequent amino acids:")
print(ranking)

fig, ax = plt.subplots()
ax.bar(ranking.keys(), ranking.values(), color="orange")
ax.set(
    xlabel="Amino acids",
    ylabel="Frequency",
    title="Amino Acid Distribution",
)
plt.show()

amino_names = ", ".join(ranking)
prompt = (
    "Identify foods containing these amino acids "
    f"and explain their dietary importance: {amino_names}"
)
print(prompt)

load_dotenv()
api_key = os.getenv("API_KEY")

if api_key:
    client = genai.Client(api_key=api_key)
    response = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt,
    )
    print(response.output_text)
else:
    print("No API key provided.")
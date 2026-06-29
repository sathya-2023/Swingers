from pathlib import Path


def load_universe(name):

    file = Path("universes") / f"{name}.txt"

    with open(file, "r") as f:
        stocks = [
            line.strip()
            for line in f.readlines()
            if line.strip()
        ]

    return stocks
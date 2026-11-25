"""Entry for Charm the Commuter: writes the forecast for a city that isn't to /output/entry.txt."""

import os

TEXT = "Brisket-on-Sea: sunny, 24 degrees, light breeze carrying the smell of someone else's bacon. Your train is on time. It is never on time."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

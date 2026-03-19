# Day 19: Pokemon CLI
import sys
import json
import os

# TODO: pip install requests
# import requests

CACHE_DIR = "cache"
API_BASE = "https://pokeapi.co/api/v2/pokemon"


def fetch_pokemon(name):
    """Fetch from PokeAPI or cache."""
    # TODO: Check cache, fetch if needed, handle errors, save to cache
    pass


def display_pokemon(data):
    """Display formatted Pokemon info."""
    # TODO: Extract and print name, id, types, stats with bars, abilities
    pass


def draw_stat_bar(name, value, max_value=255):
    """Draw ASCII stat bar."""
    # TODO: Return "HP:  35  ████████░░░░░░░░"
    pass


def compare_pokemon(name1, name2):
    """Compare two Pokemon side by side."""
    # TODO: Fetch both, display comparison
    pass


def main():
    if len(sys.argv) < 2:
        print("Usage: python pokemon_cli.py <name> [name2]")
        sys.exit(1)
    os.makedirs(CACHE_DIR, exist_ok=True)
    # TODO: Handle single or compare mode


if __name__ == "__main__":
    main()

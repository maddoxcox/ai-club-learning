# Day 12: Package Explorer
# Explore and demo third-party Python packages.

import importlib


def inspect_package(package_name):
    """Inspect an installed package and show its info."""
    # TODO: Import dynamically, show version, main items, docstring
    pass


def demo_requests():
    """Demonstrate the requests library."""
    # TODO: GET request, status codes, JSON parsing, error handling
    pass


def demo_rich():
    """Demonstrate the rich library."""
    # TODO: Console styling, Tables, Panels
    pass


def demo_click():
    """Demonstrate click (note: best as separate script)."""
    print("See click_demo.py for a working click example.")


def python_et_cetera():
    """Demonstrate Python 'et cetera' features."""
    # TODO: List/dict comprehensions, walrus operator, unpacking, f-strings
    pass


def main():
    packages = ["requests", "rich", "click"]
    for pkg in packages:
        inspect_package(pkg)
    demo_requests()
    demo_rich()
    python_et_cetera()


if __name__ == "__main__":
    main()

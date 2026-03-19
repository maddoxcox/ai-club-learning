# Day 5: Test Suite for Grade Calculator
# Run with: pytest test_grade_calculator.py -v

import pytest

# TODO: Import your grade calculator functions
# from day_01_grade_calculator import calculate_gpa, get_grade_input
# (You may need to copy or adjust imports based on your Day 1 code)


# --- Part 1: Basic Tests ---

def test_calculate_gpa_mixed_grades():
    """A, B, C should give 3.0 GPA."""
    # TODO: assert calculate_gpa(["A", "B", "C"]) == 3.0
    pass


def test_calculate_gpa_all_as():
    """All A's should give 4.0 GPA."""
    # TODO
    pass


def test_calculate_gpa_all_fs():
    """All F's should give 0.0 GPA."""
    # TODO
    pass


def test_calculate_gpa_empty_list():
    """Empty grade list should be handled gracefully."""
    # TODO: Should it raise an error? Return 0? Your choice.
    pass


def test_calculate_gpa_single_grade():
    """Single grade should return its point value."""
    # TODO
    pass


# --- Part 2: Edge Case Tests ---

def test_lowercase_grades():
    """Lowercase grades should work (a, b, c)."""
    # TODO
    pass


def test_invalid_grade_raises_error():
    """Invalid grade like 'Z' should raise ValueError."""
    # TODO: Use pytest.raises(ValueError)
    pass


# --- Part 3: TDD Challenge ---
# Write these tests FIRST, then go add +/- support to your grade calculator

def test_a_plus():
    """A+ should equal 4.0."""
    # TODO: assert calculate_gpa(["A+"]) == 4.0
    pass


def test_a_minus():
    """A- should equal 3.7."""
    # TODO
    pass


def test_b_plus():
    """B+ should equal 3.3."""
    # TODO
    pass


def test_mixed_plus_minus():
    """Mix of regular and +/- grades."""
    # TODO
    pass

# Day 1: Grade Calculator
# Build a GPA calculator that handles all bad input gracefully.

# Grade point mapping
GRADE_POINTS = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.4, "B": 3.0, "B-": 2.7,
    "C+": 2.4, "C": 2.0, "C-": 1.7,
    "D+": 1.4, "D": 1.0, "D-": 0.7,
    "F": 0.0,
}


def get_grade(percent):
    """Convert a percentage (0-100) to a letter grade."""
    if percent >= 94.0:
        return "A"
    elif percent >= 90.0:
        return "A-"
    elif percent >= 87.0:
        return "B+"
    elif percent >= 83.0:
        return "B"
    elif percent >= 80.0:
        return "B-"
    elif percent >= 77.0:
        return "C+"
    elif percent >= 73.0:
        return "C"
    elif percent >= 70.0:
        return "C-"
    elif percent >= 67.0:
        return "D+"
    elif percent >= 63.0:
        return "D"
    elif percent >= 60.0:
        return "D-"
    else:
        return "F"


def get_grade_input():
    """Ask the user for a letter grade or percentage. Return the grade or None if they type 'done'."""
    user_input = input("Enter a grade (A+/A/A-/.../F), a percentage, or 'done': ").strip()

    # Check if they want to stop
    if user_input.upper() == "DONE":
        return None

    # Check if it's empty (they just pressed Enter)
    if user_input == "":
        print("  ⚠ You didn't enter anything. Try again.")
        return get_grade_input()

    # Check if they entered a percentage (a number)
    try:
        percent = float(user_input)
        if percent < 0 or percent > 100:
            print(f"  ⚠ {percent} is out of range. Enter a percentage between 0 and 100.")
            return get_grade_input()
        letter = get_grade(percent)
        print(f"  → {percent}% = {letter}  ({GRADE_POINTS[letter]} points)")
        return letter
    except ValueError:
        pass  # Not a number — treat as a letter grade

    # Uppercase for letter grade matching
    user_input = user_input.upper()

    # Check if it's a valid grade
    if user_input not in GRADE_POINTS:
        print(f"  ⚠ '{user_input}' is not a valid grade. Use A+, A, A-, B+, B, B-, C+, C, C-, D+, D, D-, or F.")
        return get_grade_input()

    return user_input


def calculate_gpa(grades):
    """Calculate the GPA from a list of letter grades."""
    if len(grades) == 0:
        raise ValueError("No grades to calculate GPA from.")

    # Convert each letter grade to its point value
    points = [GRADE_POINTS[grade] for grade in grades]

    # Average = sum of all points / number of grades
    return sum(points) / len(points)


def main():
    """Main program loop."""
    grades = []

    print("=== GPA Calculator ===")
    print("Enter your letter grades one at a time.")
    print("Type 'done' when finished.\n")

    try:
        # Keep asking for grades until they type "done"
        while True:
            grade = get_grade_input()

            if grade is None:  # They typed "done"
                break

            grades.append(grade)
            print(f"  ✓ Added {grade} ({GRADE_POINTS[grade]} points). Total grades: {len(grades)}")
            if grade == "F":
                print("  ur cooked 💀")

        # Calculate and display GPA
        try:
            gpa = calculate_gpa(grades)
            print(f"\n{'='*30}")
            print(f"Grades entered: {', '.join(grades)}")
            print(f"Your GPA: {gpa:.2f}")
            print(f"{'='*30}")
        except ValueError as e:
            print(f"\n⚠ {e}")

    except KeyboardInterrupt:
        # Ctrl+C was pressed — exit cleanly instead of showing ugly traceback
        print("\n\nGoodbye!")


if __name__ == "__main__":
    main()

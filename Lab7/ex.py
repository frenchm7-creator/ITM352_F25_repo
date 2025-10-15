"""
Flowchart → Python implementation

Given a student ID (digits only), compute two numbers in the range 1..7:

1) first_num = (sum of all digits in the student ID) % 7 + 1
2) second_num = (product of all *non-zero* digits in the student ID) % 7 + 1

If first_num == second_num, repeatedly "increment" second_num in a circular
manner over 1..7 until they are different, i.e.:
    second_num = (second_num % 7) + 1

Return (first_num, second_num).
"""

from typing import Tuple

def compute_numbers(student_id: str) -> Tuple[int, int]:
    """
    Compute the two numbers as described by the flowchart.

    Args:
        student_id: A string consisting of numeric characters 0-9.
                    Whitespace is allowed around the ID and is ignored.

    Returns:
        A tuple (first_num, second_num), each in the range 1..7.

    Raises:
        ValueError: If the provided student_id contains non-digit characters.
    """
    sid = student_id.strip()
    if not sid.isdigit():
        raise ValueError("student_id must contain digits only")

    # First number: sum of all digits
    digit_sum = sum(int(ch) for ch in sid)
    first_num = (digit_sum % 7) + 1

    # Second number: product of all non-zero digits
    non_zero_digits = [int(ch) for ch in sid if ch != '0']
    # The product of an empty set is 1 (neutral element).
    prod = 1
    for d in non_zero_digits:
        prod *= d
    second_num = (prod % 7) + 1

    # Ensure the two numbers are different by rotating second_num in 1..7
    while second_num == first_num:
        second_num = (second_num % 7) + 1

    return first_num, second_num


def main():
    print("=== Student ID Flowchart Algorithm ===")
    user_input = input("Enter your student ID (digits only): ").strip()
    try:
        a, b = compute_numbers(user_input)
        print(f"first_num:  {a}")
        print(f"second_num: {b}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

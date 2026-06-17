"""
Tests for the Wordle CLI project.

Run from the project root with:  pytest

These tests cover the three functions that hold the game's core logic:
    - is_valid_guess  (input validation)
    - evaluate_guess  (the green / yellow / grey scoring, including the
                       tricky duplicate-letter cases)
    - format_feedback (turning a feedback list into emoji squares)
"""

from project import is_valid_guess, evaluate_guess, format_feedback

# A tiny dictionary used only by the validation tests.
SAMPLE_WORDS = ["apple", "crane", "stare", "abide"]

# Emoji squares, kept here so the expected strings below are easy to read.
GREEN = "\U0001F7E9"
YELLOW = "\U0001F7E8"
WHITE = "\U00002B1C"


def test_is_valid_guess():
    # A real five-letter word in the dictionary is valid.
    assert is_valid_guess("apple", SAMPLE_WORDS) is True
    # Case should not matter.
    assert is_valid_guess("CRANE", SAMPLE_WORDS) is True
    # Wrong length is rejected.
    assert is_valid_guess("cat", SAMPLE_WORDS) is False
    assert is_valid_guess("toolong", SAMPLE_WORDS) is False
    # Non-alphabetic characters are rejected.
    assert is_valid_guess("ab1de", SAMPLE_WORDS) is False
    assert is_valid_guess("ap le", SAMPLE_WORDS) is False
    # A well-formed word that is not in the dictionary is rejected.
    assert is_valid_guess("zzzzz", SAMPLE_WORDS) is False


def test_evaluate_guess():
    # An exact match is all green.
    assert evaluate_guess("crane", "crane") == ["correct"] * 5

    # A guess with no shared letters is all grey.
    assert evaluate_guess("fghij", "crane") == ["absent"] * 5

    # Every right letter in the wrong place is all yellow.
    # "pleat" vs "apple": p, l, e and a all exist but none line up.
    assert evaluate_guess("pleat", "apple") == [
        "present", "present", "present", "present", "absent"
    ]

    # Duplicate-letter rule: answer "abide" has only one 'e'. The guess
    # "eerie" has three e's, but the last one is in the correct spot, so it
    # alone goes green and the other two e's must be grey.
    assert evaluate_guess("eerie", "abide") == [
        "absent", "absent", "absent", "present", "correct"
    ]


def test_format_feedback():
    assert format_feedback(["correct"] * 5) == GREEN * 5
    assert format_feedback(["absent"] * 5) == WHITE * 5
    assert format_feedback(
        ["correct", "absent", "present", "absent", "correct"]
    ) == GREEN + WHITE + YELLOW + WHITE + GREEN

"""
Wordle CLI -- Hult Introduction to Python Final Project
Team: The Avengers

A command-line implementation of the classic word-guessing game Wordle.
The player has six attempts to guess a hidden five-letter word. After each
guess the game reveals, letter by letter, whether each letter is in the
correct position (green), present in the word but in the wrong position
(yellow), or not in the word at all (grey).
"""

import random
import sys

# colorama makes ANSI colour codes work on every platform (including the
# Windows terminal). We import it defensively so that the module can still
# be imported -- and the tests can still run -- even in an environment where
# colorama has not been installed yet. If it is missing we simply fall back
# to plain, uncoloured text.
try:
    from colorama import Back, Fore, Style, init as colorama_init

    colorama_init(autoreset=True)
    COLOR_ENABLED = True
except ImportError:  # pragma: no cover
    COLOR_ENABLED = False


WORD_LENGTH = 5
MAX_ATTEMPTS = 6
WORDS_FILE = "words.txt"


def main():
    """Run the Wordle game loop from start to finish."""
    word_list = load_words(WORDS_FILE)
    answer = choose_answer(word_list)

    print("=" * 29)
    print("        W O R D L E")
    print("=" * 29)
    print(f"Guess the {WORD_LENGTH}-letter word. "
          f"You have {MAX_ATTEMPTS} tries.\n")

    attempts = 0
    while attempts < MAX_ATTEMPTS:
        # Read a guess and keep asking until it is a valid word.
        # Pressing Ctrl+C or Ctrl+D quits the game cleanly instead of
        # dumping a traceback.
        try:
            guess = input(f"Attempt {attempts + 1}/{MAX_ATTEMPTS}: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print(f"\nThanks for playing! The word was '{answer.upper()}'.")
            return

        if not is_valid_guess(guess, word_list):
            print("  Not a valid 5-letter word in the dictionary. Try again.\n")
            continue

        attempts += 1
        feedback = evaluate_guess(guess, answer)
        print("  " + render_guess(guess, feedback))
        print("  " + format_feedback(feedback) + "\n")

        if guess == answer:
            print(f"You got it in {attempts} "
                  f"{'try' if attempts == 1 else 'tries'}! Well played.")
            return

    # The loop ended without a correct guess.
    print(f"Out of attempts! The word was '{answer.upper()}'.")


def load_words(filepath):
    """Read the dictionary file and return a list of lower-case words.

    Only well-formed five-letter alphabetic words are kept, so a stray
    blank line or a typo in the file cannot crash the game.
    """
    words = []
    with open(filepath, encoding="utf-8") as file:
        for line in file:
            word = line.strip().lower()
            if len(word) == WORD_LENGTH and word.isalpha():
                words.append(word)
    if not words:
        sys.exit(f"No valid {WORD_LENGTH}-letter words found in {filepath}.")
    return words


def choose_answer(word_list):
    """Return a single random word to be the hidden answer."""
    return random.choice(word_list)


def is_valid_guess(guess, word_list):
    """Return True if the guess is a legal move.

    A legal guess is exactly WORD_LENGTH letters long, contains only
    alphabetic characters, and exists in the supplied dictionary.
    """
    guess = guess.lower()
    if len(guess) != WORD_LENGTH:
        return False
    if not guess.isalpha():
        return False
    return guess in word_list


def evaluate_guess(guess, answer):
    """Compare a guess to the answer and return per-letter feedback.

    Returns a list with one entry per letter, each being one of:
        "correct" -- right letter in the right position (green)
        "present" -- right letter in the wrong position (yellow)
        "absent"  -- letter is not in the answer at all (grey)

    The function uses two passes so that duplicate letters are scored
    exactly like the real game: a letter is only marked "present" if there
    is still an unmatched copy of it left in the answer. For example, if the
    answer contains a single 'e' but the guess has two, only one of the
    guessed e's can be coloured -- the other must be grey.
    """
    guess = guess.lower()
    answer = answer.lower()
    result = ["absent"] * len(guess)

    # A mutable copy of the answer's letters that we "consume" as we match
    # them, which is what prevents a single answer-letter from being
    # credited twice.
    remaining = list(answer)

    # First pass: mark every exact-position match as correct.
    for i, letter in enumerate(guess):
        if i < len(answer) and letter == answer[i]:
            result[i] = "correct"
            remaining[i] = None

    # Second pass: mark remaining letters that exist elsewhere as present.
    for i, letter in enumerate(guess):
        if result[i] == "correct":
            continue
        if letter in remaining:
            result[i] = "present"
            remaining[remaining.index(letter)] = None

    return result


def format_feedback(feedback):
    """Turn a feedback list into the classic coloured-square string.

    This is the share-style row of emoji squares used by Wordle and is the
    same representation the tests check, since it does not depend on the
    terminal's colour support.
    """
    symbols = {"correct": "\U0001F7E9", "present": "\U0001F7E8", "absent": "\U00002B1C"}
    return "".join(symbols[state] for state in feedback)


def render_guess(guess, feedback):
    """Return the guessed word with each letter colour-coded for the terminal.

    Falls back to plain upper-case text when colorama is unavailable so the
    game never crashes on a colour-less terminal.
    """
    if not COLOR_ENABLED:
        return " ".join(letter.upper() for letter in guess)

    colors = {
        "correct": Back.GREEN + Fore.BLACK,
        "present": Back.YELLOW + Fore.BLACK,
        "absent": Back.WHITE + Fore.BLACK,
    }
    cells = [
        colors[state] + f" {letter.upper()} " + Style.RESET_ALL
        for letter, state in zip(guess, feedback)
    ]
    return "".join(cells)


if __name__ == "__main__":
    main()
 
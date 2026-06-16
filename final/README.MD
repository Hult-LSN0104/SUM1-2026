# WORDLE CLI

#### Video Demo: <URL HERE>

#### Team: The Avengers
#### Deepansh Lather and Dwij Patel
#### Video Link: https://youtu.be/w8p0vmOjcc8

#### Description:

Wordle CLI is a command-line version of the popular word-guessing game
*Wordle*, written entirely in Python. The player is given six attempts to
guess a hidden five-letter word. After every guess the program responds with
colour-coded feedback for each letter: a **green** square means the letter is
correct and in the right position, a **yellow** square means the letter is in
the word but in a different position, and a **grey** square means the letter
does not appear in the word at all. The game ends when the player guesses the
word correctly or runs out of attempts, at which point the answer is revealed.

We chose to build Wordle because, although the game looks simple on the
surface, its scoring logic is deceptively tricky. Getting the feedback exactly
right — especially when a guess or the answer contains repeated letters — is a
genuine programming challenge, and it gave us a clear, well-defined problem to
test thoroughly. It also produces a fun, visual result that demonstrates
nicely on screen.

## Project files

**`project.py`** is the heart of the project. It contains the `main` function
and five supporting functions, all defined at the top level so they can be
imported and tested individually.

- `main()` runs the overall game loop. It loads the dictionary, chooses a
  random answer, prints the banner, and then repeatedly reads guesses until the
  player either wins or exhausts their six attempts. It also catches
  `EOFError` and `KeyboardInterrupt` so that pressing Ctrl+C or Ctrl+D quits
  the program gracefully instead of printing an ugly traceback.

- `load_words(filepath)` reads the dictionary file and returns a list of
  valid words. It deliberately skips any line that is not exactly five
  alphabetic characters, so a blank line or a typo in the word file cannot
  break the game. If no usable words are found it exits with a clear message.

- `choose_answer(word_list)` simply returns one random word from the list to
  serve as the hidden answer for the round.

- `is_valid_guess(guess, word_list)` validates a player's input. A guess is
  only accepted if it is exactly five characters long, contains only letters,
  and exists in the dictionary. This stops the player from "cheating" with
  nonsense input and matches the behaviour of the real game.

- `evaluate_guess(guess, answer)` is the most important function in the
  project. It compares the guess to the answer and returns a list of results,
  one per letter, each being `"correct"`, `"present"`, or `"absent"`.

- `format_feedback(feedback)` converts that list into the familiar row of
  coloured emoji squares.

There is also a helper, `render_guess(guess, feedback)`, which prints the
guessed letters with coloured backgrounds in the terminal using the
`colorama` library, falling back to plain text if colour is unavailable.

**`test_project.py`** contains the automated tests, runnable with `pytest`.
It tests `is_valid_guess`, `evaluate_guess`, and `format_feedback`, including
the difficult duplicate-letter edge cases described below.

**`words.txt`** is the dictionary: a plain-text file of common five-letter
English words, one per line. **`requirements.txt`** lists the single external
dependency, `colorama`.

## Design decisions

The biggest design decision was how to handle **duplicate letters** in
`evaluate_guess`. A naive approach — checking each guessed letter against the
whole answer — gives wrong results when letters repeat. For example, if the
answer is `ABIDE` (one `E`) and the guess is `EERIE` (three `E`s), only the
`E` in the correct final position should turn green; the other two must be
grey, because there is no second `E` to match. We solved this with a
**two-pass algorithm**. The first pass marks all exact-position matches as
correct and "consumes" those letters from a working copy of the answer. The
second pass then marks remaining letters as present only if an unconsumed copy
still exists. This consuming step is what produces the correct, game-accurate
result, and it is the part we are proudest of.

A second decision was to require guesses to be real dictionary words rather
than accepting any five letters. This makes the game fairer and more like the
original, at the cost of being limited by our word list — which can easily be
expanded by adding lines to `words.txt`.

Finally, we returned plain string labels (`"correct"`, etc.) from
`evaluate_guess` rather than colours or symbols directly. This keeps the core
logic independent of how results are displayed, which made the function much
easier to test and would let us swap the display style without touching the
scoring.

## How to run

Install the dependency, then start the game:

```
pip install -r requirements.txt
python project.py
```

To run the test suite from the project root:

```
pytest
```

## Acknowledgements / AI use

Portions of this project were developed with assistance from Claude (Anthropic),
which was used to help structure the code, suggest the two-pass scoring
algorithm, and review the documentation. All code was reviewed, tested, and
understood by the team.

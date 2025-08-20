import random
import math
from collections import Counter
from typing import List, Tuple

class WordleSolver:
    def __init__(self, word_list: List[str], word_length: int = 5, max_guesses: int = 6):
        """Initialize the solver (like a constructor in C++)."""
        self.word_list = word_list
        self.word_length = word_length
        self.max_guesses = max_guesses
        self.possible_words = word_list.copy()
        self.guesses = []
        self.feedbacks = []

    def get_feedback(self, guess: str, target: str) -> str:
        """Generate feedback for a guess against the target word.
        Returns a string of 'G' (green), 'Y' (yellow), 'X' (gray)."""
        feedback = ['X'] * self.word_length
        target_chars = list(target)

        # First pass: Mark green (correct letter, correct position)
        for i in range(self.word_length):
            if guess[i] == target[i]:
                feedback[i] = 'G'
                target_chars[i] = None  # Remove matched letter

        # Second pass: Mark yellow (correct letter, wrong position)
        for i in range(self.word_length):
            if feedback[i] == 'G':
                continue
            if guess[i] in target_chars:
                feedback[i] = 'Y'
                target_chars[target_chars.index(guess[i])] = None

        return ''.join(feedback)

    def is_valid_word(self, word: str, guess: str, feedback: str) -> bool:
        """Check if a word is consistent with the guess and its feedback."""
        # Track required letters (from green/yellow) and their counts
        required_letters = Counter()
        for i in range(self.word_length):
            if feedback[i] in ('G', 'Y'):
                required_letters[guess[i]] += 1

        # Count letters in the candidate word
        word_letters = Counter(word)

        # Ensure all required letters appear with at least the required frequency
        for letter, count in required_letters.items():
            if word_letters[letter] < count:
                return False

        # Check position-specific constraints
        for i in range(self.word_length):
            if feedback[i] == 'G' and word[i] != guess[i]:
                return False  # Must match exactly for green
            if feedback[i] == 'Y' and (guess[i] not in word or word[i] == guess[i]):
                return False  # Must be in word but not in this position for yellow
            if feedback[i] == 'X' and guess[i] in word:
                # For gray, letter can appear only if required by green/yellow elsewhere
                if word_letters[guess[i]] > required_letters[guess[i]]:
                    return False

        return True

    def filter_words(self, guess: str, feedback: str) -> None:
        """Filter possible words based on guess and feedback."""
        self.possible_words = [
            word for word in self.possible_words
            if self.is_valid_word(word, guess, feedback)
        ]
        print(f"After filtering with guess '{guess}' and feedback '{feedback}': {len(self.possible_words)} words remain")

    def choose_guess_random(self) -> str:
        """Choose a random guess from possible words."""
        if not self.possible_words:
            return None
        if len(self.guesses) == 0:
            return "crane"  # Common first guess
        return random.choice(self.possible_words)

    def choose_guess_entropy(self) -> str:
        """Choose a guess based on maximum entropy."""
        if not self.possible_words:
            return None
        if len(self.guesses) == 0:
            return "crane"  # Hardcoded first guess for simplicity

        best_guess = None
        best_entropy = -1

        for guess in self.possible_words:
            pattern_counts = Counter()
            for possible_target in self.possible_words:
                feedback = self.get_feedback(guess, possible_target)
                pattern_counts[feedback] += 1

            total_words = len(self.possible_words)
            entropy = 0
            for count in pattern_counts.values():
                probability = count / total_words
                entropy -= probability * math.log2(probability) if probability > 0 else 0

            if entropy > best_entropy:
                best_entropy = entropy
                best_guess = guess

        return best_guess

    def choose_guess_frequency(self) -> str:
        """Choose a guess based on letter frequency in each position."""
        if not self.possible_words:
            return None
        if len(self.guesses) == 0:
            return "crane"  # Hardcoded first guess

        freq = [Counter() for _ in range(self.word_length)]
        for word in self.possible_words:
            for i, char in enumerate(word):
                freq[i][char] += 1

        best_guess = None
        best_score = -1
        for word in self.possible_words:
            score = 0
            for i, char in enumerate(word):
                score += freq[i][char]
            if score > best_score:
                best_score = score
                best_guess = word

        return best_guess

    def solve(self, target: str, guess_method: str = "random") -> Tuple[bool, int]:
        """Attempt to solve Wordle for the given target word using specified guess method.
        guess_method: 'random', 'entropy', or 'frequency'.
        Returns (solved, number_of_guesses)."""
        self.possible_words = self.word_list.copy()
        self.guesses = []
        self.feedbacks = []

        if guess_method == "random":
            choose_func = self.choose_guess_random
        elif guess_method == "entropy":
            choose_func = self.choose_guess_entropy
        elif guess_method == "frequency":
            choose_func = self.choose_guess_frequency
        else:
            raise ValueError("Invalid guess_method. Use 'random', 'entropy', or 'frequency'.")

        for attempt in range(self.max_guesses):
            guess = choose_func()
            if not guess:
                print(f"No valid guess available at attempt {attempt + 1}. Possible words: {self.possible_words}")
                return False, attempt + 1

            feedback = self.get_feedback(guess, target)
            self.guesses.append(guess)
            self.feedbacks.append(feedback)

            print(f"Guess {attempt + 1}: {guess} -> {feedback} (Method: {guess_method})")

            if feedback == 'G' * self.word_length:
                return True, attempt + 1

            self.filter_words(guess, feedback)

        return False, self.max_guesses

def main():
    # Sample word list
    word_list = ["crane", "house", "smile", "grape", "stone", "flame", "lakes"]

    # Test each guessing method
    target = "smile"
    methods = ["random", "entropy", "frequency"]

    for method in methods:
        print(f"\nTesting {method} method:")
        solver = WordleSolver(word_list)
        solved, attempts = solver.solve(target, guess_method=method)
        if solved:
            print(f"Solved in {attempts} guesses!")
        else:
            print(f"Failed to solve after {attempts} guesses. Final possible words: {solver.possible_words}")

if __name__ == "__main__":
    main()
# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
The purpose of the game is to guess a secret number within a certain range based on hints provided by the game. The player makes guesses and receives feedback on whether their guess is too high, too low, or correct. The game keeps track of the number of attempts and provides a score based on the player's performance.

- [ ] Detail which bugs you found.
1. Hardcoded range in user info message. The message prompting the user to guess a number always said "Guess a number between 1 and 100," even when the settings allowed for different ranges. This could be confusing for players who changed the settings to a different range.

2.The secret number range not updated on new game. When starting a new game, the secret number was generated based on the initial range (1 to 100) and did not update according to the new settings if the user had changed the range. This meant that even if the user changed the settings to a different range, the secret number would still be generated within the original range, making the game inconsistent and potentially unwinnable.

3. The "New Game" button did not reset the game state. When the user clicked the "New Game" button, it only reset the attempts and secret number, but it did not reset the score or the guess history. This could lead to confusion for players starting a new game, as they would see their previous score and history, which should have been cleared for a fresh start.

4. The hints for "Too High" and "Too Low" were reversed. When a guess was higher than the secret number, the hint incorrectly said "Too Low!" and when a guess was lower than the secret number, the hint incorrectly said "Too High!" This could mislead players and make it difficult to win the game.



- [ ] Explain what fixes you applied.
1. I updated the user info message to dynamically reflect the current range based on the settings. Instead of hardcoding the message to always say "Guess a number between 1 and 100," I modified it to display the actual minimum and maximum values from the settings, ensuring that players receive accurate information about the guessing range.

2. I fixed the issue with the secret number not updating by ensuring that when a new game is started, the secret number is generated based on the current range settings. This involved changing the code to use the updated range values when generating the secret number, allowing the game to function correctly regardless of any changes made to the settings.

3. I modified the "New Game" button functionality to reset the entire game state, including the score and guess history, in addition to resetting the attempts and secret number. This ensures that when a player starts a new game, they are presented with a clean slate, free from any previous scores or history that could cause confusion.

4. I corrected the logic for the hints by ensuring that when a guess is higher than the secret number, the hint now correctly says "Too High!" and when a guess is lower than the secret number, the hint now correctly says "Too Low!" This involved reviewing the logic in the code that generates the hints and making sure that the conditions for providing feedback were properly aligned with the intended messages, allowing players to receive accurate feedback on their guesses.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
![game winning screenshot](<Screenshot 2026-03-15 at 5.45.40 PM.png>)


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]

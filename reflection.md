# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game  starts with controls on the main UI and settings on the left sidebar. Main UI has title, make a guess subtitle, input field and 3 buttons. The range of numbers to guess is displayed to be between 1 and 100.

- List at least two concrete bugs you noticed at the start
  (for example: "the hints were backwards").

  1. The hints when guessing were backwards. When a guess is higher than target number, the hint said "Too low!" and when a guess is lower than target number, the hint said "Too high!".
  2. The guess range is hardcoded to be between 1 and 100, but the settings allow the user to change the range. The secret is also not being updated when we change the settings, so the game is stuck in the same guessing range.
  3. The "New Game" button does not reset the game state, so if you click it after the game has started, the score, history doesn't get reset, leaving some wrong information for the new game.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Github copilot for this project


- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

When trying to validate my guess range bug, the AI correctly identified that the guess range was hardcoded and that the secret number was not being updated when the settings were changed. The AI suggested that I should update the secret number whenever the settings are changed, and also suggested that I should use the new range values to validate the user's guess. I verified the result by changing the settings and confirming that the secret number was updated accordingly, and that the game now correctly validated guesses based on the new range.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

The AI missed the fact that the "New Game" button did not reset the game state, including the score and guess history. It suggested that I should only reset the attempts and secret number when starting a new game, but it did not account for resetting the score and history. I verified this by clicking the "New Game" button after playing a round and noticing that the score and history were still present, which could be confusing for players starting a new game.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided a bug was really fixed by testing the specific functionality that was affected by the bug. For example, for the guess range bug, I changed the settings to a different range and then made guesses to see if the hints and validation were working correctly based on the new range. For the "New Game" button bug, I played a round of the game to accumulate some score and history, then clicked "New Game" and checked if the score and history were reset. If the expected behavior occurred after my fix, I considered the bug to be fixed.

- Describe at least one test you ran (manual or using pytest)

I ran a manual test for the guess range bug. I changed the settings to set the minimum guess to 1 and the maximum guess to 50. Then I made a guess of 25, which was within the new range. I observed that the hints were now correctly reflecting whether my guess was too high or too low based on the new range. This confirmed that the bug related to the guess range and hints was fixed.

  and what it showed you about your code.

This test showed me that the code was correctly using the new range values to validate the user's guess and provide accurate hints. It also confirmed that the secret number was being updated when the settings were changed, which was essential for the game to function properly with different ranges.

- Did AI help you design or understand any tests? How?

The AI helped me understand the importance of testing the specific functionality that was affected by the bug. It suggested that I should test the game after making changes to ensure that the bugs were fixed and that no new issues were introduced. The AI also reminded me to consider edge cases, such as what happens when the user changes the settings multiple times or clicks "New Game" after playing a round, which guided me in designing more comprehensive tests for my fixes.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit "reruns" refer to the way Streamlit automatically re-executes the entire script from top to bottom whenever a user interacts with the app, such as clicking a button or changing a setting. This means that any changes in the UI or user input will trigger a rerun of the code, allowing the app to update dynamically based on user interactions. Session state is a way to store and manage data across these reruns. It allows you to keep track of variables and values that need to persist even when the script is rerun, such as user inputs, scores, or game states. By using session state, you can ensure that important information is not lost during reruns and can be accessed and updated as needed throughout the user's interaction with the app.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse in future projects is the practice of thoroughly testing my code after making changes, especially when using AI-generated suggestions. I found that while AI can provide helpful insights and code snippets, it's crucial to validate those changes through testing to ensure they work as intended and don't introduce new bugs. Next time I work with AI on a coding task, I would be more cautious about accepting suggestions without first understanding the underlying logic and potential implications of the changes. This project has made me realize that while AI can be a powerful tool for coding, it is not infallible and requires careful consideration and validation to ensure that the generated code is correct and effective.

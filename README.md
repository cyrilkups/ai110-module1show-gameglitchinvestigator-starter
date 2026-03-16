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

- Game purpose: This project is a Streamlit number-guessing game where the player tries to find a secret number within a limited number of attempts.

- Bugs found: The secret and game flow were unstable across reruns, the higher/lower hints were backwards, the app mixed string and integer comparisons, and New Game did not fully reset gameplay state.

- Fixes applied: I moved reusable logic into `logic_utils.py`, kept the secret value numeric on every turn, corrected the higher/lower hint messages, fixed the attempt counter, and reset the key game fields (`secret`, `status`, `history`, and `attempts`) on New Game.

## 📸 Demo

Winning game after the repairs:

![Winning game after the fixes](assets/demo-winning-game.png)


Challenge 1: Advanced Edge-Case Testing

I added edge-case tests for three inputs that could still trip up the game: negative integers, negative decimals, and extremely large numeric values. The expanded pytest suite verifies that `parse_guess` accepts those inputs without crashing and that the game logic still returns the correct higher/lower hint for a huge guess.

![Pytest command and passing edge-case test results](assets/pytest-results.png)

## 🚀 Stretch Features

Feature expansion completed: I added a persistent high-score tracker that saves the best finished round to `.streamlit/high_score.json` and shows it in the sidebar every time the app loads.

The agent contribution was in planning the split of responsibilities: the AI agent proposed keeping file I/O in `logic_utils.py` while `app.py` handled only Streamlit state and rendering. I still verified the behavior myself with pytest coverage for missing files, invalid score data, and "only save if the new score is better" logic.

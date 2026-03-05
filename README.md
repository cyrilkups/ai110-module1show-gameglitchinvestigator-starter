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
A Streamlit number-guessing game where the player tries to guess a secret number within a limited number of attempts.

- [ ] Detail which bugs you found.
Secret/state behavior was unstable across reruns, higher/lower hint logic was incorrect, and New Game did not fully reset gameplay state.

- [ ] Explain what fixes you applied.
st.session_state, corrected guess/hint logic (moved to logic_utils.py), and reset key fields (secret, status, history, attempts) on New Game.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

![alt text](<Screenshot 2026-03-04 at 9.54.13 PM.png>)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]

# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
it looked like a simple Streamlit guessing game with a difficulty selector, guess input, submit/new-game buttons, score/attempt info, and a debug panel showing the secret number.

- List at least two concrete bugs you noticed at the start  (for example: "the secret number kept changing" or "the hints were backwards").

* The higher/lower hints were backwards (too high said “go higher,” too low said “go lower”).
* The game state logic was inconsistent, and its  behavior changed across attempts (including type-mixing around the secret value).
* New Game did not fully reset all state, so after win/loss the app could stay stuck.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude, GPT

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI suggested refactoring reusable game logic out of app.py and into logic_utils.py (for example: get_range_for_difficulty, parse_guess, update_score, and check_guess), then importing those functions back into the Streamlit app. This suggestion was correct because it separated UI from logic and made the code easier to test and debug.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
An AI-generated approach mixed data types for the secret value (converting it to a string on some attempts and comparing string/int values), which was meant to “handle” comparison issues. This was incorrect/misleading because it caused inconsistent higher/lower behavior and can produce wrong comparisons.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I treated a bug as fixed only when I could reproduce the old issue, apply the change, and then fail to reproduce it. I also checked that the fix did not break other gameplay behavior.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran `../.venv/bin/python -m pytest -q` and got `18 passed`. That confirmed the core logic functions (`check_guess`, `parse_guess`, `update_score`, `get_range_for_difficulty`) matched expected behavior.
- Did AI help you design or understand any tests? How?
Yes. AI helped map game rules into testable functions and suggested edge cases like invalid input and unknown difficulty defaults.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
Because Streamlit reruns the script on each interaction, and the secret was being recomputed instead of persisted in session state.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Reruns mean your script starts from top to bottom again whenever the user clicks or types. `st.session_state` is the place to store values you want to survive those reruns.
- What change did you make that finally gave the game a stable secret number?
I initialized `st.session_state.secret` only once (when missing) and reset it only on New Game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I want to keep separating UI code from logic code early, then test the logic with pytest.
- What is one thing you would do differently next time you work with AI on a coding task?
I would validate AI suggestions with small tests immediately before integrating them into the main flow.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
It reinforced that AI output is a draft, not a final answer. I now treat AI as a collaborator whose code must be verified with debugging and tests.

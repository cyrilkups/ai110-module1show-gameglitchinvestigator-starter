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
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

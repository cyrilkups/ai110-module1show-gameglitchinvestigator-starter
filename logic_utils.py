import json
from pathlib import Path


HIGH_SCORE_FILE = Path(__file__).resolve().parent / ".streamlit" / "high_score.json"


def _default_high_score():
    return {"score": 0, "difficulty": "", "attempts": 0}


#FIX: AI and I moved reusable difficulty logic out of app.py.
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


#FIX: AI and I moved input parsing logic out of app.py for testing.
def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


#FIX: AI and I moved guess-check logic out of app.py for isolation.
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    guess = int(guess)
    secret = int(secret)

    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        # FIXME (resolved): this branch used to tell a high guess to go higher.
        #FIX: AI and I corrected the hint direction and normalized values to ints.
        return "Too High", "📉 Go LOWER!"

    # FIXME (resolved): this branch used to tell a low guess to go lower.
    #FIX: AI and I corrected the low-guess hint text so it guides the player up.
    return "Too Low", "📈 Go HIGHER!"


#FIX: AI and I moved score updates out of app.py for reuse.
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


#FEATURE: AI agent helped plan a file-backed high score flow so persistence
# lives in logic_utils.py and the Streamlit app can stay focused on UI state.
def load_high_score(path=HIGH_SCORE_FILE):
    """Load the saved high score record from disk."""
    score_path = Path(path)

    if not score_path.exists():
        return _default_high_score()

    try:
        payload = json.loads(score_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, TypeError):
        return _default_high_score()

    try:
        score = max(int(payload.get("score", 0)), 0)
        attempts = max(int(payload.get("attempts", 0)), 0)
    except (TypeError, ValueError, AttributeError):
        return _default_high_score()

    difficulty = payload.get("difficulty", "")
    if not isinstance(difficulty, str):
        difficulty = ""

    return {
        "score": score,
        "difficulty": difficulty,
        "attempts": attempts,
    }


def save_high_score(record, path=HIGH_SCORE_FILE):
    """Persist a high score record to disk and return the saved payload."""
    payload = {
        "score": max(int(record.get("score", 0)), 0),
        "difficulty": str(record.get("difficulty", "")),
        "attempts": max(int(record.get("attempts", 0)), 0),
    }
    score_path = Path(path)
    score_path.parent.mkdir(parents=True, exist_ok=True)
    score_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return payload


def record_high_score(score: int, difficulty: str, attempts: int, path=HIGH_SCORE_FILE):
    """Save a new high score if it beats the stored record."""
    current = load_high_score(path)
    candidate = {
        "score": max(int(score), 0),
        "difficulty": difficulty,
        "attempts": max(int(attempts), 0),
    }

    if candidate["score"] > current["score"]:
        return save_high_score(candidate, path), True

    return current, False

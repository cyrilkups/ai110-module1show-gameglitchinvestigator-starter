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

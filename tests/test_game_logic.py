from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score


# --- check_guess ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- parse_guess ---

def test_parse_guess_valid_int():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_valid_float_truncates():
    ok, value, err = parse_guess("7.9")
    assert ok is True
    assert value == 7

def test_parse_guess_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_guess_none():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None

def test_parse_guess_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None


# --- get_range_for_difficulty ---

def test_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)

def test_range_hard():
    assert get_range_for_difficulty("Hard") == (1, 50)

def test_range_unknown_defaults_to_normal():
    assert get_range_for_difficulty("Unknown") == (1, 100)


# --- update_score ---

def test_update_score_win_early():
    # attempt 1: points = 100 - 10*(1+1) = 80
    assert update_score(0, "Win", 1) == 80

def test_update_score_win_minimum_points():
    # attempt 10: points = 100 - 10*11 = -10, clamped to 10
    assert update_score(0, "Win", 10) == 10

def test_update_score_too_high_even_attempt():
    assert update_score(50, "Too High", 2) == 55

def test_update_score_too_high_odd_attempt():
    assert update_score(50, "Too High", 3) == 45

def test_update_score_too_low():
    assert update_score(50, "Too Low", 1) == 45

def test_update_score_unknown_outcome():
    assert update_score(50, "Other", 1) == 50

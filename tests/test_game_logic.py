import pytest

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    load_high_score,
    parse_guess,
    record_high_score,
    save_high_score,
    update_score,
)


# --- check_guess ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_guess_handles_numeric_string_secret():
    outcome, message = check_guess(100, "50")
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


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


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("-15", -15),
        ("-3.8", -3),
        ("999999999999999999999999", 999999999999999999999999),
    ],
)
def test_parse_guess_edge_case_inputs(raw, expected):
    ok, value, err = parse_guess(raw)
    assert ok is True
    assert value == expected
    assert err is None


def test_check_guess_handles_extremely_large_guess():
    outcome, message = check_guess(999999999999999999999999, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


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


# --- high score persistence ---

def test_load_high_score_missing_file(tmp_path):
    record = load_high_score(tmp_path / "missing.json")
    assert record == {"score": 0, "difficulty": "", "attempts": 0}


def test_save_high_score_round_trip(tmp_path):
    path = tmp_path / "high_score.json"
    saved = save_high_score(
        {"score": 85, "difficulty": "Hard", "attempts": 2},
        path,
    )

    assert saved == {"score": 85, "difficulty": "Hard", "attempts": 2}
    assert load_high_score(path) == saved


def test_record_high_score_saves_only_when_score_improves(tmp_path):
    path = tmp_path / "high_score.json"

    first_record, first_is_new = record_high_score(80, "Normal", 1, path)
    second_record, second_is_new = record_high_score(60, "Easy", 1, path)

    assert first_is_new is True
    assert first_record == {"score": 80, "difficulty": "Normal", "attempts": 1}
    assert second_is_new is False
    assert second_record == first_record


def test_load_high_score_invalid_file_falls_back_to_default(tmp_path):
    path = tmp_path / "high_score.json"
    path.write_text("not json", encoding="utf-8")

    record = load_high_score(path)

    assert record == {"score": 0, "difficulty": "", "attempts": 0}

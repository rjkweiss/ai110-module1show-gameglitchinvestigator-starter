from logic_utils import check_guess, update_score


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")


def test_guess_too_high():
    # If secret is 50 and guess is 60, should return "Too High" with correct hint to go lower
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")


def test_guess_too_low():
    # If secret is 50 and guess is 40, should return "Too Low" with correct hint to go higher
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")


def test_update_score_win():
    # Winning on attempt 1 should add points (100 - 10*2 = 80)
    new_score = update_score(0, "Win", 1)
    assert new_score == 80


def test_update_score_too_high_even_attempt():
    # "Too High" on even attempt (e.g., 2) should add 5 points (buggy behavior)
    new_score = update_score(10, "Too High", 2)
    assert new_score == 15


def test_update_score_too_high_odd_attempt():
    # "Too High" on odd attempt (e.g., 1) should subtract 5 points
    new_score = update_score(10, "Too High", 1)
    assert new_score == 5


def test_update_score_too_low():
    # "Too Low" should always subtract 5 points
    new_score = update_score(10, "Too Low", 1)
    assert new_score == 5

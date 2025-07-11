# pytest code goes here
from bowling_game import calculate_scores_scenario_one, calculate_scores_scenario_two, calculate_scores_scenario_three, calculate_scores_scenario_four, calculate_scores_scenario_five

# Assume a frame of two balls is recorded as "[a, b]" where a+b <=10
# Assume a spare is recorded as "[c, d]" where c+d = 10
# Assume a strike is recorded as "[10, 0]"

# (1) Bowler has a _Gutter_ game of all misses
#     - `-/- -/- -/- -/- -/- -/- -/- -/- -/- -/- = 0`
def test_calculate_scores_will_return_zero_for_a_gutter_game():
    # arrange
    expected = 0
    scores = [ [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0] ]
    # act
    actual = calculate_scores_scenario_one(scores)
    # assert
    assert actual == expected, f'expected scores to be "{expected}" from scores of {scores}, but was "{actual}"'

# (2) Bowler throws _All ones_
#   - `1/1 1/1 1/1 1/1 1/1 1/1 1/1 1/1 1/1 1/1 = 20`
def test_calculate_scores_will_return_20_for_a_1s_game():
    # arrange
    expected = 20
    scores = [ [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1] ]
    # act
    actual = calculate_scores_scenario_two(scores)
    # assert
    assert actual == expected, f'expected scores to be "{expected}" from scores of {scores}, but was "{actual}"'

# (3) Bowler gets a _Spare_
#   - `5/5 3/- -/- -/- -/- -/- -/- -/- -/- -/- = 16`
def test_calculate_scores_will_add_spare_to_previous_score():
    # arrange
    expected = 16
    scores = [ [5, 5], [3, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0] ]
    # act
    actual = calculate_scores_scenario_three(scores)
    # assert
    assert actual == expected, f'expected scores to be "{expected}" from scores of {scores}, but was "{actual}"'

# (4) Bowler gets a _Strike_
#   - `10/ 3/4 -/- -/- -/- -/- -/- -/- -/- -/- = 24`
def test_calculate_scores_will_add_next_frame_for_strike():
    # arrange
    expected = 24
    scores = [ [10, 0], [3, 4], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0] ]
    # act
    actual = calculate_scores_scenario_four(scores)
    # assert
    assert actual == expected, f'expected scores to be "{expected}" from scores of {scores}, but was "{actual}"'

# (5) Bowler gets a _Perfect Game_
#   - `10/ 10/ 10/ 10/ 10/ 10/ 10/ 10/ 10/ 10/ = 300`
def test_calculate_scores_will_return_300_for_a_perfect_game():
    # arrange
    expected = 300 # as this is 30 pts x 10 bowls!
    # if you get a strike you get two more balls scored...
    # ...so a perfect game is actually 12 balls, each a strike!
    # so we add a bonus [10, 10] for the extra two balls at the end
    scores = [ [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 10] ]
    # act
    actual = calculate_scores_scenario_five(scores)
    # assert
    assert actual == expected, f'expected scores to be "{expected}" from scores of {scores}, but was "{actual}"'

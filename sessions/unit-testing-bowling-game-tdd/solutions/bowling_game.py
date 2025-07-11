# bowling game code goes here

#
# Note - these should all be a single function in the exercises folks do :-)
# Here we separate the out to show the stages :-)
#

# Assume a frame of two balls is recorded as "[a, b]" where a+b <=10
# Assume a spare is recorded as "[c, d]" where c+d = 10
# Assume a strike is recorded as "[10, 0]"

# (1) Bowler has a _Gutter_ game of all misses
#     - `-/- -/- -/- -/- -/- -/- -/- -/- -/- -/- = 0`
# (2) Bowler throws _All ones_
#   - `1/1 1/1 1/1 1/1 1/1 1/1 1/1 1/1 1/1 1/1 = 20`
# (3) Bowler gets a _Spare_
#   - `5/5 3/- -/- -/- -/- -/- -/- -/- -/- -/- = 16`
# (4) Bowler gets a _Strike_
#   - `10/ 3/4 -/- -/- -/- -/- -/- -/- -/- -/- = 24`
# (5) Bowler gets a _Perfect Game_
#   - `10/ 10/ 10/ 10/ 10/ 10/ 10/ 10/ 10/ 10/ = 300`

def calculate_scores_scenario_one(frame_list):
    return 0

def calculate_scores_scenario_two(frame_list):
    total = 0
    for frame in frame_list:
        for ball in frame:
            total += ball
    return total

def is_spare(frame):
    return frame[0] + frame[1] == 10

def calculate_scores_scenario_three(frame_list):
    total = 0
    num_frames = len(frame_list)
    for frame_index, frame in enumerate(frame_list):
        frame_score = frame[0] + frame[1]

        if (is_spare(frame) and frame_index < num_frames):
            next_ball_score = frame_list[frame_index +1][0]
            frame_score += next_ball_score

        total += frame_score

    return total

def is_strike(frame):
    return frame[0] == 10 and frame[1] == 0

def calculate_scores_scenario_four(frame_list):
    total = 0
    num_frames = len(frame_list)
    for frame_index, frame in enumerate(frame_list):
        frame_score = frame[0] + frame[1]

        if (is_strike(frame) and frame_index < num_frames):
            next_frame = frame_list[frame_index +1]
            next_frame_score = next_frame[0] + next_frame[1]
            frame_score += next_frame_score

        elif (is_spare(frame) and frame_index < num_frames):
            next_ball_score = frame_list[frame_index +1][0]
            frame_score += next_ball_score

        total += frame_score

    return total

def calculate_scores_scenario_five(frame_list):
    total = 0
    max_frame_index = 9 # as max frames = 10

    for frame_index, frame in enumerate(frame_list):
        frame_score = 0
        if (frame_index <= max_frame_index):
            frame_score += (frame[0] + frame[1])

        if (is_strike(frame) and frame_index <= max_frame_index):
            next_frame = frame_list[frame_index +1]
            next_frame_score = next_frame[0] + next_frame[1]
            frame_score += next_frame_score
            if (is_strike(next_frame) and frame_index <= 9):
                # also need a ball from the next next frame
                next_next_frame = next_frame = frame_list[frame_index +1]
                frame_score += next_next_frame[0]

        elif (is_spare(frame) and frame_index < max_frame_index):
            next_ball_score = frame_list[frame_index +1][0]
            frame_score += next_ball_score

        total += frame_score

    return total

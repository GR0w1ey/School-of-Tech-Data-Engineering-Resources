# Unit-Testing 2

This module builds from `unit-testing-1` with the addition of Mocking and Stubbing with Dependency Injection.

## Related sessions

1. [unit-testing-1 intro](../unit-testing-1/README.md)
1. [unit-testing-2 stubs & mocks](../unit-testing-2/README.md) (this one)
1. [unit-testing-3 patching](../unit-testing-3/README.md)
1. [unit-testing-bowling-game-tdd](../unit-testing-bowling-game-tdd/README.md)

## Overview

- Dependency Injection
- Mocking
- Intro to `Mock()`

## Timings

- This session is timetabled for 2 blocks at 1.5 hrs each, i.e. 0.5 elapsed training days
- The formative assessments occur during this and are included in that timing
- The exercises for this session (done in breakouts) are also included in that time

## Assessments

To check the learner progress in this session we have:

- Follow-along exercises
- Discussions
- Breakout room exercises

## Prep

- Create the session files (pdf and zip) using `make generate-session-files f=module_name`
- Review the slides and exercises
- Familiarise yourself with the concept of DI if you're not already.

## Session

- Deliver `unit-testing-1` first
- Deliver presentation and distribute as `PDF` to learners
- Present and distribute exercise to learners

### Exercises

The exercise provides learners with some working code which calls a countries api to get some `JSON` data. The intention is for them to refactor the code to make use of `DI` and write some simple unit-tests. This will require them to do some mocking and stubbing.

`./exercises/solution.py` contains a happy path + common case solution.

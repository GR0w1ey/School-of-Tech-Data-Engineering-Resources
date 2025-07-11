# Source Control with Git

NOTE: All the git kata sessions use the source-control-git folder too. See [README-git-katas.md](README-git-katas.md)

## Overview

- Source Control
- Git
- Sharing Code with git
- Branching
- Pull Requests

## Timings

- This session is timetabled for 3 blocks at 1.5 hrs each (0.75 days)
- The formative assessments occur during this and are included in that timing
- The exercises for this session (done in session) are also included in that time

## Assessments

To check the learner progress in this session we have:

- Exercise on installing and configuring git
- Exercise on joining and using git organisations
- Exercise on cloning git repos
- Exercises on add, commit and push
- Multiple quizzes on git commands
- Emoji checks
- Quizzes

## Prep

In addition to the usual prep steps for other sessions, this session involves using a GitHub organisation for learners to use for their repositories throughout the whole programme.

This organisation will be configured so that learners cannot see each other's repositories. This is to encourage confidence in the learners to experiment. In the first half of the programme while working on their mini projects, learners are encouraged to collaborate through screen sharing and vocal feedback.

For the group projects, teams can be made within the organisation to allow the learners to collaborate on the same repository.

### Generation specific prep (in GitHub)

- Create a new GitHub organisation for your cohort named `academy-COHORT-NUM`, e.g. `generation-de-lon9`
- Change the permissions for members of the organisation by navigating to:
    - Organisation Settings -> Member privileges
    - Set "Base permissions" -> "No permission"
- Enforce 2FA for all members of the GitHub Org:
    - In your org, goto "Settings" -> "Authentication Security"
    - Enable "Require two-factor authentication"
- Create a new _private_ shared repository for your cohort in your new organisation by navigating to [infinityworks/academy-source-control-template](https://github.com/infinityworks/academy-source-control-template) and clicking 'use this template'
    - Give it a name, e.g. `source-control-practice`

### SoT specific prep (in GitHub)

- Add all instructors to the [IW-Academy/instructors](https://github.com/orgs/IW-Academy/teams/instructors) team
- Create a new _private_ repository for your cohort in your new organisation by navigating to [IW-Academy/github-demo-session-template](https://github.com/IW-Academy/github-demo-session-template) and clicking 'use this template'
    - Give it a name, e.g. `source-control-practice`

### Common prep (in GitHub)

- Create a team in your organisation called `full-cohort`
    - Add all the instructors to this team straight away: Select the team, click on the "Members" tab, click on the "Add a Member" green button, repeat for each instructor.
    - Add all learners as soon as you can
- In your custom repo from above
    - Give the team `full-cohort` **maintain** permission to this repo: Click on the "settings" tab for the repository, Click on the "Collaborators and teams" menu item, then in the "Manage access" section click on the "Add teams" button.

### Session delivery prep

- Create the kata PDFs using `make generate-git-katas`
- Create the session files (pdf and zip) using `make generate-session-files f=module_name`
- Review the slides and exercises
- The cheatsheet MD files can be viewed in the IDE once unzipped.

During the session itself, learners will be prompted to create a GitHub account. You will then need to invite each learner to the team `full-cohort` as they do so, which will also invite them to the organisation

- When you get to this point in the session, invite all learners by email address to the `full-cohort` Team
    - For Generation, these emails are in SalesForce

## Session

1. Distribute the git cheat sheet at the start - this is a handy reference.
1. Run the presentation.
1. Once you reach the `Exercise - Set up a GitHub account` section lead the cohort through each step.
    1. Remind them to set 2FA
1. Once you reach the `Exercise - Join a GitHub organisation` section:
    1. Invite all learners to the `full-cohort` team by email
        - This is easier than getting all the GitHub IDs.
    1. Share the link to the organisation with the learners and prompt them to accept the invitations.
1. Once you reach the `Exercise - Clone a repository` section lead the cohort to clone the `source-control-practice` repository you made above.
1. Once you reach the `Exercise - Our first branch` section lead the cohort through each step and the next sections for creating a PR and merging into main
    1. Make sure each learner creates a uniquely named file for their changes or you will end up stuck with resolving a zillion merge conflicts
1. Once you reach the `Exercise - new repository` section lead the cohort to make a new private repository that they will use for their mini-project.

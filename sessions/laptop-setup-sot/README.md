# Laptop Setup (SoT)

> This is for School of Tech only, lots of the content here is Accenture specific.

## Objectives

- Have the right software needed to be a consultant
- Have two-factor-authentication (2FA) enabled on your GitHub
- Be able to sign into your Accenture email addresses

## Prep

- Export the presentation to PDF and the zip for distribution using `make generate-session-files f=session_name`
- The I.T. dept will need to have got their laptops and Google account details prepped
- Ensure that at least one instructor is familiar with the install processes for each platform in use - for example if none of you use MacOS but half the academy do check you know how to install node.
- Ensure you have links handy for the intranet, handbook, and the mandatory training they will need to complete.

### For Mac users (if there are any)

An up to date `Brewfile` can be created from an instructors machine using `brew bundle dump` - do this on a healthy reference mac, or clean up the output.

Save this at [laptop-setup/examples/Brewfile](./examples/Brewfile).

## GitHub: Security and Sensitive info

- The course contains sensitive and proprietary material
- All individual Academite and Team projects *must* go in the IW-Academy org
- No use of personal github repos is allowed, at all, for work
- You can use personal repos for other things
- To get into the IW-Academy org you will need your Primary email during that to be one where the principal matches your SSO, so Accenture email.
- You GitHub account can then be registered (back to) to your personal email, if you wish.

### Required environment variables

- We need some environment variables saved in our `~/.zshrc` (MacOS / Unix) `~/.bashrc` (Windows / WSL2) files
- Instructors: This is is from the outputs of [academy-core-infra](https://github.com/infinityworks/academy-core-infra) - run the cdk up to date with `make cdk-all-and-vars` and then share [env-vars.txt](https://github.com/infinityworks/academy-core-infra/blob/main/cdk/env-vars.txt)

## Session

> For this session it is best if we split into those using Macs & Unix, those on Windows using WSL2.
> Instructors to organise

1. This session works best if one learner is used as a guinea pig
    1. Get one learner to screenshare the entire process under close supervision
    1. Get all the other learners to follow along slowly with each step
1. This is a very hands on session, especially if academites have chosen laptops running OSs they are unfamiliar with!
1. Encourage them to help each other out.
1. Any that get finished quickly can make a start on the mandatory training modules, others will have to slot them in over the following days.

## Windows WSL2

For anyone on a Windows machine we recommend using WSL2 for all aspects of the course (i.e. use Unix not Windows!).

Further notes for installing WSL and troubleshooting any issues are included in the session slides.

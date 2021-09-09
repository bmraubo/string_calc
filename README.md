# string_calc
CI-backed String Calculator Kata

## Instructions

## Brief

### Functional Requirements

- Complete the first 5 steps of the [String Calculator kata](https://osherove.com/tdd-kata-1), validated with a passing test suite.

### Non-Functional Requirements

- Code is implemented using the Red-Green-Refactor technique.
- Each step of the String Calculator kata should be developed in a separate branch and merged in to the `main` branch via a pull request.
- The repo provides instructions for a user to clone and run locally, with tests. Do not assume the user has strong experience in the language you'll be working in.
- A CI pipeline, which runs the application tests as part of branch pushes and merge requests, is up and running _before_ the first code pull request is filed.
- The repo is set to block merges to `main` unless the pipelines are passing.

### Languages / Tools

- The apprentice is free to use whatever language they prefer, ideally the language they feel most comfortable with (likely to be the one used for their 8th Light application)
- Any test runner is acceptable
- The apprentice should not need to bring in other dependencies at this stage

 ### Learning Objectives

This is more of a process exercise than a programming one, with the learning objectives designed to give you a solid foundation for all apprenticeship projects at 8th Light:

- Familiarity with Git branching, merging and code review
- Introduction to the concept of a walking skeleton
- Understand the basics of continuous integration and why it's useful

## Comments

### Requirements and Setup

### Tests

### Continuous Integration

### Walking Skeleton

### GitHub Actions/Automation

The requirements are that each pull request is automatically tested, and cannot be merged unless the tests are passed.

The starting point would be a test file with no tests. The first pull request would include the basic tests, as well as the features tested - however the framework would already be in place, satisfying the brief requirements. 

This has the added benefit of expending the number of tests done with each pull request automatically.

Had a dummy moment here - I could not figure out the relationship of checks to statuses and almost went down the road of making API status calls. The issue was that I was trying to find a status that referred to 'CI' the name of the check or tests.yml. The correct status was 'build' the name of the job within the yml file. That only took best part of 2 hours. 
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
- A CI pipeline, which runs the application tests as part of branch pushes and merge requests, is up and running _before_ the first code pull request is filed. *DONE*
- The repo is set to block merges to `main` unless the pipelines are passing. *DONE*

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

### Steps

#### Step 1

Create a simple String calculator with a method signature:

`int Add(string numbers)`

The method can take up to two numbers, separated by commas, and will return their sum. 

for example “” or “1” or “1,2” as inputs.

(for an empty string it will return 0)

Tests created for empty string and string with two values

This is simple enough - empty strings have to return 0, if not empty the string has to be split according to the delimiter and the totals added up. As the returned numbers will be strings, the split list is run through a for loop which adds the integer value to the answer variable, returning that variable once the loop is complete.

### Step 2

Allow strings with unknown number of values

Tests: string with 4 and 10 values

So the splitting of the string according to the delimiter will allow for any amount of numbers to be handled - no changes to the code necessary - tests all pass. Woops.

### Step 3

Allow for the use of the '\n' delimiter alongside ','

Added tests that include only the '\n' delimiter, as well as a combination of both.

I added a `.replace('\n',',')` before the string is split replace all new lines with commas. The rest of the code is unaffected.


### Red/Green/Refactor

RGR is a concept of Test Driven Development. It relies on tests being written in order to guide the development of the application as a first step in the process. These tests will inevitably fail, as there is no code written to allow them to pass (thus red - fail).

Once the test is ready, the code is written that allows it to pass (check goes Green).

The tested code can then be refactored - any changes will return us to the start of the cycle, where the code is worked on until the test succeeds again. Repeat.

### Continuous Integration

Continuous integration is the practice of merging all changes into the main branch on a regular basis - ranging from once a day to several times a day. This reduces the risk of integration conflicts on merge as there is less opportunity for the working branch to drift away from the main over time due to commits by other developers. 

The CI process can be heavily automated - in this case the merge process is streamlined by the addition of tests, with the merge being contingent on the successful passage of those tests. 

CI covers the build/test/merge part of the process and can be extended further through continuous delivery (where the code in the main branch is checked as to be be immediately deployable to users) and continuous deployment, where the deployment process is also automated. 

### Walking Skeleton

Walking skeletons are similar to the Tracer Bullet concept. The purpose is to figure out the general inter-connectivity of the application at the start in order to detect problems early and have a general framework on which to base further development. Walking skeletons have to be functional - "a tiny implementation of the system that performs a small end-to-end function". 

For example: a simple, functional query to the database - it will not have all the final functionality, but it is sufficient to demonstrate that the query works and the application can communicate wit the database. 

In the current scenario, the end-result is simple enough that Step 1 of the Kata effectively acts as the walking skeleton. 

### GitHub Actions/Automation

The requirements are that each pull request is automatically tested, and cannot be merged unless the tests are passed. *(this is now satisfied)*

The starting point would be a test file with no tests. The first pull request would include the tests for step 1, as well as the features tested - however the framework would already be in place, satisfying the brief requirements. 

This has the added benefit of expending the number of tests done with each pull request automatically.

Had a dummy moment here - I could not figure out the relationship of checks to statuses and almost went down the road of making API status calls. The issue was that I was trying to find a status that referred to 'CI' the name of the check or tests.yml. The correct status was 'build' the name of the job within the yml file. That only took best part of 2 hours - how silly. 
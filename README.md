# string_calc
CI-backed String Calculator Kata

- [Instructions](#Instructions)
- [Brief](#Brief)
- [Comments](#Comments)
    - [Steps](#Steps)
    - [Red/Green/Refactor](#Red/Green/Refactor)
    - [Continuous Integration](#Continuous_Integration)
    - [Walking Skeleton](#Walking_Skeleton)
    - [GitHub Actions/Automation](#GitHub_Actions/Automation)

## Instructions

This application requires Python 3.8.2.

If you have Git installed:

```
#clone the repository

$ git clone https://github.com/bmraubo/string_calc.git`
```

If you do not have Git installed, you can download a zipped copy, which can be unzipped into a folder of your choice. 

Once you have a local copy of the repository:

```
# go into the repository
$ cd string_calc

# run the application
$ python kata.py

# to run all tests
$ python -m unittest test_kata.py

```

Downloading the zipped repository and unzip it into a folder of your choice. Then use terminal to navigate to the folder and use command `python kata.py`.

The tests can be run by navigating to the folder containing the repository and using the command `python -m unittest test_kata.py`

Note that only the simplest input interface is currently present. Errors with string input may result in an unhandled exception. 

## Brief

### Functional Requirements

- Complete the first 5 steps of the [String Calculator kata](https://osherove.com/tdd-kata-1), validated with a passing test suite.

### Non-Functional Requirements

- Code is implemented using the Red-Green-Refactor technique. *YES*
- Each step of the String Calculator kata should be developed in a separate branch and merged in to the `main` branch via a pull request. *YES*
- The repo provides instructions for a user to clone and run locally, with tests. Do not assume the user has strong experience in the language you'll be working in. *YES*
- A CI pipeline, which runs the application tests as part of branch pushes and merge requests, is up and running _before_ the first code pull request is filed. *DONE*
- The repo is set to block merges to `main` unless the pipelines are passing. *YES*

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

#### Step 2

Allow strings with unknown number of values

Tests: string with 4 and 10 values

So the splitting of the string according to the delimiter will allow for any amount of numbers to be handled - no changes to the code necessary - tests all pass. Woops.

#### Step 3

Allow for the use of the '\n' delimiter alongside ','

Added tests that include only the '\n' delimiter, as well as a combination of both.

I added a `.replace('\n',',')` before the string is split replace all new lines with commas. The rest of the code is unaffected.

#### Step 4

Support for different delimiters in the format `'//{delimiter}\n{numbers}'`.

Tests added for '//&\n4&9' and '//howdy\n1howdy4'

I added and else if statement that catches any strings beginning with '//', and splits the delimiter away from the numbers, before splitting the numbers using the identified delimiter. All tests pass. 

I then identified a potential edge case - what if a custom delimiter was identified, but there were no numbers, per the scenario in step 1 - so I added '//howdy\n' as a test - it failed. 

I opened up a Jupyter notebook to see what actually happens to to the string when I split it according to the '\n' - ['//howdy', '']. This is cool, because we have a second object in the list that we can work with, meaning that the situation is the same as `Add("")`. Since we are doing the same thing twice (even though in real terms it would take less time to copy and paste), the situation calls for a nested function - I have never been sure about the proper use of these.

I created an `Empty(string)` function that returns True if the string is empty. 

Added benefit is that this code change will affect all tests, so it is one of the more serious refactoring exercises in this kata.

Another edge case - what if someone set the custom delimiter to '\n' - it would break the code. This is a very specific case, so can be dealt with in a specific fashion. Test written for '//\n\n4\n3', which obviously fails.

Initially, I had hoped to include a `elif string[2:4] == '\n'` condition, but that did not seem to work in my Jupyter notebook (I figured out why later... see below), so I went with `elif string.count('\n') > 1` which achieves the same result in identifying offending delimiters. At that point we know that a) the delimiter is \n, and b) that the numbers part of the string will begin at index 6 (or actually index 4, as \n is counted as a single index... this means that `if string[2] == '\n':` works as a condition too! but lets proceed with the .count method).

The logic of the `\n` delimiter also has to precede the Empty(string) check, as otherwise we will get empty strings that trigger the `return 0`. All tests now pass.

But for completeness - what about '//\n\n'? Test fails - I already have the Empty nested function, so I will feed `string[4:]` into that to identify any offenders. Test now passes - all is well.

Can't think of any other problems that might come up.

#### Step 5

Calling Add with a negative number will throw an exception “negatives not allowed” - and the negative that was passed. If there are multiple negatives, show all of them in the exception message.

Three tests - single negative '-2', mix of positives and negatives '-2,-5,10', negatives only '-4,-3'. The method of testing for exceptions is a little different (and previously I was unfamiliar with it, so Stack Overflow really deserves the credit). 

`def test_negative_positive_mix(self):
    with self.assertRaises(Exception) as context:
        Add('-2,-5,10')
    self.assertTrue(context.exception, 'Negatives not allowed: [-2, -5]')`

This calls for a nested function (as we are going to run the check for every number in every case but '') that checks if the value is negative and appends it to a negatives_list. The return of the answers variable will have to be conditional on len(negatives_list) being 0.

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

The requirements are that each pull request is automatically tested, and cannot be merged unless the tests are passed.

The starting point would be a test file with no tests. The first pull request would include the tests for step 1, as well as the features tested - however the framework would already be in place, satisfying the brief requirements. 

This has the added benefit of expending the number of tests done with each pull request automatically. *I subsequently became aware that the tests used for the merge check are from the branch, not main, making this redundant)

Had a dummy moment here - I could not figure out the relationship of checks to statuses and almost went down the road of making API status calls. The issue was that I was trying to find a status that referred to 'CI' the name of the check or tests.yml. The correct status was 'build' the name of the job within the yml file. That only took best part of 2 hours - how silly.
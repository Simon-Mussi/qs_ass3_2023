## QS Assignment 3: Group XY

## Theoretical Questions
### Question 1:

### Question 2:

### Question 3:
Learning-based testing is a strategy that relies on machine learning to identify and predict potential bugs.
Therefore it has a few problems finding bugs in the following categories:
#### - Non-deterministic bugs:
These are bugs that appear randomly or are non-deterministic are hard to find for learning-based testing.
As these bugs can be caused by race conditions or timing issues, which do not occur consistently, it is hard to predict those bugs.
#### - New, Unseen bugs:
As machine learning is trained on older data, there may be cases, which it has not seen yet, 
and therefore makes the wrong prediction, or fails to detect the bug
#### - Complex or Multi-step bugs:
These are cases where the error only occurs under a specific set of conditions or a specific sequence. This is also hard
to find my learning-based testing, as these bugs may not be in the training data.
#### - Context specific bugs:
Bugs that are tied to the environment or a specific context, which are the hardware or software version or user behaviour, may not be represented or hardly
represented in the training data, so learning-based testing may fail to detect those.
#### - Bugs because of unscpecified or wrongly specified behaviour:
When the system does not have a well defined behaviour or it is specified in the wrong way, learning-based testing
may not find bugs, as it does not know that this does not belong to the general behaviour of the system.

## Practical Notes

### Task 1

#### Correct Vending Machine: xy
Briefly describe its behaviour.

#### For each faulty vending machine, describe the fault

### Task 3

#### Describe the bugs for each implementation. Add a shortest test-case that reproduces the bug 

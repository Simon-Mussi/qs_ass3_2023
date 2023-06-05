## QS Assignment 3: Group XY

## Theoretical Questions
### Question 1:
#### Answer to (a):
Conformance testing is decidable when when the full structur is known, this is the case for M2.
We can compare the outputs of M1 and M2, after we perform an exhaustive search of all possible input sequences.
A procedure could be:
##### 1. State Mapping:
For every state in M1, try to find a corresponding state in M2. If a state in M1 doesn't have a corresponding state in M2, then M1 is not conforming to M2.
##### 2. Transition Verification:
For every transition in M1, ensure there is a corresponding transition in M2 with the same input and output. If a transition in M1 doesn't have a 
corresponding transition in M2, then M1 is not conforming to M2.
##### 3. Exhaustive Input Testing:
If both state mapping and transition verification pass, then generate all possible sequences of inputs (up to a certain length, if the input alphabet is large) 
and apply them to both M1 and M2. If for any input sequence the output of M1 is not equal to the output of M2 (or M1 outputs where M2 doesn't specify one), 
then M1 does not conform to M2. 

This process will effectively verify whether M1 conforms to M2. However, it is important to note that this process can be computationally intensive, 
especially for large automata or large input alphabets.

#### Answer to (b):
If the structure of M2 (the specification) is not known and we can only interact with it, then conformance testing is typically done using black-box testing strategies, like model inference, and is generally considered undecidable in the formal sense. This is due to the "state explosion" problem, where the number of potential states and transitions in M2 can grow exponentially with the size of the input alphabet. However, practical methods can often provide useful results even if they don't offer absolute certainty. A common approach is to infer a model of M2 by interacting with it, a process sometimes referred to as "active learning" or "automata learning". 
Here is a basic procedure: 
##### 1. Interact with M2:
Generate sequences of inputs and record the corresponding sequences of outputs. Use these input-output pairs to infer the states and transitions of M2. 
##### 2. Build a Hypothesis Model:
Using the collected data, build a hypothesis model M2'. This model is an approximation or guess of the real structure of M2 based on the observed behavior. 
##### 3. Compare M1 to M2': 
Use the same comparison method as in scenario (a) to compare M1 to the hypothesis model M2'. If they match, M1 may conform to M2. 
##### 4. Refine the Model: 
If M1 and M2' do not match, use the counterexample to refine M2' and repeat the comparison. The L* algorithm is a classic example of an algorithm that infers a finite automaton from a given system using this methodology. 

However, this approach does not guarantee to find all the states and transitions of M2, especially if it has a large number of states, a large input alphabet, or complex behavior. Further, it cannot definitively prove conformance, only provide evidence supporting it.
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

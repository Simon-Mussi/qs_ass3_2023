## QS Assignment 3: Group 52

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

#### Answer to (c):
If the structure of M2 is not known but the maximum number of states is known, and you can interact with it, this can help to make the conformance testing more feasible, although it remains undecidable in the formal sense due to the reasons previously mentioned. Similar to scenario (b), you can use active learning or automata learning methods to infer a model of M2. However, knowing the maximum number of states can guide and limit the exploration of M2. 
Here is a general approach: 
##### 1. Interact with M2: 
Start interacting with M2 by providing inputs and recording outputs. Generate a variety of sequences of inputs to cover as many possible states as possible. Since you know the maximum number of states, this can limit the number of possible sequences you need to try. 
##### 2. Build a Hypothesis Model: 
As you interact with M2 and gather more information, you construct a hypothesis model M2'. You continue refining this model as you interact with M2 more and get new information. 
##### 3. Compare M1 to M2': 
Once you have your hypothesis model, you compare it with M1, just like in scenarios (a) and (b). If they match, M1 may conform to M2. 
##### 4. Refine the Model: 
If they don't match, use the counterexample to refine your hypothesis model and repeat the process. 

Knowing the maximum number of states can significantly improve the efficiency of the model inference and comparison process, but it still doesn't guarantee perfect results. It can, however, reduce the possibility of infinite exploration, which can happen when the structure of M2 is unknown and there's no known limit to the number of states. 

Lastly, similar to the previous scenarios, conformance can't be definitively proven but only supported by empirical evidence.
### Question 2:
In the context of learning automata or models (for instance, with the L* algorithm), an equivalence oracle is a hypothetical tool or mechanism that can definitively answer whether a hypothesized model is equivalent to the true (unknown) model. The oracle, if it exists, is assumed to be able to provide a counterexample if the two models are not equivalent.

In practical situations, a true equivalence oracle does not usually exist, and we have to approximate its role with testing, which can only provide evidence of equivalence but not definitive proof.

The reason an equivalence oracle might find, in theory, infinitely many counterexamples is due to the way the learning process is designed and the nature of the language or automaton being learned.

For the task at hand, functions like "is_balanced" and "funny_counter" likely have behaviors dependent on specific conditions or sequences of inputs. When an incorrect hypothesis model is proposed, the equivalence oracle provides a counterexample which shows a difference between the hypothesized model and the true model. This counterexample is used to refine the hypothesis.

However, since there can be an infinite number of input sequences (depending on the specification of "is_balanced" and "funny_counter"), there are potentially an infinite number of counterexamples that could be found. Each counterexample represents a different sequence of inputs leading to different behavior between the hypothesis and the true model.

In practical terms, a method to provide some guarantee that the learned model is correct might involve an iterative process of learning and testing. The basic L* algorithm can be used to learn an initial model, then testing is used to find any discrepancies between the learned model and the actual behavior of the "is_balanced" and "funny_counter" functions. If discrepancies are found (i.e., counterexamples), these are fed back into the learning algorithm to refine the model. This process is repeated until no more discrepancies can be found within the constraints of your testing capacity.

Note that this process does not guarantee absolute correctness of the learned model. It only provides evidence that the model is correct within the limits of the testing that has been performed. Full verification of the model's correctness would require exhaustive testing, which is generally not feasible for complex models or large input spaces.

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

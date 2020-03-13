## Machine Learning Bit by Bit - Naive Bayes

Two years ago, at the first time I began to know machine learning, I was introduced an example of documents classification by Naive Bayes model. At that time I thought Bayes was all in machine learning.

How stupid I was. (and am ?)

#### Bayes' Theorem

Bayes' Theorem is something you should have learned in your college.

In probability theory and statistics, Bayes’ theorem describes the probability of an event, based on prior knowledge of conditions that might be related to the event.

Bayes' theorem is stated mathematically as the following equation:

	P (A∣B) = P(B∣A)P(A)/P(B)

where A and B are events and P(B) ≠ 0.
* P(A) and P(B) are the probabilities of observing A and B without regard to each other.
* P(A|B), a conditional probability, is the probability of observing event A given that B is true.
* P(B|A) is the probability of observing event B given that A is true.

##### An Example

The entire output of a factory is produced on three machines. The three machines account for 20%, 30%, and 50% of the output, respectively. The fraction of defective items produced is this: for the first machine, 5%; for the second machine, 3%; for the third machine, 1%. If an item is chosen at random from the total output and is found to be defective, what is the probability that it was produced by the third machine?

A solution is as follows. Let A<sub>i</sub> denote the event that a randomly chosen item was made by the ith machine (for i = 1,2,3). Let B denote the event that a randomly chosen item is defective. Then, we are given the following information:

P(A<sub>1</sub>) = 0.2,    P(A<sub>2</sub>) = 0.3,    P(A<sub>3</sub>) = 0.5.

If the item was made by the first machine, then the probability that it is defective is 0.05; that is, P(B | A<sub>1</sub>) = 0.05. Overall, we have

P(B | A<sub>1</sub>) = 0.05,    P(B | A<sub>2</sub>) = 0.03,    P(B | A<sub>3</sub>) = 0.01.

To answer the original question, we first find P(B). That can be done in the following way:

P(B) = Σi P(B | A<sub>i</sub>) P(A<sub>i</sub>) = (0.05)(0.2) + (0.03)(0.3) + (0.01)(0.5) = 0.024.

Hence 2.4% of the total output of the factory is defective.

We are given that B has occurred, and we want to calculate the conditional probability of A<sub>3</sub>. By Bayes' theorem,

P(A<sub>3</sub> | B) = P(B | A<sub>3</sub>) P(A<sub>3</sub>)/P(B) = (0.01)(0.50)/(0.024) = 5/24.

Given that the item is defective, the probability that it was made by the third machine is only 5/24. Although machine 3 produces half of the total output, it produces a much smaller fraction of the defective items.

#### Naive Bayes Classifier

I have to stop describing how Naive Bayes Classifier works, because the editting system here doesn't support complex math equations. Please study them on Wikipedia.

Besides all the basis of Probabilities. The most important thing to bear in mind is: assume that each feature F<sub>i</sub> is conditionally independent of every other feature F<sub>j</sub>. This assumption makes the calculation of conditional probability feasible, and it's how "NAIVE" come around.

##### Gaussian Naive Bayes

##### Multinomial Naive Bayes

##### Bernoulli Naive Bayes



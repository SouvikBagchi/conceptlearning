This repo contains python class - findingS

This class can be used to train a concept learning algorithm called Find S.
The class is initialized by mentioning the following variables -
positive_outcome - the value of the positive outcome in the result_set (eg. 'true', 1 etc.)
no_of_attributes - the number of attributes in the training set
result_list - a list of results, i.e. are they positive or negative
attribute_list - a list of attributes for the corresponding results

Methods in this class - 
1) trainS - 
Parameters : None
What it does : Will find the hypothesis according to the Find-S algorithm and store it in the instance variable hypothesis.
What it Returns : Nothing

2) resultS - 
Parameters - Attributes to be checked against
What it does - Classifies into positive or negative outcome
What is Returns - 0 for negative outcome, 1 for positive classification


An example of use is provided at the end of the class
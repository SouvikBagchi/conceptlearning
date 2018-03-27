This repo contains python class - findingS

This class can be used to train a concept learning algorithm called Find S.
The class is initialized by mentioning the following variables -
positive_outcome - the value of the positive outcome in the result_set (eg. 'true', 1 etc.)
result_list - a list of results, i.e. are they positive or negative
attribute_list - a list of attributes for the corresponding results

This class contains a method trainS which when called on an instantiated class variable will find the hypothesis
according to the Find-S algorithm and store it in the instance variable hypothesis.

An example of use is already provided at the end of the class
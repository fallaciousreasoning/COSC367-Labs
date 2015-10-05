__author__ = 'jayha_000'
import csv

def learn_prior(filename, pseudo_count=0):
    training_examples = []
    with open("spam-labelled.csv") as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)][1:]

    spam = 0
    for info in training_examples:
        if info[-1] == '1': spam += 1

    return (spam + pseudo_count) / (len(training_examples) + 2 * pseudo_count)


prior = learn_prior("spam-labelled.csv")
print("Prior probability of spam is {:.5f}.".format(prior))

prior = learn_prior("spam-labelled.csv")
print("Prior probability of not spam is {:.5f}.".format(1 - prior))

prior = learn_prior("spam-labelled.csv", pseudo_count = 1)
print(format(prior, ".5f"))

prior = learn_prior("spam-labelled.csv", pseudo_count = 2)
print(format(prior, ".5f"))

prior = learn_prior("spam-labelled.csv", pseudo_count = 10)
print(format(prior, ".5f"))

prior = learn_prior("spam-labelled.csv", pseudo_count = 100)
print(format(prior, ".5f"))

prior = learn_prior("spam-labelled.csv", pseudo_count = 1000)
print(format(prior, ".5f"))

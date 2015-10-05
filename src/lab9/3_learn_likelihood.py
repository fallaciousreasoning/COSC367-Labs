__author__ = 'jayha_000'

import csv

def learn_likelihood(file_name, pseudo_count=0):
    training_examples = []
    with open("spam-labelled.csv") as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)][1:]

    likelihoods = [[pseudo_count, pseudo_count] for i in range(12)]
    prior = 0

    for row in training_examples:
        spam = int(row[-1])
        for i in range(12):
            likelihoods[i][spam] += int(row[i])

        prior += spam

    for i in range(len(likelihoods)):
        likelihoods[i][True] /= (prior + 2 * pseudo_count)
        likelihoods[i][False] /= (len(training_examples) - prior + 2 * pseudo_count)

    return likelihoods

likelihood = learn_likelihood("spam-labelled.csv")
print(len(likelihood))
print([len(item) for item in likelihood])

likelihood = learn_likelihood("spam-labelled.csv")

print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))

likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

print("With Laplacian smoothing:")
print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))

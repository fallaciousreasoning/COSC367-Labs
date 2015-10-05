__author__ = 'jayha_000'

import csv

def posterior(prior, likelihood, observation):
    false = 1- prior
    true = prior

    for i in range(len(observation)):
        if observation[i]:
            true *= likelihood[i][True]
            false *= likelihood[i][False]
        else:
            true *= (1 - likelihood[i][True])
            false *= (1 - likelihood[i][False])

    return true / (true + false)

def learn_prior(filename, pseudo_count=0):
    training_examples = []
    with open("spam-labelled.csv") as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)][1:]

    spam = 0
    for info in training_examples:
        if info[-1] == '1': spam += 1

    return (spam + pseudo_count) / (len(training_examples) + 2 * pseudo_count)

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

def nb_classify(prior, likelihood, input_vector):
    true = posterior(prior, likelihood, input_vector)
    false = 1 - true

    if true > false:
        return ("Spam", true)
    else:
        return ("Not Spam", false)

prior = learn_prior("spam-labelled.csv")
likelihood = learn_likelihood("spam-labelled.csv")

input_vectors = [
    (1,1,0,0,1,1,0,0,0,0,0,0),
    (0,0,1,1,0,0,1,1,1,0,0,1),
    (1,1,1,1,1,0,1,0,0,0,1,1),
    (1,1,1,1,1,0,1,0,0,1,0,1),
    (0,1,0,0,0,0,1,0,1,0,0,0),
]

predictions = [nb_classify(prior, likelihood, vector)
               for vector in input_vectors]

for label, certainty in predictions:
    print("Prediction: {}, Certainty: {:.5f}"
          .format(label, certainty))

prior = learn_prior("spam-labelled.csv", pseudo_count=1)
likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

input_vectors = [
    (1,1,0,0,1,1,0,0,0,0,0,0),
    (0,0,1,1,0,0,1,1,1,0,0,1),
    (1,1,1,1,1,0,1,0,0,0,1,1),
    (1,1,1,1,1,0,1,0,0,1,0,1),
    (0,1,0,0,0,0,1,0,1,0,0,0),
]

predictions = [nb_classify(prior, likelihood, vector)
               for vector in input_vectors]

for label, certainty in predictions:
    print("Prediction: {}, Certainty: {:.5f}"
          .format(label, certainty))

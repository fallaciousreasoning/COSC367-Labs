__author__ = 'jayha_000'

def accuracy(predicted_labels, correct_labels):
    match = 0
    for i in range(len(predicted_labels)):
        if predicted_labels[i] != correct_labels[i]: continue
        match += 1

    return match / len(correct_labels)

print(accuracy((True, False, False, False),
               (True, True, False, False)))

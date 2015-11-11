import itertools

__author__ = 'jayha_000'

def joint_prob(network, assignment):
    total = 1
    for key in assignment:
        value = network[key]

        parents = []
        for p in value['Parents']:
            parents.append(assignment[p])
        
        parents = tuple(parents)
        total *= value['CPT'][parents] if assignment[key] else 1 - value['CPT'][parents]

    return total

def query(network, query_var, evidence):
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    trueProb = 0
    falseProb = 0

    for values in itertools.product((True, False), repeat=len(hidden_vars)):
        hidden_assignments = {var:val for var,val in zip(hidden_vars, values)}
        hidden_assignments.update(evidence)
        hidden_assignments.update({query_var: True})
        trueProb += joint_prob(network, hidden_assignments)

        hidden_assignments[query_var] = False
        falseProb += joint_prob(network, hidden_assignments)

    normalizer = trueProb + falseProb
    result = {True: trueProb / normalizer, False: falseProb / normalizer}
    return result

network = {
    'Disease' : {
        "Parents" : [],
        "CPT" : {
            (): 0.00001
        }
    },
    'Test' : {
        'Parents' : ["Disease"],
        "CPT" : {
            (True,): 0.99,
            (False,): 0.01
        }
    }
}

answer = query(network, 'Disease', {'Test': True})
print("The probability of having the disease\n"
      "if the test comes back positive: {:.8f}"
      .format(answer[True]))

answer = query(network, 'Disease', {'Test': False})
print("The probability of having the disease\n"
      "if the test comes back negative: {:.8f}"
      .format(answer[True]))
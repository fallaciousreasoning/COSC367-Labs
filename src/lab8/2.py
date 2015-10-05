import itertools

__author__ = 'jayha_000'

def joint_prob(network, assignment):
    probs = []
    for key in assignment:
        if len(network[key]["Parents"]) == 0:
            prob = network[key]["CPT"][()]
            if not assignment[key]:
                prob = 1 - prob

            probs.append(prob)
        else:
            lookup = []
            for parent in network[key]["Parents"]:
                lookup.append(assignment[parent])

            lookupTuple = tuple(lookup)
            prob = network[key]["CPT"][lookupTuple]
            if not assignment[key]:
                prob = 1 - prob
            probs.append(prob)

    result = 1
    for prob in probs:
        result *= prob

    return result

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
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
        }},
}

answer = query(network, 'A', {})
print("P(A=true)={:.5f}".format(answer[True]))
print("P(A=false)={:.5f}".format(answer[False]))

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
        }},

    'B': {
        'Parents': ['A'],
        'CPT': {
            (True,): 0.8,
            (False,): 0.7,
        }},
}

answer = query(network, 'B', {'A': False})
print("P(B=true|A=false) = {:.5f}".format(answer[True]))
print("P(B=false|A=false) = {:.5f}".format(answer[False]))

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
        }},

    'B': {
        'Parents': ['A'],
        'CPT': {
            (True,): 0.8,
            (False,): 0.7,
        }},
}

answer = query(network, 'B', {})
print("P(B=true) = {:.5f}".format(answer[True]))
print("P(B=false) = {:.5f}".format(answer[False]))

network = {
    'Burglary': {
        'Parents': [],
        'CPT': {
            (): 0.001
        }},

    'Earthquake': {
        'Parents': [],
        'CPT': {
            (): 0.002,
        }},
    'Alarm': {
        'Parents': ['Burglary','Earthquake'],
        'CPT': {
            (True,True): 0.95,
            (True,False): 0.94,
            (False,True): 0.29,
            (False,False): 0.001,
        }},

    'John': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
        }},

    'Mary': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.7,
            (False,): 0.01,
        }},
}

answer = query(network, 'Burglary', {'John': True, 'Mary': True})
print("Probability of a burglary when both\n"
      "John and Mary have called: {:.3f}".format(answer[True]))

network = {
    'Burglary': {
        'Parents': [],
        'CPT': {
            (): 0.001
        }},

    'Earthquake': {
        'Parents': [],
        'CPT': {
            (): 0.002,
        }},
    'Alarm': {
        'Parents': ['Burglary','Earthquake'],
        'CPT': {
            (True,True): 0.95,
            (True,False): 0.94,
            (False,True): 0.29,
            (False,False): 0.001,
        }},

    'John': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
        }},

    'Mary': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.7,
            (False,): 0.01,
        }},
}

answer = query(network, 'John', {'Mary': True})
print("Probability of John calling if\n"
      "Mary has called: {:.5f}".format(answer[True]))
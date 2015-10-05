"""This module provides a class for constructing a constraint
satisfaction problem (CSP) object. This is module is specifically
written for COSC367 lab quizzes and exercises.

Author: Kourosh Neshatian
Last modified: 25 Sep 2015
"""

from collections import namedtuple
from collections.abc import Iterable


def scope(constraint):
    """Takes a constraint in the form of a function (or lambda
    expression) and returns the set of formal parameter names.

    """
    return set(constraint.__code__.co_varnames[
               :constraint.__code__.co_argcount])


def satisfies(assignment, constraint):
    """Tests whether the assignment satisfies the constraints. The
    assignment is a dictionary of variable names and their values. The
    constraint is a predicate function (or lambda expression). The
    assignment must contain (at least) all the bindings (parameters)
    required by the constraint.

    """
    return constraint(**{var:val for var,val in assignment.items()
                         if var in scope(constraint)})


class CSP(namedtuple("CSP", "var_domains, constraints")):
    """An instance of a CSP is constructed by specifying a dictionary,
     var_domains, of the form "var_name": list_of_values, and a
     collection of constraints where each constraint is a predicate
     function (returns either true or false).  The set of CSP variable
     names are implicitly specified by the keys of var_domains. The
     name of the parameters of constraints must be in the set of
     variable names.

    """

    def __init__(self, var_domains, constraints):
        assert type(var_domains) is dict
        assert all(type(name) is str and type(domain) is list
                   for name, domain in var_domains.items())
        assert isinstance(constraints, Iterable)
        assert all(callable(c) and scope(c) <= set(var_domains.keys())
                   for c in constraints)




swap12([A|[B|Tail1]], [C|[D|Tail2]]) :-
	=(A, D),
	=(B, C),
	=(Tail1, Tail2).

test_answer :-
    swap12(L, [1]),
    write('Wrong answer!'),
    halt.

test_answer :-
    write('OK'),
    halt.
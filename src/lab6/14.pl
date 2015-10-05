py_triple(A, B, C, Min, Max) :-
	between(Min, Max, A),
	between(Min, Max, B),
	between(Min, Max, C),
	py_triple(A, B, C).

py_triple(A, B, C) :-
	0 < A,
	A =< B,
	B =< C,
	AS is A*A,
	BS is B*B,
	CS is C*C,
	H is AS + BS,
	=(CS, H).


test_answer :-
    findall([A,B,C],py_triple(A,B,C,1,10),List),
    write(List),
    halt.

test_answer :- 
    write('Wrong answer!'),
    halt.
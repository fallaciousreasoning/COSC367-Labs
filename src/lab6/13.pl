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
    py_triple(3,4,5),
    write('Correct!'),
    halt.

test_answer :- 
    write('Wrong answer!'),
    halt.
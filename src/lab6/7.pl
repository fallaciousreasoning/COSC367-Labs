element(List, Index, Value) :-
	nth0(Index, List, X),
	=(X, Value).

test_answer :-
    element([a, b, c, d, e, f], 2, X),
    write(X),
    halt.

test_answer :- 
    write('Wrong answer!'),
    halt.
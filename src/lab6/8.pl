remove(X, [], []).

remove(X, [H1|T1], ListOut) :-
	=(X, H1),
	remove(X, T1, ListOut);
	remove(X, T1, Z),
	append([H1], Z, ListOut).


test_answer :-
    remove(a, [a, b, a, c, d, a, b], L),
    write(L),
    halt.

test_answer :- 
    write('Wrong answer!'),
    halt.
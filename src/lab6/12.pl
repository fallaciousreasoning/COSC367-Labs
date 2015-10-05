inside(Min, Max, Min).

inside(Min, Max, X) :-
	Z is Min + 1,
	Z =< Max,
	inside(Z, Max, X).

test_answer :-
    findall(X, inside(1, 3, X), List),
    write(List),
    halt.

test_answer :- 
    write('Wrong answer!'),
    halt.
twice([], []).

twice([H|T], [A|[B|C]]) :- 
	=(H, A),
	=(H, B),
	twice(T, C).

test_answer :-
    twice([a, b, c, d], L),
    write(L),
    halt.

test_answer :- 
    write('Wrong answer!'),
    halt.
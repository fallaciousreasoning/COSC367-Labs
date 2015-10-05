swap_ends([], []).

swap_ends(L1, L2) :- 
	append([H1 | B1], [T1], L1),
	append([T1 | B1], [H1], L2).

test_answer :-
    swap_ends(L, [term1, term2, term3, term4]),
    write(L),
    halt.

test_answer :-
    write('Wrong answer!'),
    halt.
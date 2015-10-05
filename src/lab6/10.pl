merge([], [], []).

merge([], B, List) :-
	List = B.

merge(A, [], List) :-
	List = A.

merge([A|ARest], [B|BRest], [H|List]) :- 
	A < B,
	H = A,
	merge(ARest, [B|BRest], List);

	H = B,
	merge([A|ARest], BRest, List).

test_answer :-
    merge([3, 6, 7], [1, 2, 3, 5, 8], L),
    write(L),
    halt.

test_answer :- 
    write('Wrong answer!'),
    halt.
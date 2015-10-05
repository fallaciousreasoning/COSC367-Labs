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

split_odd_even([], [], []).

split_odd_even([A|[B|Rest]], [A|ListA], [B|ListB]) :-
  split_odd_even(Rest, ListA, ListB).
  
split_odd_even([A|Rest], [A|ListA], ListB) :-
  =(Rest, []),
  split_odd_even(Rest, ListA, ListB).

merge_sort([], []).
merge_sort([X], [X]).

merge_sort([H|T], [RH|RT]) :- 
	split_odd_even([H|T], ListA, ListB),
	merge_sort(ListA, RA),
	merge_sort(ListB, RB),
	merge(RA, RB, [RH|RT]).

test_answer :-
    merge_sort([4,3,1,2], L),
    write(L),
    halt.

test_answer :- 
    write('Wrong answer!'),
    halt.
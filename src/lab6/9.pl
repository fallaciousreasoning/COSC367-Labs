split_odd_even([], [], []).

split_odd_even([A|[B|Rest]], [A|ListA], [B|ListB]) :-
  split_odd_even(Rest, ListA, ListB).
  
split_odd_even([A|Rest], [A|ListA], ListB) :-
  =(Rest, []),
  split_odd_even(Rest, ListA, ListB).

test_answer :-
    split_odd_even([a,b,c,d,e,f,g], A, B),
    write(A),
    write(B),
    halt.

test_answer :- 
    write('Wrong answer!'),
    halt.
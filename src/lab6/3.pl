listtran([], []).

listtran([H1|T1], [H2|T2]) :-
	tran(H1, H2),
	=([], T1),
	=([], T2);

	tran(H2, H1),
	=([], T2),
	=([], T1);

	listtran(T1, T2),
	tran(H1, H2);

	listtran(T1, T2),
	tran(H2, H1).


tran(1, one). 
tran(2, two). 
tran(3, three). 

test_answer :-
    listtran([1, 2, 3], X),
    write(X),
    halt.

test_answer :- 
    write('Wrong answer!'),
    halt.
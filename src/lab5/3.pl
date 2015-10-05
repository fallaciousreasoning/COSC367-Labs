reflection(point(X1, Y1), point(X2, Y2)) :-
	=(X1, Y2), =(Y1, X2).

test_answer :-
reflection(point(-5, 8), point(X, Y)),
        write(point(X, Y)),
        halt.

test_answer :- write('Wrong answer!'),
               halt.
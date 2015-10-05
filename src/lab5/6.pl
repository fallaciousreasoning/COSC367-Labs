directlyIn(irina, natasha).
directlyIn(natasha, olga).
directlyIn(olga, katarina).

contains(X, Y) :-
	directlyIn(Y, X);
	directlyIn(Y, Z), contains(Z, Y).
	
test_answer :-
contains(katarina, natasha),
        write('OK'),
        halt.

test_answer :- write('Wrong answer!'),
               halt.
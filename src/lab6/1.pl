second(List1, X) :-
	nth0(1, List1, Z),
	=(Z, X).


test_answer :-
    second([1], X),
    write('Wrong answer!'),
    halt.

test_answer :-
    write('OK'),
    halt.
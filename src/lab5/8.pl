mirror(tree(LEFT1, RIGHT1), tree(LEFT2, RIGHT2)) :-
	mirror(LEFT1, RIGHT2), mirror(RIGHT1, LEFT2).

mirror(RIGHT_LEAF, RIGHT_LEAF) :-
	=(LEAF1, RIGHT_LEAF).

test_answer :-
    mirror(tree(tree(leaf(1),  leaf(2)),  tree(leaf(3), leaf(4))), T),
    write(T),
    halt.

test_answer :-
    write('Wrong answer!'),
    halt.
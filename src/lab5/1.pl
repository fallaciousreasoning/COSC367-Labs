eats(Person, Thing) :- likes(Person, Thing); hungry(Person), edible(Thing).

likes(bob, chocolate).

test_answer :- eats(bob, chocolate),
               write('Bob eats chocolate.').

test_answer :- write('Wrong answer!').

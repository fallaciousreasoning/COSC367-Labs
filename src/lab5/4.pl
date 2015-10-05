f(a).
f(b).
f(c).

g(b).
g(c).

h(c).

k(X):-f(X), g(X), h(X).

Search Tree
f(a), g(a) --> fail
f(b), g(b), h(b) --> fail
f(c), g(c), h(c) --> success
solution(W1, W2, W3, W4, W5, W6) :-
		word(W1, A1, A2, A3, A4, A5, A6, A7),
		word(W2, B1, B2, B3, B4, B5, B6, B7),
		word(W3, C1, C2, C3, C4, C5, C6, C7),
		word(W4, D1, D2, D3, D4, D5, D6, D7),
		word(W5, E1, E2, E3, E4, E5, E6, E7),
		word(W6, F1, F2, F3, F4, F5, F6, F7),
		=(A2, D2), =(A4, E2), =(A6, F2),
		=(B2, D4), =(B4, E4), =(B6, F4),
		=(C2, D6), =(C4, E6), =(C6, F6).

	
word(abalone,a,b,a,l,o,n,e). 
word(abandon,a,b,a,n,d,o,n). 
word(enhance,e,n,h,a,n,c,e). 
word(anagram,a,n,a,g,r,a,m). 
word(connect,c,o,n,n,e,c,t). 
word(elegant,e,l,e,g,a,n,t).

test_answer :-
findall((V1,V2,V3,H1,H2,H3), solution(V1,V2,V3,H1,H2,H3), L),
sort(L,S), 
foreach(member(X,S), (write(X), nl)).

test_answer :- write('Wrong answer!'),
               halt.
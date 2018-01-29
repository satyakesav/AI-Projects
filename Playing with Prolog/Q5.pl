/* Write a predicate to generate all bit vectors of a specified length: bitvec(X,Y)*/

bitvec(1,[1]).
bitvec(1,[0]).
bitvec(0,[]).

bitvec(N,[1|Z]) :- N>1, N0 is N-1, bitvec(N0,Z).
bitvec(N,[0|Z]) :- N>1, N0 is N-1, bitvec(N0,Z).

code(1,1,[1]).
code(1,0,[0]).

code(N,K,[1|Z]) :- N>=K, N>1, K>0, N0 is N-1, K0 is K-1, code(N0,K0,Z).
code(N,K,[0|Z]) :- N>=K, N>1, N0 is N-1, code(N0,K,Z).
/* Implement prime factorization in Prolog */

divisible(N,X) :- M is N mod X, M=0.

%This is the query for testing... for e.g:- primes(10,Z)
factor(N, Z) :- loops(N, Z, 2).

loops(1,[],K) :- K>1.
loops(N,[],K) :- N=<0, K>1.

loops(N,[K|Z],K) :- divisible(N,K), Y is N/K, loops(Y,Z,K).
loops(N,Z,K) :- K=<N, \+divisible(N,K), K0 is K+1, loops(N,Z,K0).
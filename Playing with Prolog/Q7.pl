/* SEND + MORE = MONEY is a classical" cryptarithmetic" puzzle: the variables S, E, N, D, M, O, R, Y represent digits between 0 and 9, and the task is finding values for them */

solve([S,E,N,D,M,O,R,Y]) :-
select(S,[0,1,2,3,4,5,6,7,8,9],WS),
\+(S=0),
select(E,WS,WSE),
select(N,WSE,WSEN),
select(D,WSEN,WSEND),
select(M,WSEND,WSENDM),
\+(M=0),
select(O,WSENDM,WSENDMO),
select(R,WSENDMO,WSENDMOR),
select(Y,WSENDMOR,WSENDMORY),
SEND is 1000*S+100*E+10*N+D,
MORE is 1000*M+100*O+10*R+E,
MONEY is 10000*M+1000*O+100*N+10*E+Y,
MONEY is SEND+MORE.
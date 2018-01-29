% Write a prolog function to remove duplicates from a list.
% ?-remdups([1,3,4,2,4,3,6,8,6,5,4,2,3,4,9],X).
% X = [1, 8, 6, 5, 2, 3, 4, 9]

remdups([],[]).
remdups([X],[X]).

remdups([X|Xs],[X|Ys]) :- remdups(Xs,Ys), \+member(X,Ys).
remdups([X|Xs],Ys) :- remdups(Xs,Ys), member(X,Ys).
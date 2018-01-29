/*Write rules in Prolog to infer various kinship relationships in terms of basic predicates like parent(X,Y) and female(X) and male(Y).  Input the following facts about people on The Simpsons*/

parent(bart, homer).
parent(bart, marge).
parent(lisa, homer).
parent(lisa, marge).
parent(maggie, homer).
parent(maggie, marge).
parent(homer, abraham).
parent(herb, abraham).
parent(tod, ned).
parent(rod, ned).
parent(marge, jackie).
parent(patty ,jackie).
parent(selma, jackie).

female(maggie).
female(lisa).
female(marge).
female(patty).
female(selma).
female(jackie).

male(bard).
male(homer).
male(herb).
male(burns).
male(smithers).
male(tod).
male(rod).
male(ned).
male(abraham).

brother(X, Y) :- parent(X, Z), parent(Y, Z), male(Y), \+ (X = Y).
sister(X, Y) :- parent(X, Z), parent(Y, Z), female(Y), \+ (X = Y).
aunt(X, Y) :- female(Y), parent(X, Z), parent(Z, K), parent(Y, K), \+ (Z = Y).
uncle(X, Y) :- male(Y), parent(X, Z), parent(Z, K), parent(Y, K), \+ (Z = Y).
grandfather(X, Y) :- male(Y), parent(X, Z), parent(Z, Y).
granddaughter(X, Y) :- female(Y), parent(Y, Z), parent(Z, X).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
descendant(X, Y) :- ancestor(Y,X).
unrelated(X, Y) :- \+ brother(X, Y), \+ sister(X, Y), \+ aunt(X, Y), \+ uncle(X, Y), \+ grandfather(X, Y), \+ granddaughter(X, Y), \+ ancestor(X, Y), \+ descendant(X, Y), \+ parent(X, Y), \+ brother(Y, X), \+ sister(Y, X), \+ aunt(Y, X), \+ uncle(Y, X), \+ grandfather(Y, X), \+ granddaughter(Y, X), \+ ancestor(Y, X), \+ descendant(Y, X), \+ parent(Y, X).

%['C:/Users/GSK/Desktop/aiass/Q1.pl'].
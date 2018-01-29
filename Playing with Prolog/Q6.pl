/* Write a logic program to compute the zeros of sin(x), that  is the values of x such that sin(x)=0, using Newton's method */

sin_zero(X,Y) :- K is sin(X), K>(-0.0001), K<(0.0001), (Y=X).
sin_zero(X,Y) :- K is sin(X), \+ (K>(-0.0001)), Z is X-sin(X)/cos(X), sin_zero(Z,Y).
sin_zero(X,Y) :- K is sin(X), \+ (K<(0.0001)), Z is X-sin(X)/cos(X), sin_zero(Z,Y).
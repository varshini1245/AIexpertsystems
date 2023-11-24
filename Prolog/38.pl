% Facts defining family relationships
parent(john, sue).
parent(john, bob).
parent(mary, sue).
parent(mary, bob).
parent(sue, emily).
parent(sue, george).
parent(bob, lily).
parent(bob, james).

% Rules defining different family relationships
father(X, Y) :-
    parent(X, Y),
    male(X).

mother(X, Y) :-
    parent(X, Y),
    female(X).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.
sister(X, Y) :-
    sibling(X, Y),
    female(X).

brother(X, Y) :-
    sibling(X, Y),
    male(X).

grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).

grandchild(X, Y) :-
    grandparent(Y, X).

grandfather(X, Y) :-
    grandparent(X, Y),
    male(X).

uncle(X, Y) :-
    brother(X, Z),
    parent(Z, Y).

% Additional gender definitions (replace with real gender data if available)
male(john).
male(bob).
male(george).
male(james).

female(sue).
female(mary).
female(emily).
female(lily).

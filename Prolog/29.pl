% Facts about the family relationships
father(john, lisa).
father(tom, mary).

mother(mary, lisa).
mother(mary, mike).

sister(lisa, mike).

% Rules to define other relationships
parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).

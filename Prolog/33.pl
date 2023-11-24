% parent_child.pl

% Facts: Define genders and parent-child relationships
gender(john, male).
gender(jane, female).
gender(kate, female).

has_child(john, mary).
has_child(jane, mary).
has_child(jane, peter).
has_child(kate, lily).

% Rules: Define parent relationship based on gender and having a child
parent(X) :-
    gender(X, female),
    has_child(X, _).

% Query to find all parents based on defined rules and facts
find_parents :-
    write('List of parents: '), nl,
    parent(Parent),
    write(Parent), nl,
    fail.


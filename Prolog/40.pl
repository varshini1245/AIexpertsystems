% Every boy or girl is a child
is_child(X) :-
    boy(X).
is_child(Y) :-
    girl(Y).

% Every child gets a doll or a train or a lump of coal
gets_toy(X, doll) :-
    is_child(X).
gets_toy(Y, train) :-
    is_child(Y).
gets_toy(Z, lump_of_coal) :-
    is_child(Z).

% No boy gets any doll
no_doll_for_boy(B) :-
    boy(B),
    \+ gets_toy(B, doll).

% No child who is good gets any lump of coal
good_child(X) :-
    is_child(X),
    good(X).
no_coal_for_good_child(G) :-
    good_child(G),
    \+ gets_toy(G, lump_of_coal).

% Jack is a boy
boy(jack).

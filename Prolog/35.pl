no_attack(_, []).
no_attack(X/Y, [X1/Y1 | Rest]) :-
    nonvar(X),
    nonvar(Y),
    nonvar(X1),
    nonvar(Y1),
    Y =\= Y1,
    abs(Y1 - Y) =\= abs(X1 - X),
    no_attack(X/Y, Rest).

% Place N queens on the board
queens(0, []).
queens(N, [X/Y | Others]) :-
    N > 0,
    N1 is N - 1,
    queens(N1, Others),
    member(Y, [1, 2, 3, 4]),
    no_attack(X/Y, Others).

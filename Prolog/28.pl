% Facts about birds and their flying ability
can_fly(sparrow).
can_fly(eagle).
can_fly(crow).

% Rules for birds that cannot fly
cannot_fly(penguin).

% Query to determine if a bird can fly
bird_can_fly(Bird) :-
    can_fly(Bird),
    write(Bird), write(' can fly.'), nl.

bird_can_fly(Bird) :-
    cannot_fly(Bird),
    write(Bird), write(' cannot fly.'), nl.

bird_can_fly(OtherBird) :-
    \+ (can_fly(OtherBird); cannot_fly(OtherBird)),
    write('Information about '), write(OtherBird), write(' is not available.'), nl.

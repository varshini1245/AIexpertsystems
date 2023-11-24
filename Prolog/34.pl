% Define facts about animals and their characteristics
has_feathers(sparrow).
has_feathers(eagle).
has_fur(cat).
has_fur(dog).
has_fur(bear).

gives_birth_to_live_young(cat).
gives_birth_to_live_young(dog).
gives_birth_to_live_young(bear).

% Rules defining mammals and birds based on characteristics
mammal(X) :-
    has_fur(X),
    gives_birth_to_live_young(X).

bird(X) :-
    has_feathers(X),
    \+ mammal(X).  % A bird is not a mammal if it has feathers but doesn't give birth to live young.

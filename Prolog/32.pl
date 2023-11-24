% Diagnose predicate
diagnose(Condition) :-
    write('Enter your symptoms one by one, and type "done" when finished.'), nl,
    collect_symptoms(Symptoms),
    condition(Condition),
    member(Symptom, Symptoms),
    symptom(Symptom),
    not(incorrect_symptom(Symptom, Condition)).

% Helper predicate to collect symptoms
collect_symptoms(Symptoms) :-
    read(Symptom),
    (
        Symptom \= done ->
        collect_symptoms(RestSymptoms),
        Symptoms = [Symptom | RestSymptoms]
        ;
        Symptoms = []
    ).

% Helper predicate to check if a symptom is incorrect for a condition
incorrect_symptom(Symptom, Condition) :-
    condition(Condition),
    \+ symptom(Symptom),
    not((Condition, \+ symptom(Symptom))).

% Facts related to location (city, state)
location(chicago, illinois).
location(new_york, new_york).
location(boston, massachusetts).
location(miami, florida).

% Facts related to where people stay (person, city)
stays(john, chicago).
stays(susan, new_york).
stays(mike, boston).
stays(lisa, miami).

% Display list of persons, state, and city
display_person_location :-
    stays(Person, City),
    location(City, State),
    format('Person: ~w, State: ~w, City: ~w~n', [Person, State, City]),
    fail.
display_person_location.

% Given a person, find the state in which they are staying
find_state(Person, State) :-
    stays(Person, City),
    location(City, State).

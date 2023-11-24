% Facts
dob(john, '1990-05-15').
dob(amy, '1985-02-20').
dob(mike, '1995-10-08').
dob(lisa, '1980-12-03').
dob(ryan, '1992-07-25').

% Rules

% Query to retrieve the DOB of a specific person given their name.
get_dob(Name, DateOfBirth) :-
    dob(Name, DateOfBirth).

% Query to find all individuals who are older than a certain age.
older_than_30(Name) :-
    dob(Name, DateOfBirth),
    date_of_birth_before(DateOfBirth, '1993-01-01').

% Query to determine who is the youngest person in the database.
youngest_person(Name) :-
    dob(Name, DateOfBirth),
    \+ (dob(_, AnotherDate), date_of_birth_before(AnotherDate, DateOfBirth)).

% Query to check if a specific person is older than another specific person.
older_than(Person1, Person2) :-
    dob(Person1, DateOfBirth1),
    dob(Person2, DateOfBirth2),
    date_of_birth_before(DateOfBirth1, DateOfBirth2).

% Helper rule to compare two dates (in the format 'YYYY-MM-DD').
date_of_birth_before(Date1, Date2) :-
    Date1 @< Date2.




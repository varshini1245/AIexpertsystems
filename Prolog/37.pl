% Predicate to convert Celsius to Fahrenheit
celsius_to_fahrenheit(C, F) :-
    F is (C * 9/5) + 32.

% Predicate to check if a temperature is below freezing (0°C or 32°F)
below_freezing(C) :-
    C < 0.

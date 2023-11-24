% Facts about planets
planet_distance_from_sun(mercury, 0.39).  % Distance from the Sun in AU (1 AU = distance from Earth to the Sun)
planet_mass(mercury, 0.0553).  % Mass in Earth masses

planet_orbital_period(saturn, 29.5).  % Orbital period in Earth years
planet_day_length(saturn, 0.45).  % Day length in Earth days

% Rule to find the distance between two planets based on their positions from the Sun
distance_between_planets(A, B, Distance) :-
    planet_distance_from_sun(A, DistanceA),
    planet_distance_from_sun(B, DistanceB),
    Distance is abs(DistanceA - DistanceB).

closer_to_sun_than_earth(Planet) :-
    planet_distance_from_sun(Planet, Distance),
    planet_distance_from_sun(earth, EarthDistance),
    Distance < EarthDistance.



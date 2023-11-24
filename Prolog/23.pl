% Base case: sum of integers from 1 to 1 is 1.
sum_up_to_n(1, 1).

% Recursive case: sum of integers from 1 to n is n plus the sum of integers from 1 to n-1.
sum_up_to_n(N, Sum) :-
    N > 1,
    Prev is N - 1,
    sum_up_to_n(Prev, PrevSum),
    Sum is N + PrevSum.


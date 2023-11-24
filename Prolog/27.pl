factorial(0, 1).  % Base case: 0! = 1
factorial(N, Result) :-
    N > 0,
    Prev is N - 1,
    factorial(Prev, PrevFactorial),
    Result is N * PrevFactorial.

fibonacci(0, 0).  % Base case: F(0) = 0
fibonacci(1, 1).  % Base case: F(1) = 1
fibonacci(N, Result) :-
    N > 1,
    Prev1 is N - 1,
    Prev2 is N - 2,
    fibonacci(Prev1, FibPrev1),
    fibonacci(Prev2, FibPrev2),
    Result is FibPrev1 + FibPrev2.

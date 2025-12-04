move(1, From, To, _) :-
    format('Move the top disk from ~w to ~w~n', [From, To]).

move(N, From, To, Aux) :-
    N > 1,
    N1 is N - 1,
    move(N1, From, Aux, To),
    move(1, From, To, _),
    move(N1, Aux, To, From).
in_mind([l, o, v, e, l]).


start :- 
    in_mind(Word),
    guess(Word, []).

guess([], _) :- 
    write('Congratulations! The word is '), 
    in_mind(W), 
    write(W), 
    !.


guess(Word, GuessedLetters) :- 
    repeat, in_mind(CorrectWord),
    display_word(CorrectWord, GuessedLetters),
    write('Next letter: '), 
    read(X),
    (   member(X, Word),
        (   \+ member(X, GuessedLetters)  % Verificar que la letra no se haya adivinado antes
    ->  write('OK- ')), 
        append(GuessedLetters, [X], UpdatedGuessedLetters),
        delete(Word, X, RemainingWord),
        guess(RemainingWord, UpdatedGuessedLetters)
    ;   write('Fail. Try again! '), guess(Word, GuessedLetters)
    ).

% Predicado para mostrar la palabra con letras adivinadas y guiones bajos (_) para letras no adivinadas
display_word(Word, CurrentWord) :-
    display_helper(Word, CurrentWord).

display_helper([], _).
display_helper([H | T], CurrentWord) :-
    ( member(H, CurrentWord)
    ->  write(H)
    ;   write('_')
    ),
    display_helper(T, CurrentWord).

print_list([]).
print_list([H | T]) :-
    write(H),
    print_list(T).
    

% Inicializar el sistema con start/0
:- initialization(start).

in_mind([a,h,o,r,c,a,d,o]).


start :- 
    in_mind(Word),
    guess(Word, []).

guess([], _) :- 
    write('Congratulations! The word is '), 
    in_mind(W), 
    write(W), 
    !.


guess(X, Word, GuessedLetters) :- 
    repeat, in_mind(CorrectWord),
    display_word(CorrectWord, GuessedLetters),
    write('Next letter: '), 
    (   member(X, Word),
        (   \+ member(X, GuessedLetters)  % Verificar que la letra no se haya adivinado antes
    ->  write('OK- ')), 
        append(GuessedLetters, [X], UpdatedGuessedLetters),
        delete(Word, X, RemainingWord),
        guess(RemainingWord, UpdatedGuessedLetters)
    ;   write('Fail. Try again! '), guess(Word, GuessedLetters)
    ).
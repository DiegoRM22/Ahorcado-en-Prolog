% Juego de Adivinanza en Prolog
in_mind([l, o, v, e, l]).

start :-
    in_mind(Word),
    guess(Word, []).

guess([], _) :-
    writeln('¡Felicidades! La palabra es:'),
    in_mind(W),
    print_list(W),
    nl, halt.

guess(Word, GuessedLetters) :-
    repeat,
    in_mind(CorrectWord),
    display_word(CorrectWord, GuessedLetters),
    writeln('Próxima letra:'),
    read(X),
    (
        member(X, Word),
        \+ member(X, GuessedLetters),
        writeln('¡Correcto!'),
        append(GuessedLetters, [X], UpdatedGuessedLetters),
        delete(Word, X, RemainingWord),
        guess(RemainingWord, UpdatedGuessedLetters)
    ;
        writeln('¡Incorrecto! Inténtalo de nuevo.'),
        guess(Word, GuessedLetters)
    ).

% Predicado para mostrar la palabra con letras adivinadas y guiones bajos (_) para letras no adivinadas
display_word(Word, CurrentWord) :-
    display_helper(Word, CurrentWord),
    nl.

display_helper([], _).
display_helper([H | T], CurrentWord) :-
    (
        member(H, CurrentWord)
    ->
        write(H)
    ;
        write('_')
    ),
    display_helper(T, CurrentWord).

print_list([]).
print_list([H | T]) :-
    write(H),
    print_list(T).

% Interfaz gráfica en Python utilizando tkinter
:- use_module(library(pyswip)).

init_swipl :-
    assertz(swipl_flag(program, 'path/to/your/prolog/script.pl')),
    swipl.

start_gui :-
    init_swipl,
    tk_new([name('Adivinanza en Prolog')], Toplevel),
    button_new(Toplevel, guess_button, button),
    button_configure(guess_button, [text('Guess'), command='guess_letter']),
    tk_main_loop.

guess_letter :-
    prolog_eval('guess(Word, GuessedLetters), display_word(Word, GuessedLetters).', _).

:- initialization(start_gui).

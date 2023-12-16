in_mind([a,h,o,r,c,a,d,o]).

copy(Word1, Word2) :-
    Word1 = Word2.

start :- 
    in_mind(Word),
    guess(Word, []).

guess([], _).

guess(Word, Input) :-
    member(Input, Word).

erase(Word, Letter) :-
    copy(Aux, Word),
    delete(Aux, Letter, Word).
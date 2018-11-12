## Importing a game from pgn.

Board is a superset of FEN. Board objects have to be created from the full pgn not just from iterative moves made on FEN.

Necessary:
get start Board.
    - make iterative moves.
    - from one state to next, deep copy Board
    - associated metadata: eg FEN 2 - 6.


TODO: can i make member variables private in python??


## Making a move on a Board.
As it is done in chess package. board = game.board() and for each move, we do board.push(move).

So we should have a "move" object.
Verify that a move can be made to a "Board" object.
Multiple ways to make a move.
    - Square to Square
    - Piece to Square.
    - verification need to be done:
        - this is done on a Board - Move leve.


## FEN notes:
1. piece placement: pnbrqk PNBRQK.
    - / separate rank
    - number denotes all empty spaces.
2. active color. w or b
3. castling. KQkq
4. en passant. target if capturable. - empty.
5. halfmove clock. 
6. fullmove clock.




## Game implementation notes: New class or extend chess-python.
#### Pros:
- a light mvp doesn't seem too lengthy to code.
- counterpoint to con 1: a lot of those things are actually out of scope for me: I don't need to check for draw states. This is not a chess *everything* library. This isn't meant to be a library. This is a read-only focused analysis code.
#### Cons:
- a lot of stupid stuff needed to re-implement like game reading. checking for draw states. etc.
- 



## Board implementation:
Instinct was to make a doubly indexed structure so that things such as iterating by file were easy. However, now that a Square(Enum) class has been made, iterating over Squares also seems quite reasonable. so there is an internal way to iterate over Squares.



## When can a piece move?
Check that the following is not true:
    - Move being attempted makes king not in check. This trumps all rules.









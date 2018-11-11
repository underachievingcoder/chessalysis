from enum import Enum, auto
import chess.pgn

# Usage: Piece.W1
class Piece(Enum):
  W1 = auto()
  W2 = auto()
  W3 = auto()
  W4 = auto()
  W5 = auto()
  W6 = auto()
  W7 = auto()
  W8 = auto()
  WP1 = auto()
  WP2 = auto()
  WP3 = auto()
  WP4 = auto()
  WP5 = auto()
  WP6 = auto()
  WP7 = auto()
  WP8 = auto()
  B1 = auto()
  B2 = auto()
  B3 = auto()
  B4 = auto()
  B5 = auto()
  B6 = auto()
  B7 = auto()
  B8 = auto()
  BP1 = auto()
  BP2 = auto()
  BP3 = auto()
  BP4 = auto()
  BP5 = auto()
  BP6 = auto()
  BP7 = auto()
  BP8 = auto()

class PieceType(Enum):
  Pawn = auto()
  Rook = auto()
  Knight = auto()
  Bishop = auto()
  Queen = auto()
  King = auto()

class Square(Enum):
  A1 = auto()
  A2 = auto()
  A3 = auto()
  A4 = auto()
  A5 = auto()
  A6 = auto()
  A7 = auto()
  A8 = auto()
  B1 = auto()
  B2 = auto()
  B3 = auto()
  B4 = auto()
  B5 = auto()
  B6 = auto()
  B7 = auto()
  B8 = auto()
  C1 = auto()
  C2 = auto()
  C3 = auto()
  C4 = auto()
  C5 = auto()
  C6 = auto()
  C7 = auto()
  C8 = auto()
  D1 = auto()
  D2 = auto()
  D3 = auto()
  D4 = auto()
  D5 = auto()
  D6 = auto()
  D7 = auto()
  D8 = auto()
  E1 = auto()
  E2 = auto()
  E3 = auto()
  E4 = auto()
  E5 = auto()
  E6 = auto()
  E7 = auto()
  E8 = auto()
  F1 = auto()
  F2 = auto()
  F3 = auto()
  F4 = auto()
  F5 = auto()
  F6 = auto()
  F7 = auto()
  F8 = auto()
  G1 = auto()
  G2 = auto()
  G3 = auto()
  G4 = auto()
  G5 = auto()
  G6 = auto()
  G7 = auto()
  G8 = auto()
  H1 = auto()
  H2 = auto()
  H3 = auto()
  H4 = auto()
  H5 = auto()
  H6 = auto()
  H7 = auto()
  H8 = auto()

class ChessError(Exception):
  def __init__(self, error_msg):
    self.error_msg = error_msg
    return

class EnumConverter:
  @staticmethod
  def piece_to_pieceType(piece):
    if "P" in piece.name:
      return PieceType.Pawn
    num = piece.name[-1]
    if num == "1" or num == "8":
      return PieceType.Rook
    if num == "2" or num == "7":
      return PieceType.Knight
    if num == "3" or num == "6":
      return PieceType.Bishop
    if num == "4":
      return PieceType.Queen
    return PieceType.King

class Board:
  """A chess Board type is conversion of chess notation: eg H6.
    It is a Dictionary keyed by "A" through "H" that is then indexed (virtually) 1 through 8.
    Empty values are None. Values are Piece.
    type: {str: [Piece]}

    TODO: Decide if I want to add the other thingies.
  """
  ## TODO: what else do I want? eg number of active pieces. 
  def __init__(self, board_input=None):
    """Constructs board that copies the board_input. If None, constructs the starting board."""
    if board_input is None:
      self.board = {
        "A": [Piece.W1, Piece.WP1, None, None, None, None, Piece.BP1, Piece.B1],
        "B": [Piece.W2, Piece.WP2, None, None, None, None, Piece.BP2, Piece.B2],
        "C": [Piece.W3, Piece.WP3, None, None, None, None, Piece.BP3, Piece.B3],
        "D": [Piece.W4, Piece.WP4, None, None, None, None, Piece.BP4, Piece.B4],
        "E": [Piece.W5, Piece.WP5, None, None, None, None, Piece.BP5, Piece.B5],
        "F": [Piece.W6, Piece.WP6, None, None, None, None, Piece.BP6, Piece.B6],
        "G": [Piece.W7, Piece.WP7, None, None, None, None, Piece.BP7, Piece.B7],
        "H": [Piece.W8, Piece.WP8, None, None, None, None, Piece.BP8, Piece.B8],
      }
    else:
      self.board = {}
      for char in "ABCDEFGH":
        col = []
        for i in range(1, 9):
          col[i] = board_input.board[char][i]
          self.board[char] = {col}
    _generate_long_fen()
    return

  def __getitem__(self, Square_square):
    """Example usage: board_object[Square.A4]
    """
    try:
      return self.board[Square_square.name[0]][int(Square_square.name[1])-1]
    except _:
      raise ChessError("Improper chess algebraic notation")

  def _generate_long_fen(self):
    self.
    # TODO

  def get(self, char, index):
    if len(char) != 1 or char not in "ABCDEFGH" or index not in range(1, 9):
      return False  # TODO: more robust checking.
    return self.board[char][index - 1]

  # Need more complex moving functions
  def move(self, char_from, index_from, char_to, index_to):
    if len(char_from) != 1 or char_from not in "ABCDEFGH" or index_from not in range(1, 9):
      return False  # TODO: more robust checking.
    if len(char_to) != 1 or char_to not in "ABCDEFGH" or index_to not in range(1, 9):
      return False  # TODO: more robust checking.
    self.board[char_to][index_to] = self.board[char_from][index_from]
    self.board[char_from][index_from] = None
    return

  @staticmethod
  def _board_to_fen(dict_list_pieces):
    # TODO

  @staticmethod
  def fen_to_board(str_fen):
    """Given a pgn in string format, creates a Board object.

        Throws exceptions for badly handled games.
    str_fen: str. Can be full FEN or just board position. If latter, TODO: defaults.
    rtype: Board.
    """
    # TODO: implement
    return
    long_fen = str_fen.split()
    if len(long_fen) != 1 or len(long_fen) != 6:
      raise ChessError("Bad input FEN")
    




class Game:
  """A full chess game is a sequence of boards.
    Design decision to have full boards since storage is not limited factor. Easier way to iterate boards.
  """
  def __init__(self, pgn=None):  # can give it a pgn.
    if pgn is None:
      self.boards = []
      self.tags = {tag: None for tag in PGN.METADATA_TAGS_LIST}
      return

  def _set_tags(self, tags):
    """tags: dict{str: str}.
    """
    self.tags = {}
    for tag in PGN.METADATA_TAGS_LIST:
      if tag in tags:
        self.tags = tags[tag]
    return

  def _set_boards(self, iter_boards):  # purposefully uses [] instead of queue to index games. Maybe slow?
    self.boards = []
    for each in iter_boards:
      self.boards.append(each)
    return

  @staticmethod
  def construct_from_pgn(str_fname):
    """
    rtype: Game
    """
    tags = {}
    (metadata, iter_boards) = PGN.pgn_to_game(str_fname)
    for tag in PGN.METADATA_TAGS_LIST:
      tags[tag] = metadata[tag]
    new_game = Game()
    new_game._set_tags(tags)
    new_game._set_boards(iter_boards)
    return(new_game)

    



class PGN:
  """PGN analyzer class with helper functions
  """
  METADATA_TAGS_LIST = [
    "Event",
    "Site",
    "Date",
    "Round",
    "White",
    "Black",
    "WhiteElo",
    "BlackElo",
    "Result",
  ]

  @staticmethod
  def pgn_to_game(str_fname):
    """Returns metadata and iterator of Board objects from input pgn file.
    rtype: tuple(dict{str: str}, iter(Board))
    """
    relevant_metadata = {}
    boards = []
    with open(str_fname) as pgn:
      game = chess.pgn.read_game(pgn)
      for tag in relevant_metadata:
        if tag in game.headers:
          relevant_metadata[tag] = game.headers[tag]
      board = game.board()
      boards.append(Board.fen_to_board(board.board_fen()))
      for move in game.main_line():
        board.push(move)
        boards.append(Board.fen_to_board(board.board_fen()))
      return (relevant_metadata, boards)
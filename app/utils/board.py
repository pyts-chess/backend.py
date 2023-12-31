from typing import Literal, List, Dict

from utils import (
    FILES,
    LABELED_BOARD,
    POSITION_IDX,
    RANKS,
    SQUARE_TYPE,
    STARTING_POSITION,
    PieceColor,
    PieceName,
    PieceTypes,
)
from utils.piece import Bishop, ChessPiece, King, Knight, Pawn, Queen, Rook
from utils.player import Player


class ChessBoard:
    def __init__(self) -> None:
        self.position: List[List[None | ChessPiece]] = [
            [None for _ in range(8)] for _ in range(8)
        ]
        self.squares = LABELED_BOARD

    def setup(self) -> None:
        piece: PieceName
        positions_by_color: Dict[PieceColor, List[str]]
        color: PieceColor
        positions: List[str]
        square: SQUARE_TYPE

        for piece, positions_by_color in STARTING_POSITION.items():
            for color, positions in positions_by_color.items():
                for square in positions:
                    if square[1] in ("3", "4", "5", "6"):
                        continue

                    sqr_idxs = self.get_index_of_square(square)
                    rank = sqr_idxs["rank"]
                    file = sqr_idxs["file"]

                    new_piece = PieceTypes[piece](color)

                    self.position[rank][file] = new_piece

    def get_index_of_square(
        self, square: SQUARE_TYPE
    ) -> Dict[Literal["file", "rank"], int]:
        """
        Takes square (A1-H8)
        Returns List[int] pointing to specific board position
        NOTE: Base format is File + Rank | Position array requires indexing Rank prior to File
        """
        rank = 7 - RANKS.index(square[1])  # 7 for idx offset
        file = FILES.index(square[0])

        return {"file": file, "rank": rank}

    def _get_square_of_index(self, rank: POSITION_IDX, file: POSITION_IDX) -> str:
        """
        Takes List[2 idxs] (rank, file)
        Returns square (A1-H8)
        """
        square = self.squares[rank][file]
        return square

    def _is_square_occupied(self, square: SQUARE_TYPE) -> bool | ChessPiece:
        sqr_idxs = self.get_index_of_square(square)

        rank = sqr_idxs["rank"]
        file = sqr_idxs["file"]

        return self.position[rank][file] is not None

    def _is_square_occupied_by_oppenent(
        self, player: Player, square: SQUARE_TYPE
    ) -> bool | ChessPiece:
        """
        T/F or Piece if belongs to player who's moving
        """
        sqr_idxs = self.get_index_of_square(square)

        rank = sqr_idxs["rank"]
        file = sqr_idxs["file"]

        piece = self.position[rank][file]

        # TODO Maybe fix: Currently returns either Piece on specific square or True (meaning opp is on square)
        if not isinstance(piece, ChessPiece):
            return False
            # Returns Piece object if it's Player's own piece else TRUE -> refering to square is occupied
        return piece if not piece.color == player.color else True


    def display(self):
        ...

    def move_piece(self):
        ...

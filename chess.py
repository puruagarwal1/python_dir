import itertools

WHITE = "white"
BLACK = "black"


class Piece:
    def __init__(self, color, name):
        self.name = name
        self.position = None
        self.color = color

    def is_valid(self, start_pos, end_pos, color, gameboard):
        if end_pos in self.available_moves(start_pos[0], start_pos[1], gameboard, color=color):
            return True
        return False

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def available_moves(self, x, y, gameboard, color=None):
        print("ERROR: no movement for base class")

    def ad_nauseum(self, x, y, gameboard, color, intervals):
        answers = []
        for x_int, y_int in intervals:
            x_temp, y_temp = x + x_int, y + y_int
            while self.is_in_bounds(x_temp, y_temp):
                target = gameboard.get((x_temp, y_temp), None)
                if target is None:
                    answers.append((x_temp, y_temp))
                elif target.color != color:
                    answers.append((x_temp, y_temp))
                    break
                else:
                    break
                x_temp, y_temp = x_temp + x_int, y_temp + y_int
        return answers

    def is_in_bounds(self, x, y):
        if 0 <= x < 8 and 0 <= y < 8:
            return True
        return False

    def no_conflict(self, gameboard, initial_color, x, y):
        if self.is_in_bounds(x, y) and ((x, y) not in gameboard or gameboard[(x, y)].color != initial_color):
            return True
        return False


class Knight(Piece):
    def available_moves(self, x, y, gameboard, color=None):
        if color is None:
            color = self.color
        return [(xx, yy) for xx, yy in knight_list(x, y, 2, 1) if self.no_conflict(gameboard, color, xx, yy)]


class Rook(Piece):
    def available_moves(self, x, y, gameboard, color=None):
        if color is None:
            color = self.color
        return self.ad_nauseum(x, y, gameboard, color, chess_cardinals)


class Bishop(Piece):
    def available_moves(self, x, y, gameboard, color=None):
        if color is None:
            color = self.color
        return self.ad_nauseum(x, y, gameboard, color, chess_diagonals)


class Queen(Piece):
    def available_moves(self, x, y, gameboard, color=None):
        if color is None:
            color = self.color
        return self.ad_nauseum(x, y, gameboard, color, chess_cardinals + chess_diagonals)


class King(Piece):
    def available_moves(self, x, y, gameboard, color=None):
        if color is None:
            color = self.color
        return [(xx, yy) for xx, yy in king_list(x, y) if self.no_conflict(gameboard, color, xx, yy)]


class Pawn(Piece):
    def __init__(self, color, name, direction):
        self.name = name
        self.color = color
        self.direction = direction

    def available_moves(self, x, y, gameboard, color=None):
        if color is None:
            color = self.color
        answers = []
        if (x + 1, y + self.direction) in gameboard and self.no_conflict(gameboard, color, x + 1, y + self.direction):
            answers.append((x + 1, y + self.direction))
        if (x - 1, y + self.direction) in gameboard and self.no_conflict(gameboard, color, x - 1, y + self.direction):
            answers.append((x - 1, y + self.direction))
        if (x, y + self.direction) not in gameboard and color == self.color:
            answers.append((x, y + self.direction))
        return answers


class Game:
    def __init__(self):
        self.players_turn = BLACK
        self.message = "This is where prompts will go"
        self.gameboard = {}
        self.place_pieces()
        print("Chess program. Enter moves in algebraic notation separated by space")
        self.main()

    def place_pieces(self):
        for i in range(8):
            self.gameboard[(i, 1)] = Pawn(WHITE, uni_dict[WHITE][Pawn], 1)
            self.gameboard[(i, 6)] = Pawn(BLACK, uni_dict[BLACK][Pawn], -1)

        placers = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for i in range(8):
            self.gameboard[(i, 0)] = placers[i](WHITE, uni_dict[WHITE][placers[i]])
            self.gameboard[((7 - i), 7)] = placers[i](BLACK, uni_dict[BLACK][placers[i]])
        placers.reverse()

    def main(self):
        while True:
            self.print_board()
            print(self.message)
            self.message = ""
            start_pos, end_pos = self.parse_input()
            try:
                target = self.gameboard[start_pos]
            except KeyError:
                self.message = "Could not find piece; index probably out of range"
                target = None

            if target:
                print("Found " + str(target))
                if target.color != self.players_turn:
                    self.message = "You aren't allowed to move that piece this turn"
                    continue
                if target.is_valid(start_pos, end_pos, target.color, self.gameboard):
                    self.message = "That is a valid move"
                    self.gameboard[end_pos] = self.gameboard[start_pos]
                    del self.gameboard[start_pos]
                    self.is_check()
                    if self.players_turn == BLACK:
                        self.players_turn = WHITE
                    else:
                        self.players_turn = BLACK
                else:
                    self.message = "Invalid move" + str(target.available_moves(start_pos[0], start_pos[1], self.gameboard))
                    print(target.available_moves(start_pos[0], start_pos[1], self.gameboard))
            else:
                self.message = "There is no piece in that space"

    def is_check(self):
        king = King
        king_dict = {}
        piece_dict = {BLACK: [], WHITE: []}
        for position, piece in self.gameboard.items():
            if isinstance(piece, King):
                king_dict[piece.color] = position
            print(piece)
            piece_dict[piece.color].append((piece, position))
        if self.can_see_king(king_dict[WHITE], piece_dict[BLACK]):
            self.message = "White player is in check"
        if self.can_see_king(king_dict[BLACK], piece_dict[WHITE]):
            self.message = "Black player is in check"

    def can_see_king(self, king_pos, piece_list):
        for piece, position in piece_list:
            if piece.is_valid(position, king_pos, piece.color, self.gameboard):
                return True

    def parse_input(self):
        try:
            a, b = input().split()
            a = ((ord(a[0]) - 97), int(a[1]) - 1)
            b = (ord(b[0]) - 97, int(b[1]) - 1)
            print(a, b)
            return a, b
        except ValueError:
            print("Error decoding input. Please try again")
            return ((-1, -1), (-1, -1))

    def print_board(self):
        print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
        for i in range(8):
            print("-" * 32)
            print(chr(i + 97), end="|")
            for j in range(8):
                item = self.gameboard.get((i, j), " ")
                print(str(item) + ' |', end=" ")
            print()
        print("-" * 32)


chess_cardinals = [(1, 0), (0, 1), (-1, 0), (0, -1)]
chess_diagonals = [(1, 1), (-1, 1), (1, -1), (-1, -1)]


def knight_list(x, y, int1, int2):
    return [(x + int1, y + int2), (x - int1, y + int2), (x + int1, y - int2), (x - int1, y - int2),
            (x + int2, y + int1), (x - int2, y + int1), (x + int2, y - int1), (x - int2, y - int1)]


def king_list(x, y):
    return [(x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x, y + 1), (x, y - 1), (x - 1, y), (x - 1, y + 1), (x - 1, y - 1)]


uni_dict = {
    WHITE: {Pawn: "♙", Rook: "♖", Knight: "♘", Bishop: "♗", King: "♔", Queen: "♕"},
    BLACK: {Pawn: "♟", Rook: "♜", Knight: "♞", Bishop: "♝", King: "♚", Queen: "♛"}
}

Game()


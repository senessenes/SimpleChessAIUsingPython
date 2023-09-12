import chess
import math
import chess.polyglot
import random
class Game():
    def __init__(self):
        self.board=chess.Board()
        self.num_played_moves=0
        self.turn="w"
        self.boards=[]
        self.takes=[]
        self.checks=[]
        self.converted_board=[['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'], ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'], ['--', '--', '--', '--', '--', '--', '--', '--'], ['--', '--', '--', '--', '--', '--', '--', '--'], ['--', '--', '--', '--', '--', '--', '--', '--'], ['--', '--', '--', '--', '--', '--', '--', '--'], ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'], ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]



        #Creating sample boards for finding the best place for a piece in the chess board.
        self.knight_point_board=[
            [1, 2, 2, 2, 2, 2, 2, 1],
            [2,2,2,5,5,2,2,1],
            [3,4,5,4,4,5,4,3],
            [3,4,6,8,8,6,4,3],
            [3,4,6,8,8,6,4,3],
            [3,4,5,4,4,5,4,3],
            [2,2,2,5,5,2,2,1],
            [1,2,2,2,2,2,2,1]]

        self.white_pawn_point_board = [[10,10, 10, 11, 11, 10, 10, 10],
                                   [0, 1, 3, 3, 3, 3, 1, 0],
                                   [0, 1, 1, 1, 1, 1, 1,0],
                                   [0, 3, 6, 9, 9, 6, 3,0],
                                   [0, 3, 6, 9, 9, 9, 3, 0],
                                   [0, 3, 6, 7, 7, 6, 3,0],
                                    [0, 1, 3, 3, 3, 3, 1, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0]]
        self.black_pawn_point_board = [[0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 1, 3,3, 3, 3, 1, 0],
                                       [0, 3, 6, 7, 7, 6, 3, 0],
                                       [0, 3, 6, 9, 9, 6, 3, 0],
                                        [0, 3, 6, 9, 9, 6, 3,0],
                                       [0, 1, 1, 1, 1, 1, 1, 0],
                                       [0, 1, 3, 3, 3, 3, 1, 0],
                                   [10,10, 10, 11, 11, 10, 10, 10]]

        self.white_bishop_point_board =              [[3, 3, 3, 3, 3, 3, 3, 3],
                                   [3, 4, 4, 4, 4, 4, 4, 4],
                                   [4, 5, 5, 8, 8, 5, 6, 4],
                                   [4, 5, 7, 5, 5, 7, 5, 4],
                                   [4, 5, 7, 5, 5, 7, 5, 4],
                                   [4, 5, 5, 6, 6, 5, 5, 4],
                                   [4, 5, 5, 5, 5, 5, 5, 4],
                                   [4, 4, 4, 4, 4, 4, 4,4], ]
        self.black_bishop_point_board =  [[4, 4, 4, 4, 4, 4, 4,4],
                                        [4, 5, 5, 5, 5, 5, 5, 4],
                                        [4, 5, 5, 6, 6, 5, 5, 4],
                                          [4, 5, 7, 5, 5, 7, 5, 4],
                                        [4, 5, 7, 5, 5, 7, 5, 4],
                                        [4, 5, 5, 8, 8, 5, 6, 4],
                                        [3, 4, 4, 4, 4, 4, 4, 4],
                                        [3, 3, 3, 3, 3, 3, 3, 3]]
        self.white_king_point_board = [[0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0,0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0],
                                         [1, 1, 1, 1, 1, 1, 1, 1],
                                         [3, 3, 3, 1, 1, 3, 3, 3],
                                         [3, 5, 5, 2, 2, 3, 5, 5], ]
        self.black_king_point_board = [ [3, 5, 5, 2, 2, 3, 5, 5],
                                        [3, 3, 3, 1, 1, 3, 3, 3],
                                        [1, 1, 1, 1, 1, 1, 1, 1],
                                       [0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0],
                                        ]
        self.king_endgame_point_board= [ [1, 1, 1, 1, 1, 1, 1, 1],
                                        [1, 2, 2, 2, 2, 2, 2, 1],
                                        [1, 2, 3, 3, 3, 3, 2, 1],
                                       [1, 2, 3, 4, 4, 3, 2,1],
                                       [1, 2, 3, 4, 4, 3, 2, 1],
                                       [1, 2, 3, 3, 3, 3, 2, 1],
                                       [1, 2, 2, 2, 2, 2, 2, 1],
                                       [1, 1, 1, 1, 1, 1, 1, 1],
                                        ]
        self.rook_point_board =         [[1, 2, 4, 5, 5, 4, 2, 1],
                                         [1, 2, 4, 5, 5, 4, 2, 1],
                                         [1, 2, 4, 5, 5, 4, 2, 1],
                                         [1, 2, 4, 5, 5, 4, 2, 1],
                                         [1, 2, 4, 5, 5, 4, 2, 1],
                                         [1, 2, 4, 5, 5, 4, 2, 1],
                                         [1, 2, 4, 5, 5, 4, 2, 1],
                                         [1, 2, 4, 5, 5, 4, 2, 1],
                                         ]
        self.white_queen_point_board_middlegame=[[8, 9, 11, 12, 12, 11, 9, 8],
                                         [7, 8, 10, 11, 11, 10, 8, 7],
                                         [6, 7, 9, 10, 10, 9, 7, 6],
                                         [5, 6, 8, 9, 9, 8, 6, 5],
                                         [4,5, 7, 8, 8, 7, 5, 4],
                                         [3, 4, 6, 7, 7, 6, 4, 3],
                                         [2, 3, 5, 6, 6, 5, 3, 2],
                                         [1, 2, 4, 5, 5, 4, 2, 1],
                                         ]
        self.black_queen_point_board_middlegame=[[1, 2, 4, 5, 5, 4, 2, 1],
                                      [2, 3, 5, 6, 6, 5, 3, 2],
                                      [3, 4, 6, 7, 7, 6, 4, 3],
                                      [4, 5, 7, 8, 8, 7, 5, 4],
                                       [5, 6, 8, 9, 9, 8, 6, 5],
                                      [6, 7, 9, 10, 10, 9, 7, 6],
                                      [7, 8, 10, 11, 11, 10, 8, 7],
                                      [8, 9, 11, 12, 12, 11, 9, 8],
                                         ]
        self.white_queen_point_board_opening = [
                                        [-10, -10, -10, -10, -10, -10, -10, -10],
                                        [-10, -10, -10, -10, -10, -10, -10, -10],
                                        [-10, -10, -10, -10, -10, -10, -10, -10],
                                       [-10, -10, -10, -10, -10, -10, -10, -10],
                                       [-5, -5, -5, -5, -5, -5, -5, -5],
                                       [-5, -5, -5, -5, -5, -5, -5, -5],
                                       [-5, -5, -5, 5, 4, 3, -5, -5],
                                       [-5, -5, -5, 4, 0, 0, 0, 0],]
        self.black_queen_point_board_opening = [[-5, -5, -5, 4, 0, 0, 0, 0],
                                                [-5, -5, -5, 5, 4, 3, -5, -5],
                                                [-5, -5, -5, -5, -5, -5, -5, -5],
                                                [-5, -5, -5, -5, -5, -5, -5, -5],
                                                [-10, -10, -10, -10, -10, -10, -10, -10],
                                                [-10, -10, -10, -10, -10, -10, -10, -10],
                                                [-10, -10, -10, -10, -10, -10, -10, -10],
                                                [-10, -10, -10, -10, -10, -10, -10, -10],]

    #A function for findin all the possible moves
    def actions(self):
        moves=list(self.board.generate_legal_moves())
        return moves
    def book(self):
        moves=[]
        with chess.polyglot.open_reader("data/opening_book.bin") as reader:
             for entry in reader.find_all(self.board):
                 moves.append(entry.move)
        return moves

    #A function which returns the winner if there is one or "=" if it is draw else False
    def winner(self):

        if self.board.is_checkmate():

            if(self.board.fen()[-9]=="w"):
                return "b"
            else:
                return "w"
        elif self.board.is_fifty_moves() or self.board.is_fivefold_repetition() or self.board.is_insufficient_material():
            return "="
        return False

    #A function for making the move and switching the turn
    def play_move(self,move,is_user_move):


        if not(is_user_move):
            self.board.push(move)
            str_move=str(move)



            converted_move=self.move_conversion(move)
            piece=converted_move[0]
            target=converted_move[1]

            self.converted_board[piece[1]][piece[0]],self.converted_board[target[1]][target[0]]=self.converted_board[target[1]][target[0]],self.converted_board[piece[1]][piece[0]]
            if str_move == "e1g1":
                self.converted_board[7][7], self.converted_board[7][5] = \
                self.converted_board[7][5], self.converted_board[7][7]
            elif str_move=="e1c1":
                self.converted_board[7][0], self.converted_board[7][2] = \
                self.converted_board[7][2], self.converted_board[7][0]
            elif str_move == "e8g8":
                self.converted_board[0][7], self.converted_board[0][5] = \
                self.converted_board[0][5], self.converted_board[0][7]
            elif str_move=="e8c8":
                self.converted_board[0][0], self.converted_board[0][2] = \
                self.converted_board[0][2], self.converted_board[0][0]
            if(self.turn=="w"):


                self.turn="b"
            else:
                self.turn="w"
        else:

            self.board.push(chess.Move.from_uci(move))
            converted_move = self.move_conversion(move)
            piece = converted_move[0]
            target = converted_move[1]
            str_move = str(move)

            self.converted_board[piece[1]][piece[0]], self.converted_board[target[1]][target[0]] = self.converted_board[target[1]][target[0]], self.converted_board[piece[1]][piece[0]]
            if str_move == "e1g1":
                self.converted_board[7][7], self.converted_board[7][5] = \
                self.converted_board[7][5], self.converted_board[7][7]
            elif str_move=="e1c1":
                self.converted_board[7][0], self.converted_board[7][2] = \
                self.converted_board[7][2], self.converted_board[7][0]
            elif str_move == "e8g8":
                self.converted_board[0][7], self.converted_board[0][5] = \
                self.converted_board[0][5], self.converted_board[0][7]
            elif str_move=="e8c8":
                self.converted_board[0][0], self.converted_board[0][2] = \
                self.converted_board[0][2], self.converted_board[0][0]




            self.turn = "b"
        self.num_played_moves+=1

    #A function for converting FEN's of chess boards into matrixes
    #def convert_to_list(self,fen):
    #
    #
    #
    #    board = []
    #    for row in fen.split('/'):
    #        brow = []
    #        for c in row:
    #            if c == ' ':
    #                break
    #            elif c in '12345678':
    #                brow.extend(['--'] * int(c))
    #            elif c == 'p':
    #                brow.append('bp')
    #            elif c == 'P':
    #                brow.append('wp')
    #            elif c > 'Z':
    #                brow.append('b' + c.upper())
    #            else:
    #                brow.append('w' + c)
    #
    #        board.append(brow)
    #    return board
    #




    #The function which calculates the materials and adjusting the values according to where they should be placed
    def material_eval(self):
        materialw = 0
        materialb = 0

        for i in range(1, 6):

            if (i == 2):
                materialw += len(self.board.pieces(piece_type=i, color=True)) * 3
                materialb -= len(self.board.pieces(piece_type=i, color=False)) * 3

            elif (i == 4):
                materialw += len(self.board.pieces(piece_type=i, color=True)) * 5
                materialb -= len(self.board.pieces(piece_type=i, color=False)) * 5
            elif (i == 5):
                materialw += len(self.board.pieces(piece_type=i, color=True)) * 9
                materialb -= len(self.board.pieces(piece_type=i, color=False)) * 9

            else:
                materialw += len(self.board.pieces(piece_type=i, color=True)) * i
                materialb -= len(self.board.pieces(piece_type=i, color=False)) * i



        for x in range(0,len(self.converted_board)):
            for y in range(0,len(self.converted_board[x])):
                if self.converted_board[x][y]=="wN":
                    materialw+=self.knight_point_board[x][y]/40
                elif self.converted_board[x][y]=="bN":
                    materialb -= self.knight_point_board[x][y] / 40
                elif self.converted_board[x][y]=="wp":
                    materialw+=self.white_pawn_point_board[x][y]/40
                elif self.converted_board[x][y]=="bp":
                    materialb-=self.black_pawn_point_board[x][y]/40
                elif self.converted_board[x][y] == "wB":
                    materialw += self.white_bishop_point_board[x][y] / 40

                elif self.converted_board[x][y] == "bB":
                    materialb -= self.black_bishop_point_board[x][y] / 40





            
                elif self.converted_board[x][y] == "wK":
                    materialw += self.white_king_point_board[x][y] / 40
                elif self.converted_board[x][y] == "bK":
                    materialb -= self.black_king_point_board[x][y] / 40

            
            

            

        return materialw + materialb

    #A function for undoing the move(used in minimax algorithm)
    def undo_move(self,last_fen):

        self.board.set_fen(last_fen)
        if(self.turn=="b"):
            self.turn = "w"

        else:
            self.turn="b"
        self.num_played_moves-=1

    #The function for ordering the moves for better alpha-beta pruning:1-Checking moves,2-Taking moves,3-Other moves
    def order_moves(self,actions):
        self.takes=[]
        self.checks=[]


        normal_moves=[]
        ordered_actions=[]
        last_fen = self.board.fen()
        material_eval=self.material_eval()

        for action in actions:


            self.play_move(action,False)

            if self.board.is_check():
                self.checks.append(action)
            elif self.material_eval()-material_eval<=-0.8:
                self.takes.append(action)
            else:
                normal_moves.append(action)

            self.undo_move(last_fen)

        ordered_actions+=self.checks
        ordered_actions+=self.takes
        ordered_actions+=normal_moves

        return ordered_actions

    #Returns an integer according to the winner
    def utility(self):
        winner=self.winner()
        if winner=="w":
            return math.inf
        elif winner=="b":
            return -math.inf
        return self.material_eval()
    def move_conversion(self,move):
        letters=["a","b","c","d","e","f","g","h"]
        numbers=["8","7","6","5","4","3","2","1"]
        str_move=str(move)


        piece=str_move[0]+str_move[1]

        target=str_move[2]+str_move[3]

        converted_piece=[]
        converted_target=[]
        for letter in range(0,len(letters)):
            if letters[letter]==piece[0]:

                converted_piece.append(letter)
            if letters[letter]==target[0]:
                converted_target.append(letter)
            if len(converted_piece)>0 and len(converted_target)>0:
                break
        for number in range(0,len(numbers)):
            if numbers[number]==piece[1]:

                converted_piece.append(number)
            if numbers[number]==target[1]:
                converted_target.append(number)
            if len(converted_piece)>1 and len(converted_target)>1:
                break
        return [converted_piece,converted_target]





    #The algorithm
    def minimax(self,depth,alpha,beta):
        best_move=None


        if depth<=0 or not(self.winner()==False):

            return self.utility(),None

        if self.turn=="w":


            best_score=-math.inf

            moves=self.order_moves(self.actions())
            for move in moves:

                last_fen=self.board.fen()



                self.play_move(move,False)
                if move in self.takes or move in self.checks:

                    score = self.minimax(depth, alpha, beta)[0]
                else:
                    score = self.minimax(depth - 1, alpha, beta)[0]

                alpha=max(alpha,score)


                self.undo_move(last_fen)

                if(score>best_score):
                    best_score=score
                    best_move=move
                if (beta <= alpha):
                    break


            return best_score,best_move
        else:

            best_score = math.inf
            best_move = None
            moves=self.order_moves(self.actions())
            for move in moves:
                last_fen=self.board.fen()



                self.play_move(move,False)
                if move in self.takes or move in self.checks:


                    score = self.minimax(depth, alpha, beta)[0]
                else:
                    score = self.minimax(depth - 1, alpha, beta)[0]




                beta=min(beta,score)


                self.undo_move(last_fen)

                if (score < best_score):
                    best_score = score
                    best_move = move
                if (beta <= alpha):
                    break

            return best_score, best_move

DEPTH=4
def main():
    game = Game()
    while not(game.winner()):





        print(game.turn)
        print(game.board)
        print(game.num_played_moves)
        move = input("Your move...")
        game.play_move(move, True)
        game.last_fen = game.board.fen()
        book_moves=game.book()
        print("AI is thinking...")
        if len(book_moves)>0:
            aimove=random.choice(book_moves)
            eval="Book"
        else:
            minimax = game.minimax(DEPTH, -math.inf, math.inf)
            aimove = minimax[1]
            eval=minimax[0]
        print("Eval:", eval)

        game.last_fen = game.board.fen()
        print(aimove)
        game.play_move(aimove, False)








    if(game.winner()=="w"):
        print("Congratulations you won")
    elif(game.winner()=="b"):
        print("AI won")
    else:print("Draw")

main()





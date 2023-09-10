import chess
import math
class Game():
    def __init__(self):
        self.board=chess.Board()
        self.counter=0
        self.turn="w"
        self.boards=[]
        self.knight_point_board=[[2,3,4,4,4,4,3,2],
                                 [3,4,6,6,6,6,4,3],
                                 [4,6,8,8,8,8,6,4],
                                 [4,6,8,10,10,8,6,4],
                                 [4,6,8,10,10,8,6,4],
                                 [4,6,8,8,8,8,6,4],
                                 [3,4,6,6,6,6,4,3],
                                 [2,3,4,4,4,4,3,2]]
        self.white_pawn_point_board = [[9,10, 10, 11, 11, 10, 10, 9],
                                   [1, 4, 6, 6, 6, 6, 4, 1],
                                   [1, 6, 6, 6, 6, 6, 6, 1],
                                   [1, 6, 6, 12, 12, 6, 6,1],
                                   [1, 6, 9, 12, 12, 9, 6,1],
                                   [1, 6, 9, 10, 10, 9, 6, 1],
                                   [1, 4, 6, 6, 6, 6, 6, 1],
                                   [0, 0, 0, 0, 0, 0, 0, 0]]
        self.black_pawn_point_board = [[0, 0, 0, 0, 0, 0, 0, 0],
                                   [1, 4, 6, 6, 6, 6, 4, 1],
                                   [1, 6, 6, 6, 6, 6, 6, 1],
                                   [1, 6, 6, 12, 12, 6, 6,1],
                                   [1, 6, 9, 12, 12, 9, 6,1],
                                   [1, 6, 9, 10, 10, 9, 6, 1],
                                   [1, 4, 6, 6, 6, 6, 6, 1],
                                   [9,10, 10, 11, 11, 10, 10, 9]]

        self.white_bishop_point_board =              [[8, 8, 8, 8, 8, 8, 8, 8],
                                   [8, 9, 9, 9, 9, 9, 9, 8],
                                   [8, 9, 9, 12, 12, 9, 10, 8],
                                   [8, 9, 11, 9, 9, 11, 9, 8],
                                   [8, 9, 11, 9, 9, 11, 9, 8],
                                   [8, 9, 9, 10, 10, 9, 9, 8],
                                   [8, 9, 9, 9, 9, 9, 9, 8],
                                   [8, 8, 8, 8, 8, 8, 8, 8], ]
        self.black_bishop_point_board = [[8, 8, 8, 8, 8, 8, 8, 8],
                                         [8, 9, 9, 9, 9, 9, 9, 8],
                                         [8, 9, 9, 10, 10, 9, 10, 8],
                                         [8, 9, 11, 9, 9, 11, 9, 8],
                                         [8, 9, 11, 9, 9, 11, 9, 8],
                                         [8, 9, 9, 12, 12, 9, 9, 8],
                                         [8, 9, 9, 9, 9, 9, 9, 8],
                                         [8, 8, 8, 8, 8, 8, 8, 8], ]
        self.white_king_point_board = [[0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0,0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0],
                                         [1, 1, 1, 1, 1, 1, 1, 1],
                                         [3, 3, 3, 2, 2, 3, 3, 3],
                                         [3, 5, 5, 2, 2, 3, 5, 5], ]
        self.black_king_point_board = [ [3, 5, 5, 2, 2, 3, 5, 5],
                                        [3, 3, 3, 2, 2, 3, 3, 3],
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

    def actions(self):
        moves=list(self.board.generate_legal_moves())
        return moves
    def winner(self):

        if self.board.is_checkmate():

            if(self.board.fen()[-9]=="w"):
                return "b"
            else:
                return "w"
        elif self.board.is_fifty_moves() or self.board.is_fivefold_repetition() or self.board.is_insufficient_material():
            return "="
        return False
    def play_move(self,move,is_user_move):


        if not(is_user_move):
            self.board.push(move)
            self.boards.append(self.board)


            if(self.turn=="w"):


                self.turn="b"
            else:
                self.turn="w"
        else:

            self.board.push_san(move)
            self.boards.append(self.board)



            self.turn = "b"

    def convert_to_list(self,fen):



        board = []
        for row in fen.split('/'):
            brow = []
            for c in row:
                if c == ' ':
                    break
                elif c in '12345678':
                    brow.extend(['--'] * int(c))
                elif c == 'p':
                    brow.append('bp')
                elif c == 'P':
                    brow.append('wp')
                elif c > 'Z':
                    brow.append('b' + c.upper())
                else:
                    brow.append('w' + c)

            board.append(brow)
        return board





    def material_eval(self):
        materialw = 0
        materialb = 0

        for i in range(1, 6):

            if (i == 2):
                materialw += len(self.board.pieces(piece_type=i, color=True)) * 3

            elif (i == 4):
                materialw += len(self.board.pieces(piece_type=i, color=True)) * 5
            elif (i == 5):
                materialw += len(self.board.pieces(piece_type=i, color=True)) * 9

            else:
                materialw += len(self.board.pieces(piece_type=i, color=True)) * i
        for i in range(1, 6):

            if (i == 2):
                materialb -= len(self.board.pieces(piece_type=i, color=False)) * 3

            elif (i == 4):
                materialb -= len(self.board.pieces(piece_type=i, color=False)) * 5
            elif (i == 5):
                materialb -= len(self.board.pieces(piece_type=i, color=False)) * 9
            else:
                materialb -= len(self.board.pieces(piece_type=i, color=False)) * i
        current_board=self.convert_to_list(self.board.fen())
        for x in range(0,len(current_board)):
            for y in range(0,len(current_board[x])):
                if current_board[x][y]=="wN":
                    materialw+=self.knight_point_board[x][y]/24
                elif current_board[x][y]=="bN":
                    materialb -= self.knight_point_board[x][y] / 24
                elif current_board[x][y]=="wp":
                    materialw+=self.white_pawn_point_board[x][y]/24
                elif current_board[x][y]=="bp":
                    materialb-=self.black_pawn_point_board[x][y]/24
                elif current_board[x][y] == "wB":
                    materialw += self.white_bishop_point_board[x][y] / 24

                elif current_board[x][y] == "bB":
                    materialb -= self.black_bishop_point_board[x][y] / 24
                elif materialw+(-materialb)<=30 :
                    if current_board[x][y] == "wK":
                        materialw += self.king_endgame_point_board[x][y] / 12
                    elif current_board[x][y] == "bK":
                        materialb -= self.king_endgame_point_board[x][y] / 12

                elif current_board[x][y] == "wK":
                    materialw += self.white_king_point_board[x][y] / 12
                elif current_board[x][y] == "bK":
                    materialb -= self.black_king_point_board[x][y] / 12



        return materialw + materialb
    def undo_move(self,last_fen):
        self.boards.remove(self.board)
        self.board.set_fen(last_fen)
        if(self.turn=="b"):
            self.turn = "w"

        else:
            self.turn="b"
    def order_moves(self,actions):
        checks=[]
        takes=[]
        normal_moves=[]
        ordered_actions=[]
        last_fen = self.board.fen()
        material_eval=self.material_eval()

        for action in actions:


            self.play_move(action,False)

            if self.board.is_check():
                checks.append(action)
            elif self.material_eval()>material_eval:
                takes.append(action)
            else:
                normal_moves.append(action)

            self.undo_move(last_fen)
        for move in checks:
            ordered_actions.append(move)
        for move in takes:
            ordered_actions.append(move)
        for move in normal_moves:
            ordered_actions.append(move)
        return ordered_actions

    def utility(self):
        winner=self.winner()
        if winner=="w":
            return math.inf
        elif winner=="b":
            return -math.inf
        return self.material_eval()

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


                score = self.minimax(depth-1, alpha, beta)[0]

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



                score = self.minimax(depth - 1, alpha, beta)[0]

                beta=min(beta,score)


                self.undo_move(last_fen)

                if (score < best_score):
                    best_score = score
                    best_move = move
                if (beta <= alpha):
                    break

            return best_score, best_move

DEPTH=3
def main():
    game = Game()
    while not(game.winner()):

        print(game.turn)
        print(game.board)

        move=input("Your move...")
        game.play_move(move,True)
        game.last_fen=game.board.fen()
        print(game.board)
        print("AI is thinking...")
        minimax=game.minimax(DEPTH,-math.inf,math.inf)


        aimove=minimax[1]

        game.last_fen = game.board.fen()
        game.play_move(aimove,False)
    if(game.winner()=="w"):
        print("Congratulations you won")
    elif(game.winner()=="b"):
        print("AI won")
    else:print("Draw")

main()





import chess as ch
import random as rd

class engine:

    def __init__(self,board, maxdepth,color):
        self.board=board
        self.maxdepth=maxdepth
        self.color=color

    def getbestmove(self):
        return self.engine(None,1)

    def  evalfunct(self):
        compt =0
        for i in range (64):
            compt+=self.squareResPoints(ch.SQUARES[i])
        compt+=self.mateOpportunity()+self.openning()+0.001*rd.random()


    #to make bot  develope in the first moves
    def openning(self):
        if (self.board.fullmve_no <10):
            if (self.board.turn==self.color):
                return 1/30 *self.board.leagal_move.count()
            else:
                return -1/30 *self.board.leagal_move.count()
        else:
            return 0


    def mateOpportunity(self):
        if (self.board.legal_move.count()==0):
            if (self.board.turn ==self.color):
                return -999
            else:
                return 999
        else:
            return 0
    
    #Takes a square as input and returns the corresponding han's berliner's system value fo it's resident
    def squareResPoints(self, square):
        pieceValue =0
        if self.board.piece_type_at(square)== ch.PAWN:
            pieceValue=1
        
        elif(self.board.piece_type_at(square)== ch.ROOK):
            pieceValue=5.1
        
        elif(self.board.piece_type_at(square)== ch.BISHOP):
            pieceValue=3.33


        elif(self.board.piece_type_at(square)== ch.KNIGHT):
            pieceValue=3.2
        
        elif(self.board.piece_type_at(square)== ch.QUEEN):
            pieceValue=8.8

        if (self.board.color_at(square)== ch.color):
            return -pieceValue
        else:
            return pieceValue

    def engine(self,candidate,depth):
        if(depth==self.maxdepth or self.board.legal_moves.count()==0):
            return self.evalfunct()

        else:
            # get list of legal moves of the current position
            movelist =list(self.board.leagal_moves)

            #initialise newcandidate
            newcandidate=None

            if (depth % 2 != 0):
                newcandidate=float("-inf")
            
            else:
                newcandidate=float("-nif")

            #analyse board after deeper moves
            for i in movelist:

                #play the move i
                self.board.push(i)

                #get the value of move i
                value =self.engine(newcandidate,depth+1)

                #basic minmax algorithm:
                #if maximizing (engine's turn)
                if (value > newcandidate and depth % 2 != 0):
                    newcandidate =value
                    if (depth==1):
                        move=i
                    newcandidate =value

                #if minimizing (human player's turn)
                elif (value < newcandidate and depth % 2 !=0):
                    newcandidate =value
                

                #alpha-beta pruning cuts;
                #(if pervious move was made by the bot)
                if (candidate != None and value < candidate and depth %2 == 0):
                    self.board.pop()
                    break

                #(if pervious move was made by the human player)
                elif (candidate != None and value < candidate and depth %2 == 0):
                    self.board.pop()
                    break
                #undo last move
                self.board.pop()

        #return result
        if (depth>1):
            #return value of a mvoe in the tree
            return newcandidate
        
        else:
            #return the move (only on first move)
            return move

